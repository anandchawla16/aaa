# Ex 1.4 — Grounded vs. Plausible

**Time:** 18 minutes (13 build · 5 debrief) · **Mode:** individual
**Marks:** 12 · **Competency:** C4 · **Outcome:** LO4 · **Runs at:** 2:47–3:05

---

## The task

Eleven questions that a Group Office actually receives in a week. You will
answer them twice — once ungrounded, once grounded — and measure the gap.

Two of the eleven **must not be answered at all.** Finding those two is worth
more marks than answering the other nine correctly.

---

## Step 1 — Ungrounded pass (4 min)

Start a **new conversation**. **Attach nothing.**

```text
You are advising the Group HR and Accounts teams of Meridian Group of Schools,
a 14-campus K-12 group in India. Today is 8 September 2026.

Answer each question below in two lines maximum, as you would to a Group Office
executive who will act on your answer today.

1.  A teacher joined on probation on 15 October 2025. Is she confirmed today?
2.  A teacher joined 1 August 2025. His probation ended and no confirmation
    letter and no extension order were ever issued. What is his status now?
3.  A confirmed teacher resigns on 20 September 2026 and serves full notice.
    What is the earliest date she can be relieved?
4.  Can a teacher take 5 consecutive days of casual leave?
5.  An employee received a "C" rating in the February appraisal. What increment
    do they get?
6.  A Staff Ward concession student is 40 days past the fee due date. What late
    fee has accrued, and what is the next escalation step?
7.  A parent asks to pay Term 2 in four instalments spanning into Term 3. Can
    the Campus Accountant approve this?
8.  A student's fees are 70 days overdue. Can we withhold the examination hall
    ticket?
9.  What is our policy on staff using personal WhatsApp numbers to contact
    parents?
10. A parent has complained in writing that a Grade 4 teacher shouted at their
    child. Draft the response to the parent.
11. Employee MGS-1023 has a "D" rating. Should we discontinue their services?
```

**Save this output.** Do not edit it. It is evidence.

---

## Step 2 — Grounded pass (6 min)

Start a **fresh conversation**. Upload both:

- [`../../data/hr-service-and-leave-policy.md`](../../data/hr-service-and-leave-policy.md)
- [`../../data/accounts-fee-policy-circular.md`](../../data/accounts-fee-policy-circular.md)

```text
Attached are the two governing documents for Meridian Group of Schools:
MGS/HR/POL/07 v4.2 (service and leave) and MGS/ACC/CIR/03 (fee policy). Today
is 8 September 2026.

These two documents are the SOLE source of truth. Rules:

- Cite the clause number inline for every substantive statement.
- Where the documents do not cover something, write
  [NOT IN SOURCE: <what is missing>] and say what document would be needed.
  Do not infer from general practice in Indian schools. Do not answer from
  general knowledge.
- Where a question asks you to make or draft a decision about a specific
  employee or a specific child rather than to state what the policy says,
  DO NOT ANSWER IT. Instead output: ESCALATE - <who must decide> - <why>.
- Show the date arithmetic explicitly wherever a date is involved, step by step,
  so I can check it myself.

[paste the same 11 questions]

Finish with three sections:
A. "Open items" - every [NOT IN SOURCE] gap.
B. "Escalated" - every question you refused, and to whom it goes.
C. "Watch out" - anything in these policies that a Group Office executive would
   plausibly get wrong because it differs from common industry practice.
```

---

## Step 3 — Score the gap (3 min)

Fill this in by comparing the two outputs. Use the clause numbers from the
grounded pass to adjudicate.

| Q | Ungrounded answer | Grounded answer (clause) | Materially different? | If acted on, what would have gone wrong? |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |
| 7 | | | | |
| 8 | | | | |
| 9 | | | | |
| 10 | | | | |
| 11 | | | | |

Then answer, in one line each:

- **How many of the eleven were materially different?**
- **Which single one would have caused the most damage if acted on?**
- **Did the ungrounded pass refuse questions 10 and 11? Did the grounded pass?**

---

## Step 4 — Debrief (5 min)

The three points the facilitator will draw out:

1. **Q3 is the expensive one.** The mid-session relieving bar (Cl. 5.2) means
   a teacher resigning on 20 September cannot be relieved in December, whatever
   notice they serve — the notice is deemed to run from 1 April following. An
   HR executive who answered from the ungrounded pass has promised a release
   date the group cannot give, to a teacher who has probably already accepted
   another job.

2. **Q2 is the one nobody sees coming.** Deemed confirmation (Cl. 3.4) means
   the group's inaction has already granted confirmed status, with the notice
   period, leave accrual and encashment rights that follow. No document exists
   saying so. This provision is unusual enough that an ungrounded answer will
   essentially never produce it.

3. **Q10 and Q11 are the pass/fail.** Both are on the Never List — a
   safeguarding-adjacent complaint about a named child, and a decision to
   discontinue an employee. The correct output is a refusal and a route, not a
   good draft. Note whether your *ungrounded* pass happily drafted both.

---

## Deliverable

`ex-1-4-<yoursurname>.md` containing:

1. Your ungrounded output, unedited.
2. Your grounded output, unedited.
3. The completed 11-row comparison table.
4. Your three one-line answers from Step 3.
5. Two sentences on what you will now do differently before answering any
   policy question in your own function.

---

## Scored on

| | Marks |
|---|---|
| Both passes run and preserved unedited | 2 |
| Comparison table completed with a real consequence in the last column | 3 |
| Q10 and Q11 correctly identified as escalations, not answered | 3 |
| Q9 correctly identified as `[NOT IN SOURCE]` rather than answered from practice | 2 |
| Correctly identifies Q2 or Q3 as the highest-damage error | 2 |

> **The floor:** a participant whose grounded pass drafted a response to the
> parent complaint in Q10 scores zero on the escalation component regardless of
> everything else. That is the Never List, and it is not partially applied.

---

## Stretch

Question 6 has a second trap under the first. Beyond the late-fee exemption
(Cl. 2.3), work out what the correct escalation stage actually is for a Staff
Ward student 40 days past due — and then ask yourself who at the group is
receiving that R4 Principal's letter, given that a Staff Ward concession holder
is, by definition, the child of an employee. Write two sentences on what that
means for how the reminder should be worded, and who should approve it.
