# Module 4 — Marketing & Admissions: The Funnel and the Proof

**4:00 elapsed · 3:40 instructional · Prerequisite: Module 1**
**Competencies: C4, C5, C7**

---

## Premise

This is where the group can most easily prove value in rupees — and most easily
fool itself with a vanity metric. Board priority 4 is explicit: marketing spend
rose 34% while admissions rose 9%, and the Board wants the gap explained.

The module's discipline is **attribution honesty**: saying what the data can and
cannot support, especially when the confident version would be more welcome.

---

## Run sheet

| Start | Min | Type | Block |
|---|---|---|---|
| 0:00 | 15 | D | Commitments review |
| 0:15 | 20 | T | **Teach A** — Funnels, CPL vs CAC, and the metric that misleads |
| 0:35 | 40 | E | **Ex 4.1** — The group funnel and the 6× spread |
| 1:15 | 10 | — | Break |
| 1:25 | 20 | T | **Teach B** — Correlation, confounding, and what a trial would cost |
| 1:45 | 35 | E | **Ex 4.2** — Pressure-testing the follow-up effect |
| 2:20 | 35 | E | **Ex 4.3** — The counsellor's daily worklist |
| 2:55 | 10 | — | Break |
| 3:05 | 25 | E | **Ex 4.4** — The Board slide and the CFO's questions |
| 3:30 | 15 | T | **Teach C** — Establishing the capstone baseline |
| 3:45 | 15 | D | Commitment update and close |

---

## Teach A — CPL, CAC, and the metric that misleads

| Metric | What it measures | Why it misleads |
|---|---|---|
| Cost per lead | Efficiency of buying attention | Rewards cheap leads that never convert. A campus can halve CPL and admit fewer students. |
| **Cost per admission** | Efficiency of the whole funnel | The only one the Board should hear — but see below |
| Conversion rate | Funnel health | Ignores volume entirely; a campus with 20 enquiries and 40% conversion is not succeeding |

**And the correction that matters:** cost per admission is still the wrong basis
for a capital allocation decision when some campuses are full. The fact sheet
says three campuses are at capacity and five are the binding constraint on fill
rate. Moving budget toward a campus with excellent CAC and no seats produces
nothing.

A good Lead says this before the Board discovers it. Participants who reach it
in Ex 4.4 without prompting score at the top of the module.

---

## Ex 4.1 — The group funnel · 40 min

The full version of Module 1's Ex 1.6, extended.

**Data:** `marketing_admission_enquiries.csv` (2,518 rows),
`marketing_channel_spend.csv` (280 rows).

Beyond Module 1:

- **Month-by-month funnel**, handling the 116 blank `enquiry_date` rows
  explicitly: included in status counts, excluded from monthly cuts, and the
  exclusion stated.
- **Per-counsellor analysis**, and the honest caveat that counsellor and campus
  are entangled — a counsellor at a referral-led campus has an easier job, and
  nothing in this data separates skill from territory.
- **Channels with no spend line** — Referral, Walk-in, School Website, Alumni,
  Justdial — identified as uncostable rather than quietly excluded.
- **The Print anomaly**: ₹3,21,000 of spend with zero attributed enquiries.
  Either the CRM has no Print source value, or the channel produces nothing.
  Participants must state that this data cannot distinguish the two, and say
  what would.

**Reconciliation required:** 2,518 enquiries, ₹33,93,900 spend. A table that
does not reconcile means a failed join on campus names.

**Deliverable:** the full funnel pack with reconciliations and a stated list of
what is not knowable from this data.

---

## Ex 4.2 — Pressure-testing the follow-up effect · 35 min

The effect is real: 5.6% admission at ≤1 follow-up, 22.8% at ≥3. A 4.1× ratio
across 2,028 enquiries.

The exercise is to attack it, properly:

1. **Reverse causation.** Warm parents take more calls. Does follow-up create
   conversion, or does interest create both?
2. **Confounding by source.** The best campuses are referral-led, and referral
   converts at 27% against Meta's 8.9%. Recompute the follow-up effect **within
   each source** and see how much survives.
3. **Selection.** `followup_count` is measured at the end. Enquiries that
   convert quickly stop accruing follow-ups; dead ones may accrue several.
4. **The plateau.** Rates flatten after 3 and dip at 5. What does that shape
   suggest, and what does it rule out?

Then design the trial that would settle it: one campus, one intake cycle,
follow-up cadence assigned in advance rather than chosen, compared within
source. State what it would cost, what it would risk, and how long before it
answers.

**Deliverable:** the within-source recomputation, the four challenges answered
with numbers, and the trial design.

**Marked hardest on:** whether the participant's final position is
proportionate to the evidence. Both "it's proven" and "we can't know anything"
are wrong answers.

---

## Ex 4.3 — The counsellor's daily worklist · 35 min

Analysis nobody acts on is worth nothing. Build what a counsellor with 40 open
enquiries can act on before 11 a.m.

Requirements:

- At most **12 enquiries**, ranked, with the reason each is on the list.
- The next action for each, in a few words.
- A stated rule for what falls off, so the list does not silently become a
  backlog.
- Fits on one screen.
- **Lane 1**: it prompts a human call, it does not send anything.

Then the constraint that makes it real: **no enquiry appears on the list more
than three days running without being escalated or closed.** Ask participants
what happens without that rule. The answer is that the same twelve names sit
there forever and the counsellor stops opening it — which is how most worklists
die.

**Deliverable:** the worklist for one campus, the ranking logic, the falloff
rule, and the specification of it as a reusable asset.

---

## Ex 4.4 — The Board slide · 25 min

One slide. Under 200 words. One headline number, three sentences, one table of
at most six rows, one decision the Board must take with its cost and expected
return, and the main caveat stated plainly in the body.

Then: the three questions a sceptical CFO asks, and the honest answer to each —
including where the honest answer is "we don't know from this data."

Then the capacity correction: what changes in the recommendation once
at-capacity campuses are excluded from spend reallocation, and the two sentences
that stop the Board moving budget to a campus with no seats.

**Deliverable:** the slide, the three CFO questions with answers, and the
capacity correction.

---

## Teach C — Establishing the capstone baseline

The last fifteen minutes of teaching in the programme before Module 5, and the
most consequential.

A baseline must be:

- **Taken before the build.** Not reconstructed. This is irreversible — no later
  measurement can recover it, and a reconstructed baseline presented as an
  original is an automatic certification exclusion.
- **The same metric, measured the same way, both times.**
- **Attributable.** What else changed in the period? Admission season, a fee
  revision, a new campus, a competitor opening. Say so.
- **Honest about the counterfactual.** What would have happened anyway?

Participants leave with their baseline metric defined and a date to collect it,
before Module 5.

---

## Module 4 deliverables

1. Full funnel pack with reconciliations and a stated list of unknowables
2. Within-source recomputation, four challenges answered, trial design
3. Counsellor worklist with ranking logic, falloff rule, and asset spec
4. Board slide, CFO questions, capacity correction
5. Capstone baseline metric defined with a collection date

**Marks: 100. Pass: 70.** Floor: presenting the follow-up effect as established
causation caps the module at 65.
