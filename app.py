from langgraph.graph import StateGraph, START, END
from typing import TypedDict
import google.generativeai as genai

GENAI_API_KEY = "AIzaSyAwyxBz9IRWv2mF2b7OwkIHcp4dg508t8s"
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel("models/gemini-2.5-flash")

class Agentstate(TypedDict):
    topic: str
    memory: str
    round: int
    response: str
    current_person: str
    Judgement: str

def user_node(state: Agentstate) -> Agentstate:
    print("\nStarting debate between Scientist and Philosopher...\n")
    state["round"] = 0
    state["memory"] = ""
    return state

def scientist(state: Agentstate) -> Agentstate:
    state["current_person"] = "Scientist"
    state["round"] += 1
    prompt = f"""
You are a Scientist debating the topic: "{state['topic']}".
Here is your memory: {state['memory']}
This is round {state['round']}.
Be concise and logical. State your argument clearly in just 2 lines.
"""
    state["response"] = model.generate_content(prompt).text.strip()
    return state

def philosopher(state: Agentstate) -> Agentstate:
    state["current_person"] = "Philosopher"
    state["round"] += 1
    prompt = f"""
You are a Philosopher debating the topic: "{state['topic']}".
Here is your memory: {state['memory']}
This is round {state['round']}.
Be concise and logical. State your argument clearly in just 2 lines.
"""
    state["response"] = model.generate_content(prompt).text.strip()
    return state

def memory_node(state: Agentstate) -> Agentstate:
    message = f"[Round {state['round']}] {state['current_person']}: {state['response']}\n"
    print(message)
    state["memory"] += message
    return state

def check(state: Agentstate) -> str:
    if state["round"] == 8:
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(f"\nDebate topic: {state['topic']}\n")
            f.write(f"{state['memory']}\n")
        return "Judge"
    if state["current_person"] == "Scientist":
        return "Philosopher"
    return "Scientist"

def judge(state: Agentstate) -> Agentstate:
    conversation = state["memory"]
    topic = state["topic"]
    prompt = f"""
You are the Judge of a debate on the topic: "{topic}".
Here is the full transcript:
{conversation}

1. Summarize each participant's core points.
2. Evaluate their logic and reasoning.
3. Declare the winner and justify your choice (cannot be a tie).

Format:
Summary:
- Scientist: ...
- Philosopher: ...

Evaluation:

Winner: [Scientist/Philosopher]
Reason: ...
"""
    result = model.generate_content(prompt).text.strip()
    final_judgment = f"[Judge] {result}"
    print(final_judgment)
    state["Judgement"] = final_judgment
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"{final_judgment}\n")
    return state

graph = StateGraph(Agentstate)
graph.add_node("User_node", user_node)
graph.add_node("Scientist", scientist)
graph.add_node("Philosopher", philosopher)
graph.add_node("Memory", memory_node)
graph.add_node("Judge", judge)

graph.add_edge(START, "User_node")
graph.add_edge("User_node", "Scientist")
graph.add_edge("Scientist", "Memory")
graph.add_edge("Philosopher", "Memory")

graph.add_conditional_edges(
    "Memory",
    check,
    {"Philosopher": "Philosopher", "Scientist": "Scientist", "Judge": "Judge"},
)

graph.add_edge("Judge", END)
from graphviz import Digraph

dot = Digraph(comment="LangGraph Debate DAG", format="png")

dot.attr(rankdir="LR", size="8,5")
dot.attr("node", shape="box", style="rounded,filled", fontname="Helvetica")

# Define nodes with colors
dot.node("START", "START", fillcolor="#E0E0E0")
dot.node("User_node", "User Node", fillcolor="#BBDEFB")
dot.node("Scientist", "Scientist", fillcolor="#C8E6C9")
dot.node("Philosopher", "Philosopher", fillcolor="#FFE0B2")
dot.node("Memory", "Memory", fillcolor="#FFF9C4")
dot.node("Judge", "Judge", fillcolor="#FFCDD2")
dot.node("END", "END", fillcolor="#E0E0E0")

# Define edges
dot.edge("START", "User_node")
dot.edge("User_node", "Scientist")
dot.edge("Scientist", "Memory")
dot.edge("Philosopher", "Memory")
dot.edge("Memory", "Philosopher", label="If Scientist", color="blue")
dot.edge("Memory", "Scientist", label="If Philosopher", color="green")
dot.edge("Memory", "Judge", label="If round == 8", color="red")
dot.edge("Judge", "END")

dot.render("flowdiagram", cleanup=True)
print(" flowdiagram.png generated successfully.")

app = graph.compile()

if __name__ == "__main__":
    topic = input("Enter debate topic: ")
    app.invoke({"topic": topic})
