# Daily Reflection Tree: A Deterministic Psychological Mirror

This repository contains a psychologically grounded end-of-day reflection tool designed for employees. It uses a deterministic decision tree to help users navigate three critical psychological axes: **Locus of Control**, **Orientation**, and **Radius of Impact**.

## 🚀 Overview
The tool is designed as a **Deterministic State Machine**. While AI was used to architect the logic and content, the final product runs purely on fixed JSON data—ensuring zero hallucination, consistent paths, and reliable, high-fidelity insights without the need for an LLM at runtime.

## 📂 Project Structure
- **/tree/**
    - `reflection-tree.json`: The complete decision tree logic (26 nodes).
    - `tree-diagram.md`: A Mermaid-js visual representation of the logic flow.
- **/agent/**
    - `main.py`: The Python CLI engine that executes the reflection tree.
    - `requirements.txt`: Project dependencies (Standard Library only).
- **/transcripts/**
    - `persona-1-transcript.md`: A walkthrough of the "Narrow/Victim" path.
    - `persona-2-transcript.md`: A walkthrough of the "Growth/Victor" path.
- `write-up.md`: 2-page detailed design rationale and psychological grounding.

## 🧠 Psychological Axes
1. **Locus (Victim ↔ Victor):** Based on Rotter (1954), measuring internal vs. external control.
2. **Orientation (Entitlement ↔ Contribution):** Based on Organ (1988), measuring focus on receiving vs. giving.
3. **Radius (Self-Centric ↔ Altrocentric):** Based on Maslow (1969), measuring the scope of impact.

## 🛠️ How to Run the Agent
To experience the reflection tool, ensure you have Python 3 installed and follow these steps:

1. Clone the repository:
   git clone https://github.com/prakashprajapati-git/daily-reflection-tree.git

2. Navigate to the project directory:
   cd daily-reflection-tree

3. Run the agent:
   python agent/main.py

## 🛠️ Tech Stack
- **Data Structure:** JSON (Deterministic Logic Storage)
- **Logic Engine:** Python 3.x (State Machine Implementation)
- **Visualization:** Mermaid.js (Logic Mapping)
- **Documentation:** Markdown