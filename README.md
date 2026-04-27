# Daily Reflection Tree

A deterministic end-of-day reflection tool built for the DeepThought CultureTech Fellowship assignment.

**Author:** Prakash Kumar Prajapati

---

## What This Is

A CLI tool that walks an employee through a structured evening reflection using a decision tree. The employee picks from fixed options, the tree branches based on their answers, and they end the session with a clearer picture of how they showed up that day.

No free text. No LLM at runtime. No randomness. Same answers always produce the same path — by design.

---

## Psychological Axes

The tree moves through three axes in sequence:

| Axis            | Spectrum                    | Source                               |
| --------------- | --------------------------- | ------------------------------------ |
| **Locus**       | Victim ↔ Victor             | Rotter (1954), Dweck (2006)          |
| **Orientation** | Entitlement ↔ Contribution  | Campbell et al. (2004), Organ (1988) |
| **Radius**      | Self-Centric ↔ Altrocentric | Maslow (1969), Batson (2011)         |

Each axis builds on the previous one — it's one conversation, not three independent quizzes.

---

## Project Structure

```
daily-reflection-tree/
├── tree/
│   ├── reflection-tree.json     # The complete decision tree (35 nodes)
│   └── tree-diagram.md          # Mermaid visual of every node and branch
├── agent/
│   ├── main.py                  # Python CLI engine (pure state machine)
│   └── requirements.txt         # No external dependencies — stdlib only
├── transcripts/
│   ├── persona-1-transcript.md  # Victim / Entitled / Self-Centric path
│   └── persona-2-transcript.md  # Victor / Contributor / Altrocentric path
├── write-up.md                  # Design rationale (psychological grounding, trade-offs)
└── README.md
```

---

## How to Run

**Requirements:** Python 3.7+, no external packages needed.

```bash
# 1. Clone the repository
git clone https://github.com/prakashprajapati-git/daily-reflection-tree.git

# 2. Enter the project directory
cd daily-reflection-tree

# 3. Run the agent
python agent/main.py
```

The agent loads `tree/reflection-tree.json` automatically. Run it from the project root.

---

## How to Read the Tree

Open `tree/reflection-tree.json`. Each node has:

| Field     | Purpose                                                                                           |
| --------- | ------------------------------------------------------------------------------------------------- |
| `id`      | Unique node identifier                                                                            |
| `type`    | `start` / `question` / `decision` / `reflection` / `bridge` / `summary` / `end`                   |
| `text`    | What the employee sees. `{node_id}` placeholders are replaced with earlier answers at render time |
| `options` | Fixed choices (question nodes only). Each option has a `next` pointer and optional `signal`       |
| `signal`  | Records axis state — e.g. `axis1:internal`, `axis2:entitlement`                                   |
| `logic`   | Decision nodes only — e.g. `set locus=victim`                                                     |
| `next`    | Next node ID (non-question nodes)                                                                 |

Every path through the tree is traceable by following `next` and `options[n].next` fields — no code needed.

---

## Tree at a Glance

- **35 nodes** across 7 types
- **12 question nodes** — all with 3–4 fixed options
- **2 branching paths per axis** — one per pole of each spectrum
- **Full answer interpolation** — reflections reference the employee's exact earlier words
- **Zero runtime dependencies** — the tree is static JSON walked by a simple state machine

See `tree/tree-diagram.md` for the full Mermaid visual, or `transcripts/` for two complete walkthroughs showing how different answers produce different paths and reflections.

---

## Design Notes

See `write-up.md` for the full rationale. The short version:

- Questions target internal monologue, not observable behavior — because entitlement and locus are invisible from the outside
- The victim path routes through `q_locus_choice` before crossing to Axis 2 — giving the employee one more chance to surface their own agency rather than being told they had it
- Binary decision nodes were chosen over weighted scoring deliberately — a tired employee at 7pm needs a clear path, not a percentage score
