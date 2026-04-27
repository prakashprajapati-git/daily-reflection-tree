# Persona 2 Transcript — The Growth Path

**Profile:** Victor / Contributor / Altrocentric  
**Purpose:** Demonstrates the tree routing an employee who owns their agency, focuses on giving, and keeps others in their frame.

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

  Your choice (enter a number): 2

  ❓  You said 'Productive'. When something went well today, what made it happen?

     1.  I prepared well and stayed focused
     2.  Honestly, the timing just worked out
     3.  I adapted quickly when the situation shifted
     4.  The team came through — I relied on others

  Your choice (enter a number): 1

  ──────────────────────────────────────────────────

  💡  You described today as 'Productive' — and you stayed in the driver's
      seat through it. That's not a small thing. Seeing the link between
      your choices and outcomes is exactly what separates learning from
      just surviving a day.

  ──────────────────────────────────────────────────

  [Press Enter to continue]

  ··················································

  🌉  Now that we've looked at how you moved through the day — let's look
      at where your energy was directed.

  ··················································

  ❓  In your interactions today, which of these thoughts feels most honest?

     1.  I hope the effort I put in was noticed
     2.  I hope my work moved something forward for the team
     3.  I was mostly focused on getting through my own list
     4.  I kept looking for where I could be most useful

  Your choice (enter a number): 4

  ❓  Was there a moment today where you helped someone with something
      that wasn't strictly your responsibility?

     1.  Yes — and it felt like the right thing to do
     2.  It felt like a fair trade for the effort I put in
     3.  I thought about it but didn't act on it

  Your choice (enter a number): 1

  ──────────────────────────────────────────────────

  💡  You're drawing satisfaction from the act of contributing — not from
      the applause that follows. That's a quietly powerful place to work
      from. The people around you feel it, even when they don't say it.

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

  Your choice (enter a number): 4

  ❓  When you hit a hard moment today, who came to mind?

     1.  Just me — it was my problem to solve
     2.  My team — we were all affected by this
     3.  A specific colleague who had it harder than me
     4.  The end user or customer we're serving

  Your choice (enter a number): 2

  ──────────────────────────────────────────────────

  💡  You kept others in your frame today — a colleague, a user, the
      mission. That kind of perspective-taking is what turns individual
      effort into collective progress. It's easy to miss. You didn't.

  ──────────────────────────────────────────────────

  [Press Enter to continue]

════════════════════════════════════════════════════════

  📊  YOUR REFLECTION SUMMARY

════════════════════════════════════════════════════════

  Today's reflection: You moved through a 'Productive' day with a
  proactive, agency-led orientation — seeing your work through a
  contribution-focused lens, and holding an outward-looking view of
  your impact.

  These aren't fixed traits. They're today's snapshot.
  Come back tomorrow and see what shifts.

════════════════════════════════════════════════════════

  🏁  That's it for today. Rest well — tomorrow is a fresh page.
```

---

## Path Taken

| Node                   | Answer chosen                                   | Branch triggered                                            |
| ---------------------- | ----------------------------------------------- | ----------------------------------------------------------- |
| `q_energy_check`       | Productive                                      | → `q_locus_impact`                                          |
| `q_locus_impact`       | I prepared well and stayed focused              | → `d_locus_victor` → `r_locus_victor`                       |
| `q_orientation_focus`  | I kept looking for where I could be most useful | → `q_contribution_check`                                    |
| `q_contribution_check` | Yes — and it felt like the right thing to do    | → `d_orientation_contributor` → `r_orientation_contributor` |
| `q_radius_scope`       | For the larger mission we're working toward     | → `q_radius_wide`                                           |
| `q_radius_wide`        | My team — we were all affected by this          | → `d_radius_altro` → `r_radius_altro`                       |
| `summary_node`         | —                                               | locus=victor · orientation=contributor · radius=altro       |
