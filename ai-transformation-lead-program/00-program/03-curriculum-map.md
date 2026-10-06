# Curriculum Map

**Total:** 24 hours of facilitated time across 6 modules, plus a 30-day
supervised field period before certification.

**Delivery surface:** every exercise in every module is done *inside Claude*.
No spreadsheets to install, no scripts to run, no third-party tooling. The
participant uploads a file from the data pack, works in the conversation, and
produces something they keep.

| # | Module | Hours | Functions in scope | Assessed competencies |
|---|---|---|---|---|
| **1** | **Foundations: the group as workflows** | **5:00** (4:33 instructional) | All five | C1 C2 C3 C4 C5 C6 |
| 2 | HR & Academics: people workflows | 4:00 | HR, Academics | C1 C3 C4 C5 |
| 3 | Accounts & Purchase: numbers you can defend | 4:00 | Accounts, Purchase | C2 C4 C5 C7 |
| 4 | Marketing & Admissions: the funnel and the proof | 4:00 | Marketing | C4 C5 C7 |
| 5 | Governance: privacy, approval, audit | 3:00 | All five | C6 C8 |
| 6 | Build, handover and capstone | 4:00 + field | Participant's choice | C5 C7 C8 |

---

## Module 1 — Foundations: the group as workflows · 5:00

**The module this programme is built around.** Fully specified in
[`../module-01-foundations/`](../module-01-foundations/).

Participants leave with: a scored workflow inventory across all five functions,
a working CRISP prompt they wrote themselves, a normalised vendor comparison, a
funnel analysis that finds a real insight in 2,518 rows, a specification for a
reusable asset, and a personal 30-day commitment.

Eight exercises, all in Claude, all on the synthetic Meridian data pack.

---

## Module 2 — HR & Academics: people workflows · 4:00

**Premise:** HR and Academics are where language work is densest and where
getting it wrong costs the most trust.

- **Teach:** the letter family (offer, appointment, confirmation, promotion,
  transfer, experience) as a single templated system rather than six documents;
  policy-grounded query answering; the deemed-confirmation trap and why date
  arithmetic must be verified, never trusted.
- **Ex 2.1** Build a confirmation-due register from `hr_staff_roster.csv`:
  who is past 11 months, who is inside the 15-day window, who is already
  deemed confirmed. Verify every date by hand for three rows.
- **Ex 2.2** Draft a policy-grounded answer to eight real staff queries with
  clause citations, and identify the two that must be escalated, not answered.
- **Ex 2.3** Turn `academic_assessment_results.csv` into a coordinator's
  intervention list — and find the anomaly that campus-level reporting hides.
- **Ex 2.4** Design the teacher-time audit: what four hours a week are actually
  going on, and which of it is language work.
- **Deliverable:** an HR letter Project with standing policy context, plus an
  escalation rule set.

---

## Module 3 — Accounts & Purchase: numbers you can defend · 4:00

**Premise:** the moment AI output touches money, "it looked right" is not a
standard. This module is about verification discipline.

- **Teach:** why totals must be independently recomputed; reconciling two
  exports that disagree; the difference between an analysis and an assertion;
  writing a comparison that survives an audit committee.
- **Ex 3.1** Full ageing analysis of `accounts_fee_ledger.csv` mapped to the
  seven-stage escalation ladder — including who must *not* receive a reminder.
- **Ex 3.2** Draft the R1 through R4 reminder set, then red-team it against the
  Clause 6 conduct rules.
- **Ex 3.3** Structure `purchase-requests-inbox.txt` into a requisition
  register; flag the post-facto purchase, the single-source case and the
  capex-threshold breach.
- **Ex 3.4** Build the three-quote comparison note for the Purchase Committee,
  with the recommendation, the risks and the dissent.
- **Deliverable:** a fee-ageing asset and a quote-comparison asset, each with a
  built-in verification step.

---

## Module 4 — Marketing & Admissions: the funnel and the proof · 4:00

**Premise:** this is where the group can most easily prove value in rupees, and
most easily fool itself with a vanity metric.

- **Teach:** enquiry-to-admission funnels; cost per lead vs cost per admission
  and why the second is the only one the Board should hear; attribution honesty;
  what a counsellor can actually act on tomorrow morning.
- **Ex 4.1** Rebuild the group funnel across all 14 campuses; produce the CAC
  table and explain the 6× spread between best and worst campus.
- **Ex 4.2** Isolate the follow-up effect and pressure-test it — is it cause,
  or are good leads simply followed up more?
- **Ex 4.3** Draft a counsellor daily worklist that a person with 40 open
  enquiries can act on before 11 a.m.
- **Ex 4.4** Write the Board slide: one chart, three sentences, one ask.
- **Deliverable:** a monthly funnel-review asset, and a baseline for the
  capstone.

---

## Module 5 — Governance: privacy, approval, audit · 3:00

**Premise:** the fastest way to end an AI programme in a school group is one
incident involving a child's data.

- **Teach:** DPDP-shaped obligations in a school context; the Approved Systems
  List; consent and purpose limitation; the Three-Lane model; audit trails that
  reconstruct a decision; what to do in the first hour after a suspected
  disclosure.
- **Ex 5.1** Classify twelve live workflows into Lane 1 / Lane 2 / Never, and
  defend the three you found hardest.
- **Ex 5.2** Write the group's one-page AI Use Standard for campus staff.
- **Ex 5.3** Red-team a colleague's build: find the disclosure path they missed.
- **Ex 5.4** The real-data gate: prepare the written case to move one workflow
  from synthetic to production data.
- **Deliverable:** signed AI Use Standard and an approved real-data case. **This
  module gates access to real group data for the capstone.**

---

## Module 6 — Build, handover and capstone · 4:00 + 30-day field period

**Premise:** the work is not done when it works. It is done when someone else
runs it.

- **Teach:** handover design for low-technical-capacity sites; run-books;
  failure behaviour and the "what do I do when it looks wrong" page; measuring
  the after.
- **In session:** build the capstone asset; write the run-book; rehearse the
  handover with a sceptical stakeholder played by a peer.
- **Field period (30 days):** the asset runs weekly at a real site with a named
  non-Lead owner. The participant collects before/after evidence and logs every
  failure.
- **Certification panel:** 20-minute defence covering the workflow chosen, the
  evidence, the guardrails, and one thing that went wrong and what they did.

---

## Sequencing rules

1. **Module 1 is a prerequisite for everything.** It is not an overview; the
   trust tiers, CRISP structure and Never List introduced there are used
   verbatim in every later module.
2. **Modules 2, 3 and 4 may be taken in any order** and may be split by
   function if a cohort is function-specific. Each is self-contained on the same
   data pack.
3. **Module 5 must precede any use of real data.** No exceptions, including for
   senior participants.
4. **Module 6 requires a sponsor.** A participant without a named function head
   willing to own the capstone workflow is not ready for it.

## Cohort shape

- **6 to 12 participants.** Below 6 the peer red-teaming in Ex 1.8 and Ex 5.3
  loses its value; above 12 the debriefs cannot be run properly.
- Ideally **at least one participant from each of the five functions**, plus the
  Group's IT/compliance representative as an observer in Module 5.
- One facilitator up to 8; two above that.
