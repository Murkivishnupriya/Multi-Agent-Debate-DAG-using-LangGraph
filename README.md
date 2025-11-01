## Multi-Agent Debate DAG using LangGraph

A state-driven, multi-agent debate simulation built with LangGraph, Google Gemini 2.5 Flash, and Graphviz.Two AI agents — a Scientist and a Philosopher — engage in an eight-round structured debate on a user-given topic.The debate flow, memory management, and decision logic are represented as a Directed Acyclic Graph (DAG).

## Overview

This project demonstrates a multi-agent workflow system where autonomous agents participate in a formal debate managed through LangGraph.
The system alternates control between the two agents, tracks the discussion in memory, and evaluates the outcome through a Judge Node.

Each execution generates:

1) A complete transcript of the debate in log.txt

2) A visual workflow diagram (flowdiagram.png) using Graphviz


## SYSTEM ARCHITECTURE
__________________________________________________________________________________________________
| Component                 | Description                                                         |
| ------------------------- | ------------------------------------------------------------------- |
| **UserInputNode**         | Accepts the debate topic from the user                              |
| **Scientist (Agent A)**   | Provides evidence-based, logical arguments                          |
| **Philosopher (Agent B)** | Provides conceptual and ethical counterpoints                       |
| **MemoryNode**            | Maintains dialogue history and manages turn-based flow              |
| **JudgeNode**             | Analyzes all responses, summarizes arguments, and declares a winner |
| **LangGraph DAG**         | Defines and executes the debate state transitions                   |
| **Graphviz**              | Visualizes the entire system as a DAG diagram                       |



## Workflow Design

## Node Flow Diagram

START
  ↓
UserInputNode
  ↓
Scientist ↔ Philosopher
  ↕
 MemoryNode
  ↓
JudgeNode
  ↓
END


## Data Flow

User provides the debate topic.

Agents alternate for 8 rounds (4 each).

Each response is stored in MemoryNode.

Once rounds complete, JudgeNode evaluates the conversation.

Results and summaries are logged in log.txt.

Graphviz generates flowdiagram.png for workflow visualization.

## Features

Multi-agent debate system using LangGraph

Controlled workflow with 8 rounds of structured dialogue

Real-time argument generation using Google Gemini 2.5 Flash

Memory management and state transitions

Automated evaluation and winner declaration

Full transcript logging

DAG visualization using Graphviz

## Installation
## Prerequisites

Python 3.10+

Graphviz (installed and added to PATH)

A valid Google Gemini API key


## SETUP
cd Multi-Agent-Debate-DAG-using-LangGraph
python -m venv venv
venv\Scripts\activate
pip install -r requirement.txt

## If requirement.txt is not updated, you can manually install:
pip install langgraph google-generativeai graphviz

Verify Graphviz installation:
dot -V


## Usage
Set the API Key

You can configure the Gemini API key in one of the following ways:
1) Option 1 — Inside the script

GENAI_API_KEY = "YOUR_API_KEY"

2) Option 2 — As an environment variable
set GEMINI_API_KEY=your_api_key_here

## RUN THE PROGRAM
python app.py


## SAMPLE OUTPUT

Enter debate topic: Should AI replace teachers?

# EXAMPLE OUTPUT

Starting debate between Scientist and Philosopher...

[Round 1] Scientist: AI can scale personalized education efficiently.
[Round 2] Philosopher: Human empathy cannot be automated.

[Judge] Summary:
Scientist: Focused on scalability and accessibility.
Philosopher: Emphasized ethics and human connection.
Winner: Philosopher
Reason: Presented deeper reasoning and moral perspective.

## Validation

1) Both agents alternate strictly in turn.

2) The system executes 8 total rounds (4 per agent).

3) The MemoryNode correctly tracks and updates state.

4) JudgeNode evaluation concludes the debate with clear reasoning.

5) All steps are logged and visualized.


## Summary

This project fulfills the ATG technical assignment requirements for building a multi-agent debate DAG using LangGraph.It integrates structured conversation logic, AI-generated reasoning, workflow orchestration, and visual representation of state transitions in a modular, reproducible format.


## Developer

Murki Vishnupriya
Machine Learning Intern



