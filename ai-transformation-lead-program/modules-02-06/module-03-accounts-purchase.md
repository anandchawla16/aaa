# Module 3 — Accounts & Purchase: Numbers You Can Defend

**4:00 elapsed · 3:40 instructional · Prerequisite: Module 1**
**Competencies: C2, C4, C5, C7**

---

## Premise

The moment AI output touches money, "it looked right" stops being a standard.
This module is about **verification discipline** and about writing analysis that
survives an audit committee rather than merely persuading one.

Two Board priorities are in scope: cutting overdue fee balance by 40%, and
raising three-quote compliance from 61%.

---

## Run sheet

| Start | Min | Type | Block |
|---|---|---|---|
| 0:00 | 15 | D | Commitments review |
| 0:15 | 20 | T | **Teach A** — Verification: recomputing, reconciling, and what "checked" means |
| 0:35 | 40 | E | **Ex 3.1** — Fee ageing mapped to the escalation ladder |
| 1:15 | 10 | — | Break |
| 1:25 | 15 | T | **Teach B** — Writing to a parent about money |
| 1:40 | 35 | E | **Ex 3.2** — Draft R1–R4, then red-team against Clause 6 |
| 2:15 | 15 | T | **Teach C** — Structuring the unstructured; the audit view of intake |
| 2:30 | 35 | E | **Ex 3.3** — The requisition register from a WhatsApp inbox |
| 3:05 | 10 | — | Break |
| 3:15 | 30 | E | **Ex 3.4** — The Purchase Committee note, done properly |
| 3:45 | 15 | D | Commitment update and close |

---

## Teach A — What "checked" means

Three levels, and only the third counts for money:

| Level | What it is | Worth |
|---|---|---|
| **Read** | You looked at the output and it seemed reasonable | Nothing, for numbers |
| **Spot-checked** | You verified a row or two against the source | Catches gross errors |
| **Reconciled** | You recomputed a headline figure by a **different route** and the two agree | The only one that catches a systematic error |

The distinction matters because the errors that reach a Board are never random
— they are systematic. A wrong GST basis, a failed join, a dropped category.
Spot-checking a row will not find any of them, because every individual row is
correct. Only recomputing by a different route will.

**The standing rule for this module:** any number that goes to the CFO has been
reconciled, and the participant can say how.

---

## Ex 3.1 — Fee ageing and the escalation ladder · 40 min

**Data:** `accounts_fee_ledger.csv` (142 rows), `accounts-fee-policy-circular.md`.

1. Defect report first. Present: one exact duplicate row, one negative
   (credit) balance, mixed number formats, inconsistent campus naming, 17 RTE
   rows with zero due.
2. Ageing analysis against the **invoice due date**, not the standard term date
   — Cl. 1.2 says the staggered date on the invoice governs.
3. Map every outstanding account to its correct escalation stage R1–R7.
4. **Produce the exclusion list**: who must *not* receive a reminder, and why.
   RTE and Staff Ward accounts are late-fee exempt (Cl. 2.3); accounts with a
   recorded dispute in `remarks` are exempt; accounts on an approved instalment
   plan are exempt; the credit-balance account is not a debtor at all.
5. Compute accrued late fee correctly: ₹50/day after the 15-day grace, capped
   at ₹3,000, and zero for the exempt categories.
6. **Reconcile the total two ways** — by campus and by ageing bucket.

**The exclusion list is the marked deliverable.** Getting the total right is
routine; knowing who must not be chased is the professional judgement, and it
is where a real collection process causes real harm.

**Deliverable:** ageing table, stage mapping, exclusion list with reasons and
clause references, and the two-way reconciliation.

---

## Ex 3.2 — Draft R1–R4, then attack them · 35 min

Draft the four reminder stages for one exemplar account. Then red-team all four
against the Clause 6 conduct rules — which exist because they have been
breached before:

| Rule | Cl. |
|---|---|
| Parent or guardian on record only; never the student | 6.1 |
| Never exclude a child from class, meals, transport or activity | 6.2 |
| Never display, read out or circulate defaulter names | 6.3 |
| No threat of any action not in the ladder; no stage skipped | 6.4 |
| A named human approves every outbound message | 6.5 |
| Courteous at every stage, including R6 and R7 | 6.6 |

Then the harder half: **write the version that breaches Clause 6 without
obviously breaching it.** A message that mentions the child will "not be able to
join the trip", or that copies the class teacher, or that says "as discussed
with others in your class group". Participants must be able to recognise a
breach that is written politely, because that is the form real breaches take.

**Deliverable:** four drafts, a red-team log, and three examples of polite
breaches with the clause each violates.

---

## Ex 3.3 — The requisition register · 35 min

**Data:** `purchase-requests-inbox.txt`.

Turn WhatsApp forwards and email fragments — partly in Hinglish, with missing
budget heads and missing approvals — into a structured requisition register.

Extract per request: campus, requester, item, quantity, required-by date, budget
head, approval status, and **what is missing**.

Then flag the compliance issues that are actually present in the file:

| Issue | Where |
|---|---|
| Purchase already made without approval, regularisation requested | Ahmedabad-Bopal, 60 desk-bench units |
| Single-source purchase needing a documented justification | Bengaluru-Whitefield, IB PYP kits |
| Capex threshold question raised but unresolved | Surat, 4 × UPS |
| Scope creep after submission | Powai, panels 2 → 6 |
| Incomplete request — referenced list never attached | Thane, library books |
| Repeat-vendor engagement with no comparison | Andheri AC, Vadodara stationery |
| Statutory deadline that overrides normal lead times | Indore, fire NOC extinguishers |

**Deliverable:** the register, the flagged-issues table with recommended
handling, and a two-sentence recommendation on what intake form would have
prevented most of these. The second part matters more than the first — the
lesson is that **structuring the intake removes the problem at source**, and no
amount of downstream cleverness does.

---

## Ex 3.4 — The Purchase Committee note · 30 min

The full version of Module 1's Ex 1.5, now with the requisition register as
context and Clause-level procurement rules applied.

New requirements beyond Ex 1.5:

- The three-quote compliance position stated explicitly.
- Bluewave handled correctly — flagged for **requote**, not disqualified.
- The delivery analysis done properly, establishing that delivery does **not**
  discriminate between these vendors, and therefore cannot justify a premium.
- A written dissent section: the strongest case for the option you did not
  favour.
- Still Lane 2: **options and trade-offs, never an award.**

**Deliverable:** the committee note, and a one-paragraph reflection on what
changed between the Module 1 version and this one.

---

## Module 3 deliverables

1. Fee ageing with stage mapping, exclusion list, and two-way reconciliation
2. Four reminder drafts, red-team log, three polite-breach examples
3. Requisition register with flagged compliance issues and an intake
   recommendation
4. Purchase Committee note with dissent

**Marks: 100. Pass: 70.** Floor: a submission with no reconciliation evidence
caps at 60, whatever the arithmetic.
