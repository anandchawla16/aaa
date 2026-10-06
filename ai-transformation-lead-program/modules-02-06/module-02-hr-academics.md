# Module 2 — HR & Academics: People Workflows

**4:00 elapsed · 3:40 instructional · Prerequisite: Module 1**
**Competencies: C1, C3, C4, C5**

---

## Premise

HR and Academics are where language work is densest and where getting it wrong
costs the most trust. They are also where the group's stated priorities bite:
teacher attrition at 19% against a 13% target, and a commitment to remove four
hours a week of administrative load from teachers.

The module's central discipline: **date arithmetic and policy application must
be verified, never trusted** — because in HR a wrong date is a legal position,
not a typo.

---

## Run sheet

| Start | Min | Type | Block |
|---|---|---|---|
| 0:00 | 15 | D | Commitments review — every participant, 90 seconds |
| 0:15 | 20 | T | **Teach A** — The letter family as one system, not six documents |
| 0:35 | 35 | E | **Ex 2.1** — Confirmation-due register |
| 1:10 | 10 | — | Break |
| 1:20 | 15 | T | **Teach B** — Policy-grounded query answering and escalation routing |
| 1:35 | 35 | E | **Ex 2.2** — Eight staff queries, two of which must not be answered |
| 2:10 | 15 | T | **Teach C** — Reading assessment data without naming a child |
| 2:25 | 35 | E | **Ex 2.3** — The coordinator's intervention list |
| 3:00 | 10 | — | Break |
| 3:10 | 20 | E | **Ex 2.4** — The teacher-time audit design |
| 3:30 | 15 | E | **Ex 2.5** — Build the HR Project |
| 3:45 | 15 | D | Commitment update and close |

---

## Teach A — The letter family

Six letters — offer, appointment, confirmation, promotion, transfer, experience
— are usually treated as six templates maintained separately, which is why they
drift out of alignment with policy at different rates.

They are better understood as **one system with three layers**:

| Layer | Content | Changes |
|---|---|---|
| Policy layer | Probation, leave, notice, appraisal terms | Once a year, centrally |
| Letter-type layer | What this specific letter must establish | Rarely |
| Instance layer | Name, ID, designation, campus, dates, CTC | Every time |

The design consequence: the policy layer is attached once as standing context;
the letter-type layer is a parameter; the instance layer is merged **locally,
after review**, because it is personal data.

**The honest complication:** two of the six do not belong in the same asset.
The experience letter is a statement of fact about past service and carries
different liability; the promotion letter follows a decision that is on the
Never List and must not be drafted before that decision exists. Participants
should reach this themselves in the Ex 2.5 build.

---

## Ex 2.1 — Confirmation-due register · 35 min

**Data:** `hr_staff_roster.csv` (91 rows), `hr-service-and-leave-policy.md`.

Build the register Group HR does not currently have: who is due for
confirmation, who is inside the 15-day window, and **who is already deemed
confirmed under Cl. 3.4** because nobody issued a letter in time.

Sequence:

1. Defect report first. The roster has three date formats, three blank joining
   dates, three blank CTC values, leading/trailing whitespace in names,
   inconsistent campus naming, and one person appearing under two employee IDs.
2. Normalise, then compute against Cl. 3.1 (11 months) and Cl. 3.3 (15 days).
3. **Verify three rows entirely by hand.** No exceptions. Show the arithmetic.
4. Produce the register with a column stating the action and the responsible
   role.
5. Handle the blank joining dates explicitly — they cannot be computed and must
   not be silently dropped.

**The finding that matters:** any employee already deemed confirmed represents
a legal position the group has taken by inaction, with notice period, leave
accrual and encashment consequences, and no document recording it.

**Deliverable:** the register, the hand-verification of three rows, and a
one-paragraph note to the Group HR Head on the deemed-confirmation exposure.

**Rubric weight:** hand-verification 8 of 25 marks. Correct treatment of the
duplicate identity and the blank dates, 6.

---

## Ex 2.2 — Eight staff queries · 35 min

Eight real queries. Six are answerable from policy with citation; **two must be
escalated, not answered.** Participants who answer all eight fail the exercise
regardless of the quality of the six.

Coverage: leave combination rules (Cl. 4.2), EL during session (Cl. 4.4),
notice buy-out (Cl. 5.3), appraisal consequence (Cl. 6.2), relieving
documentation (Cl. 5.4), and one question the policy is silent on — which must
return `[NOT IN SOURCE]`.

The two escalations involve a decision about a specific employee's continued
engagement and a grievance about a named colleague.

**Deliverable:** the eight answers with inline clause citations, the escalation
routing for the two, and the `[NOT IN SOURCE]` gap written as a
recommendation to Group HR for the next policy revision.

---

## Ex 2.3 — The coordinator's intervention list · 35 min

**Data:** `academic_assessment_results.csv` (420 rows).

Produce what a campus coordinator can act on this week: which cohorts are
underperforming relative to attendance, and where the relationship breaks down.

Constraints, stated in the prompt and marked:

- **No student is named.** Work at cohort level — grade, section, subject.
- Every flagged segment states its record count, and segments too small to
  support a conclusion are labelled as questions, not findings.
- No action about any individual teacher is proposed in a circulated document.

The Surat anomaly from Module 1 recurs here at n = 9. The correct handling is
a private question to the campus academic head, not a finding in a report —
and the exercise is marked on whether participants hold that line under the
pressure of having found something interesting.

**Deliverable:** the intervention list, plus one paragraph on what should be
said to whom about the anomaly, and in what setting.

---

## Ex 2.4 — The teacher-time audit · 20 min

Board priority 6 is four hours a week returned to teachers. Nobody knows where
those hours currently go.

Design the audit: what to measure, how to collect it without adding to the load
being measured, what to do about the fact that teachers will report what they
think is wanted, and how to separate language work from everything else.

**Deliverable:** a one-page audit design that a Principal could run next week,
including the specific question wording and the sampling approach.

---

## Ex 2.5 — Build the HR Project · 15 min

Create a Claude Project with `hr-service-and-leave-policy.md` and
`group-fact-sheet.md` as standing context, and the Ex 1.3 letter prompt as its
first saved asset.

Then answer the design question in writing: **which of the six letter types
belong in this asset and which do not, and why.** The expected answer excludes
at least the promotion letter — because it presupposes a Never List decision —
and treats the experience letter separately.

**Deliverable:** the Project, and the written scope decision.

---

## Module 2 deliverables

1. Confirmation-due register with hand-verification and the deemed-confirmation
   note
2. Eight policy answers with citations and two correct escalations
3. Cohort intervention list with no student named and sample sizes stated
4. Teacher-time audit design
5. An HR Project with a written scope decision

**Marks: 100. Pass: 70.** Floor: answering either escalation question in Ex 2.2
caps the module at 60.
