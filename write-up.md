# Design Rationale: The Daily Reflection Tree

**Author:** Prakash Kumar Prajapati  
**Role:** Artificial Intelligence Internship Applicant — DeepThought CultureTech Ventures Private Limited 

---

## 1. Psychological Foundation

**Axis 1 — Locus (Victim ↔ Victor)**  
_Sources: Rotter (1954); Dweck (2006)_

Questions probe the first instinct under friction and the attribution
of success — the two most reliable markers of locus orientation from
Rotter's original scale. The victim path routes through a secondary
question (`q_locus_choice`) that asks "Did you have any choice in how
you responded?" rather than stating the answer. This embodies the
assignment's "wise colleague" tone — it invites the employee to find
their agency, not be told they had it.

**Axis 2 — Orientation (Entitlement ↔ Contribution)**  
_Sources: Campbell et al. (2004); Organ (1988)_

Entitlement is invisible to the person holding it — it manifests as
felt deprivation, not conscious claim. Questions therefore target
internal monologue ("which thought feels most honest?") rather than
behavior. A tiebreaker node (`q_orientation_extra`) forces a direct
choice between recognition and impact — the clearest moment where
orientation becomes undeniable. I avoided "Did you help a colleague?"
because it invites socially desirable answers regardless of internal
state.

**Axis 3 — Radius (Self-Centric ↔ Altrocentric)**  
_Sources: Maslow (1969); Batson (2011)_

The axis asks who the employee was "ultimately doing it for" —
borrowing Batson's perspective-taking framing. The narrow path routes
through `q_radius_extra` ("Did you check in on anyone — not because
it was required?") before concluding. This prevents the tree from
delivering a binary verdict and gives the employee one more chance to
surface altrocentric behavior.

---

## 2. Technical Architecture

The tree contains 35 nodes across 7 types, encoded in a single JSON
file. Every path is traceable by following node IDs without running
code. The Python agent is a pure state machine — identical inputs
always produce identical outputs, with zero API calls at runtime.

Answer interpolation stores the user's chosen text by node ID and
resolves `{node_id}` placeholders at render time, producing
personalized reflections ("You described today as 'Exhausting'...")
without any generative model. Decision nodes carry `signal` fields
(`axis1:internal`, `axis2:entitlement`) that make the psychological
meaning of each routing decision auditable.

---

## 3. AI Collaboration and Guardrails

Gemini 2.5 Pro (Thinking mode) was used for research, question
drafting, and code generation. Hallucination was controlled
structurally — a strict JSON schema meant any invented node IDs or
broken routing chains were caught immediately by the Python loader.
The final product contains no runtime AI dependency.

**Negative prompting:** I explicitly banned clinical language,
motivational-poster language, and managerial framing. Target register:
a wise peer who observes without judging.

**Where I overrode the AI:** The AI routed all Axis 1 paths directly
to the bridge after one reflection. I rejected this — the victim path
needed `q_locus_choice` to surface agency as a question, not assert
it as a conclusion. I rewrote that branch manually.

---

## 4. Trade-offs and What I'd Improve

**Binary vs. weighted scoring:** The tree uses binary decision nodes
for clarity. A weighted tally across multiple questions per axis would
add nuance — but a tired employee at 7pm needs a clear path, not a
percentage score.

**With more time I would add:**

- Weighted axis scoring replacing binary decision nodes
- Full answer interpolation in every reflection node
- 30-day session history to surface axis trends over time
- A fourth axis — Temporality (rumination vs. anticipation) based on
  Seligman (2011) and Nolen-Hoeksema's work

---

_The questions are the product. Everything else is scaffolding._
