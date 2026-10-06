# Module 5 — Governance: Privacy, Approval, Audit

**3:00 elapsed · 2:45 instructional · Prerequisite: Modules 1–4**
**Competencies: C6, C8**

> **This module gates access to real group data.** No participant may use real
> student, parent, employee or vendor data in any AI workflow until they have
> completed it and their written real-data case has been approved. Nothing in
> the programme is more strictly enforced.

---

## Premise

The fastest way to end an AI programme in a school group is one incident
involving a child's data. Not a policy breach in the abstract — a specific
parent, a specific message, a specific screenshot on a specific WhatsApp group.

This module is about making that not happen, and about being able to show
afterwards exactly what was done and why.

---

## Run sheet

| Start | Min | Type | Block |
|---|---|---|---|
| 0:00 | 10 | D | Commitments review — abbreviated |
| 0:10 | 25 | T | **Teach A** — Personal data in a school: what the law wants and what parents expect |
| 0:35 | 30 | E | **Ex 5.1** — Lane classification of twelve live workflows |
| 1:05 | 10 | — | Break |
| 1:15 | 20 | T | **Teach B** — Audit trails that reconstruct a decision |
| 1:35 | 30 | E | **Ex 5.2** — The group's one-page AI Use Standard |
| 2:05 | 25 | E | **Ex 5.3** — Peer red-team: find the disclosure path they missed |
| 2:30 | 25 | E | **Ex 5.4** — The real-data gate |
| 2:55 | 5 | D | Close |

**Attendance:** the Group IT & Compliance representative attends this module.
If they cannot, it does not run — the deliverables need their sign-off and a
standard written without them will not be enforced.

---

## Teach A — Personal data in a school

**What the law wants** (DPDP-shaped obligations, as they apply here):

| Principle | In practice at Meridian |
|---|---|
| Purpose limitation | Data collected for admission is not available for marketing analysis without a fresh basis |
| Data minimisation | If the analysis does not need the name, the name does not go in |
| Children's data | Materially higher protection; verifiable parental consent; no behavioural tracking or targeted advertising |
| Storage limitation | Alumni enquiry data from 2019 has no current purpose |
| Security | Cl. 9.2 — the Approved Systems List is the operative control |
| Breach notification | Cl. 9.4 — within 24 hours of discovery, to the Group HR Head |

**What parents expect**, which is stricter and matters more day to day: that
what they tell the school about their child stays inside the school, is used to
help their child, and is not visible to other parents or to staff with no reason
to see it.

**The practical test** that resolves most cases without a lawyer:

> Would you be comfortable if this parent saw exactly what you did with their
> child's data, and why? If the answer needs explaining, it is a no.

### Minimisation in practice

Almost no analysis needs identity. It needs *what, how much, how long, against
which rule.* Before any personal data enters a workflow, ask what the name is
doing for the analysis. The answer is usually nothing — and where it is
something, that is a Lane and consent question, not a convenience one.

---

## Ex 5.1 — Lane classification · 30 min

Twelve live workflows drawn from Modules 1–4. Classify each: Lane 1 Draft,
Lane 2 Decide-support, or Never.

The set includes the genuinely hard cases, and these are the marked ones:

| Workflow | Why it is hard |
|---|---|
| Drafting an R6 formal demand letter | Lane 1, but carries a legal representation — approval level changes |
| Summarising exit interviews to explain 19% attrition | Lane 2, but small campuses make individuals identifiable in aggregate |
| Ranking candidates from applications | **Never.** Feels like Lane 2. It determines a hiring outcome. |
| Drafting a Principal's note about repeated absence of a named child | **Never.** Named child, behavioural. |
| Producing the intervention list from assessment data | Lane 2 — but only cohort-level, never student-level |
| Suggesting which fee accounts to send to Group CFO review | Lane 2, with the exclusion list applied first |

Then, for the three the participant found hardest: a written defence, and the
single control that keeps each in its assigned lane.

**Deliverable:** the twelve classifications, three written defences, three
controls.

---

## Teach B — Audit trails

An audit trail that satisfies an auditor reconstructs a decision. Five elements:

1. **What data** — which export, from which system, on which date, with which
   defects known at the time.
2. **What instruction** — the prompt, versioned. "We asked it to analyse the
   ledger" is not an audit trail.
3. **What output** — retained as produced, before human editing.
4. **What check** — which acceptance check was performed, by whom.
5. **Who approved** — a name and a date, before the output was acted on.

The cheapest implementation that actually works: a dated folder per run holding
the export, the prompt, the raw output, and a one-line approval note. It
requires no system, no budget and no IT involvement — which is why it survives.

---

## Ex 5.2 — The AI Use Standard · 30 min

Write the one page that goes to every campus. Constraints:

- **One page.** Anything longer is not read and therefore does not exist.
- Written for an administrator, not a lawyer.
- Says what is allowed, not only what is forbidden — a standard that only
  prohibits gets ignored the first time someone needs to get work done.
- Names the three things that are never done.
- Says what to do in the first hour after a suspected disclosure (Cl. 9.4).
- Names who to ask when unsure, with an actual role.

Drafted individually, then merged as a cohort into one version. The merge is the
exercise: seeing which rules everyone wrote independently, and which one person
thought of and everyone accepts, is what makes the result feel owned rather than
imposed.

**Deliverable:** the merged one-page standard, ready for the compliance
representative's sign-off.

---

## Ex 5.3 — Peer red-team · 25 min

Exchange capstone designs with a peer who is **not** in your function. Find the
disclosure path they missed.

Trace, specifically:

- What personal data enters.
- Where the **output** lives after it is produced — the most commonly missed
  path, and the one that actually leaks. Cl. 9.2 covers the input; the output is
  usually what gets forwarded.
- Who has access to that location, including who has it by accident.
- What happens to it at year end.
- What a screenshot of it would show.

Findings go back with severity and a proposed design change. **"Be careful" is
not a finding.**

**Deliverable:** a red-team report on a peer's design, and your response to
theirs — including what you accepted and what you disputed.

---

## Ex 5.4 — The real-data gate · 25 min

Prepare the written case to move **one** workflow from synthetic to production
data. This is a real approval document, not an exercise artefact.

| Section | Content |
|---|---|
| Workflow and lane | What it does, which lane, who owns it |
| Data required | The minimum fields. Justify every personal-data field, one line each. |
| Fields deliberately excluded | And what that costs the analysis |
| Legal basis | Purpose, and why this use is compatible with collection |
| Systems | Confirmation that every system used is on the Approved Systems List |
| Controls | Access, retention, deletion, approval before any output is acted on |
| Audit trail | The five elements, and where they are kept |
| Failure plan | What happens in the first hour after a suspected disclosure, and who is called |
| Sign-off | Function head, and Group IT & Compliance |

Reviewed in-session by the compliance representative. **Cases that are not
signed off do not proceed to a real-data capstone** — the participant runs
their capstone on synthetic data instead, which is a legitimate outcome and
should be framed that way rather than as a failure.

---

## Module 5 deliverables

1. Twelve lane classifications with three written defences and three controls
2. The merged one-page AI Use Standard, signed off
3. A peer red-team report, and your response to the one on your work
4. A written real-data case, signed off or explicitly deferred

**Assessment: pass/fail.** All four required. A participant who does not pass
proceeds to Module 6 on synthetic data only.
