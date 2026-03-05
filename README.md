# Agentic Logic Circuit Analyzer 🔌

An autonomous AI agent built with [LangGraph](https://github.com/langchain-ai/langgraph), implementing the ReAct (Reasoning and Acting) architecture to analyze digital logic circuits, calculate discrete math structures, and solve hardware-level state problems deterministically.

## 🚀 The Problem It Solves
Large Language Models (LLMs) are notoriously bad at deterministic calculations and hardware logic (such as identifying precise Flip-Flop timing diagrams or resolving SR Latch race conditions). They tend to hallucinate mathematical outcomes. 

This project solves that by transforming the LLM into a **router/orchestrator**. The core logic is defined in `src/react_agent/graph.py`. Instead of guessing the outputs of digital circuits, the agent iteratively reasons about user queries and executes actions by calling custom, strictly-typed Python logic tools. 

## ⚙️ How It Works (The ReAct Loop)
The agent follows a strict reasoning loop:
1. Takes a user **query** as input (e.g., "What happens if both S and R inputs are 1 in an active-high NOR latch?")
2. Reasons about the query and decides which hardware-logic tool to trigger.
3. Executes the chosen action using available tools (bypassing LLM hallucinations).
4. Observes the result of the action.
5. Repeats the process or provides a final, verified engineering answer.

## 🛠️ Custom Tools (`src/react_agent/tools.py`)
The agent has been extended with custom tools tailored for Computer Engineering contexts:
- `analyze_sr_latch`: Calculates exact states for Set-Reset latches based on previous states (Q).
- `prufer_code_generator`: Resolves tree topologies for discrete math verifications.

## 💻 Getting Started

1. Clone the repository and navigate to the project directory.
2. Create your environment variables file:
```bash
cp .env.example .env