Design Rationale: The Daily Reflection Tree
Author: Prakash Kumar Prajapati

Role: Artificial Intelligence Internship Applicant | DeepThought CultureTech Ventures Private Limited 

1. Psychological Foundation
The tree is built on three distinct but interconnected psychological axes, designed to move an employee from a reactive state to a proactive, contribution-oriented mindset.

Axis 1: Locus (Victim ↔ Victor)
Theory: Julian Rotter’s Locus of Control (1954) and Carol Dweck’s Growth Mindset.

Implementation: Questions target "Energy" and "Reaction to Friction." By identifying if an employee blames "the world" or "luck" (External Locus) versus "effort" or "strategy" (Internal Locus), the tree provides a mirror for their agency.

Design Choice: I used neutral language like "drained" vs "satisfied" to avoid triggering defensive responses, allowing for a more honest self-assessment.

Axis 2: Orientation (Entitlement ↔ Contribution)
Theory: Psychological Entitlement (Campbell) and Organizational Citizenship Behavior (Organ).

Implementation: This axis probes the intent behind actions. Is the employee focused on "what I am owed" (Support/Notice) or "what I gave" (Helping the team)?

Design Choice: The "Checklist" option acts as a neutral "hidden" path that reveals a self-preservation mindset, which often correlates with a lack of contribution-focus.

Axis 3: Radius (Self-Centric ↔ Altrocentric)
Theory: Maslow’s Self-Transcendence and Batson’s Perspective-Taking.

Implementation: The final shift focuses on the scope of the day’s work. Did the impact end at the employee’s desk, or did it reach the customer or the broader mission?

Design Choice: Questions ask about the "next thought" after finishing a task, capturing the "Radius" of their concern in a moment of transition.

2. Technical Architecture
The system is designed as a Deterministic State Machine.

Zero-LLM Runtime: To ensure 100% reliability and zero latency, the logic is stored in a structured reflection-tree.json. This makes the "reflection" safe, consistent, and traceable.

Modular Node Types: By defining start, question, decision, bridge, and summary nodes, the engine (main.py) can be extended with thousands of new questions without changing a single line of code.

State Interpolation: The summary_node uses placeholder interpolation ({locus}, {orientation}, etc.). This allows the tool to generate a "personalized" story at the end while remaining strictly logic-driven.

3. AI Collaboration & Guardrails
In alignment with the assignment guidelines, AI was used as a collaborative architect, not a blind generator.

Negative Prompting: I strictly instructed the AI not to use clinical, managerial, or "toxic positivity" language. I forced the AI to adopt the persona of a "Wise Peer"—someone who observes rather than judges.

Controlling Hallucination: Since the final product is a JSON file, the "Hallucination" risk was mitigated by defining a strict Schema. Any "hallucinated" fields by the AI were immediately caught by the Python loader during the development phase.

Human-in-the-Loop: I manually adjusted the transitions between Axis 1 and 2, as the AI initially suggested a "quiz-like" break. I re-wrote the bridge nodes to ensure the conversation felt like a single, flowing experience.