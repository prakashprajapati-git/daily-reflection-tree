# Persona 1 Transcript — The Narrow Path

**Profile:** Victim / Entitled / Self-Centric  
**Purpose:** Demonstrates the tree routing an employee who externalises blame, seeks recognition, and stays self-focused.

---

```
════════════════════════════════════════════════════════

  ✨  Good evening. This is your space — no performance, no judgment.
      Let's take a quiet look at your day.

════════════════════════════════════════════════════════

  [Press Enter to begin your reflection]

  ❓  Before we dive in — how would you describe today in one word or phrase?

     1.  Exhausting
     2.  Productive
     3.  Frustrating
     4.  Steady — nothing dramatic

  Your choice (enter a number): 3

  ❓  You said 'Frustrating'. When something didn't go as planned today,
      what was your first instinct?

     1.  Figure out what I could still control
     2.  Feel frustrated by things outside my control
     3.  Wait and see if things sorted themselves out
     4.  Adapt and find another way through

  Your choice (enter a number): 2

  ──────────────────────────────────────────────────

  💡  You described today as 'Frustrating'. A day like that pulls attention
      outward — to what others did or didn't do, to what the situation
      allowed or didn't. That's a fair response. But somewhere in there,
      you made at least one call. Even waiting is a choice.

  ──────────────────────────────────────────────────

  [Press Enter to continue]

  ❓  Think of one moment today where things got difficult. Looking back —
      did you have any choice in how you responded?

     1.  Yes — I could have responded differently and I knew it
     2.  Not really — the situation left me no room
     3.  Maybe — I didn't stop to think about it at the time

  Your choice (enter a number): 2

  ··················································

  🌉  Now that we've looked at how you moved through the day — let's look
      at where your energy was directed.

  ··················································

  ❓  In your interactions today, which of these thoughts feels most honest?

     1.  I hope the effort I put in was noticed
     2.  I hope my work moved something forward for the team
     3.  I was mostly focused on getting through my own list
     4.  I kept looking for where I could be most useful

  Your choice (enter a number): 1

  ❓  When things didn't go your way today, what was your internal reaction?

     1.  I felt I deserved more support than I received
     2.  I looked for ways to adjust my own approach to the situation
     3.  I felt frustrated that others weren't pulling their weight

  Your choice (enter a number): 1

  ──────────────────────────────────────────────────

  💡  It's natural to want recognition — we all carry that need. But when
      'what did I receive today' becomes louder than 'what did I give today',
      the work starts to feel hollow. That gap is worth noticing.

  ──────────────────────────────────────────────────

  [Press Enter to continue]

  ··················································

  🌉  One last shift — let's zoom out and look at who was in your frame today.

  ··················································

  ❓  Think about the most meaningful thing you did today.
      Who were you ultimately doing it for?

     1.  Primarily to clear my own backlog
     2.  For a specific colleague or teammate
     3.  For a user or customer I may never meet
     4.  For the larger mission we're working toward

  Your choice (enter a number): 1

  ❓  After you finished that task, what was the first thing on your mind?

     1.  What's next on my list
     2.  Whether the person receiving this would find it useful
     3.  Whether this moved the needle for the team

  Your choice (enter a number): 1

  ❓  Did you check in on anyone today — not because it was required,
      but because you noticed they might need it?

     1.  Yes — and it mattered to them
     2.  No — I was too focused on my own work
     3.  I noticed but didn't act on it

  Your choice (enter a number): 2

  ──────────────────────────────────────────────────

  💡  Today, your frame was tight — focused on your own execution and
      immediate responsibilities. That's not wrong. But the most meaningful
      work tends to happen when we occasionally look up from our own list
      and ask who else is affected by what we do.

  ──────────────────────────────────────────────────

  [Press Enter to continue]

════════════════════════════════════════════════════════

  📊  YOUR REFLECTION SUMMARY

════════════════════════════════════════════════════════

  Today's reflection: You moved through a 'Frustrating' day with a
  reactive, externally-driven orientation — seeing your work through a
  receiving-focused lens, and holding a personally-centered view of
  your impact.

  These aren't fixed traits. They're today's snapshot.
  Come back tomorrow and see what shifts.

════════════════════════════════════════════════════════

  🏁  That's it for today. Rest well — tomorrow is a fresh page.
```

---

## Path Taken

| Node                  | Answer chosen                                  | Branch triggered                                       |
| --------------------- | ---------------------------------------------- | ------------------------------------------------------ |
| `q_energy_check`      | Frustrating                                    | → `q_locus_friction`                                   |
| `q_locus_friction`    | Feel frustrated by things outside my control   | → `d_locus_victim` → `r_locus_victim`                  |
| `q_locus_choice`      | Not really — the situation left me no room     | → `d_locus_choice_victim` → `bridge_locus_orientation` |
| `q_orientation_focus` | I hope the effort I put in was noticed         | → `q_entitlement_check`                                |
| `q_entitlement_check` | I felt I deserved more support than I received | → `d_orientation_entitled` → `r_orientation_entitled`  |
| `q_radius_scope`      | Primarily to clear my own backlog              | → `q_radius_narrow`                                    |
| `q_radius_narrow`     | What's next on my list                         | → `q_radius_extra`                                     |
| `q_radius_extra`      | No — I was too focused on my own work          | → `d_radius_extra_self` → `r_radius_self`              |
| `summary_node`        | —                                              | locus=victim · orientation=entitled · radius=self      |
