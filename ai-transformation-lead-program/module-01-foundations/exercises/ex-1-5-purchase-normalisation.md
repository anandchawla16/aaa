# Ex 1.5 — Purchase: Normalising Four Quotations

**Time:** 28 minutes (22 build · 6 debrief) · **Mode:** individual
**Marks:** 18 · **Competency:** C4, C2 · **Outcome:** LO5 · **Runs at:** 3:05–3:33

---

## The situation

Pune-Baner needs Science Block Phase 2 furniture and equipment by **15 November
2026**. Twelve line items. Four vendors have quoted. The Purchase Committee
meets on Thursday and the Group Purchase Head has asked you for a comparison.

The four quotations are **not comparable as they stand.** They differ in ways
that a quick look does not reveal, and at least one of them looks like the
cheapest bid while not actually being a bid for the same thing.

Your job is to make them comparable, then write the note.

**This is Lane 2 work.** You produce the analysis. The Committee awards the
order. Your note must not tell them who to award to as a conclusion — it tells
them what the numbers say and what the risks are.

---

## Setup

Start a **new conversation**. Upload:

- [`../../data/purchase_requisition.csv`](../../data/purchase_requisition.csv) — what is actually needed
- [`../../data/purchase_vendor_quotations.csv`](../../data/purchase_vendor_quotations.csv) — what four vendors offered

---

## Step 1 — Defect report first. No analysis. (5 min)

Resist the urge to ask for the comparison. Ask for the problems.

```text
Attached are a purchase requisition (12 line items needed by Pune-Baner campus
of Meridian Group of Schools) and four vendor quotations against it.

Do NOT compare the vendors yet. Do NOT recommend anything.

First, produce a data-quality and comparability report. Tell me every reason
these four quotations cannot be compared as they stand. Look specifically for:

- items in the requisition that a vendor has not quoted at all
- quantities quoted that differ from quantities required
- any difference in the basis on which rates are stated
- the same physical item described differently by different vendors, which
  would break a naive match on description
- anything else that would make a straight sum of the quoted amounts
  misleading

For each issue: which vendor, which item codes, how many rows affected, and
what specifically must be done to make the numbers comparable.

Finish by stating the row count of each file and the number of distinct item
codes in each, so I can confirm nothing was dropped.
```

**Check the row counts against the file before you go on.** The quotations file
has 46 data rows and the requisition has 12. If the reply says otherwise,
something was misread and every number after this point is suspect.

There are **four distinct comparability problems** planted in this data. If the
report found fewer than four, ask again, naming the category it missed.

---

## Step 2 — Normalise and compare (7 min)

```text
Good. Now build the comparison, applying the fixes you identified.

Rules for the comparison:
- Price every vendor for the FULL requisition quantity of all 12 items, so the
  totals are like for like.
- Put every rate on the same basis: landed cost including GST.
- Where a vendor has not quoted an item at all, do NOT treat it as zero and do
  NOT silently exclude it. Show that vendor's total for the items they DID
  quote, and separately state which items are missing and what the two missing
  items would cost at the median of the other three vendors' rates.
- Where a vendor quoted a quantity lower than required, price at the required
  quantity at their quoted rate, and flag it.

Output:
(a) A per-vendor summary: comparable landed total for all 12 items, items not
    quoted, quantity shortfalls, delivery days, warranty months, payment terms.
(b) A per-item table: the four vendors' landed unit rates side by side, with
    the lowest highlighted, and a column for the spread between highest and
    lowest as a percentage.
(c) State your arithmetic method in two lines so I can reproduce it.

Show the totals to the rupee. Do not round to lakhs.
```

---

## Step 3 — Verify. Do not skip this. (5 min)

This is Tier 3 work: the reasoning is probably sound, the arithmetic must be
confirmed. Verify **two things by hand**, on paper or a calculator:

**(a) One line item, end to end.** Pick any item code. Find the row in the CSV
yourself. Take the raw `unit_rate_inr`, apply `gst_pct` **only if**
`rate_basis` says exclusive, multiply by the requisition's
`quantity_required`. Does it match the table?

**(b) One vendor total, recomputed a different way.** Ask:

```text
Recompute Sahyadri's comparable landed total a second, independent way: sum the
per-item landed line totals from your per-item table, rather than from your
per-vendor calculation. State both figures and whether they agree exactly. If
they differ by even one rupee, find the cause and tell me which figure is
correct and why.
```

If (a) and (b) both reconcile, you can trust the table. If either does not, you
have just caught an error before it reached a committee — which is a better
outcome for this exercise than a clean run.

Record what you verified and the result. **You get no marks for the comparison
without this record.**

---

## Step 4 — The committee note (5 min)

```text
Now draft the note for the Purchase Committee meeting on Thursday.

Context: Meridian Group of Schools. Requirement is for Pune-Baner Science Block
Phase 2, required by 15 November 2026. Budget head CAPEX-2026-27. Group policy
requires three quotes for capital purchases above Rs 2,00,000, and the award is
made by the Purchase Committee, not by the Purchase Head and not by me.

Write a note of at most 400 words with these sections:
1. What was compared, and what had to be normalised to make it comparable
   (one short paragraph - the Committee must know the raw quotes were not
   like-for-like)
2. Comparable landed totals, as a table
3. Non-price factors that materially affect the decision: delivery against the
   15 November requirement, warranty, payment terms, and completeness of quote
4. Risks and open questions, including any vendor that should be asked to
   requote before being considered
5. Options for the Committee, with the trade-off of each

Constraints:
- Do NOT state a recommendation as a conclusion. Present options and
  trade-offs. The Committee decides.
- Where a fact is not in the attached data, write [NOT IN SOURCE: ...]. Do not
  infer vendor reputation, past performance, or anything not in the files.
- Plain, unhedged business English. No adjectives about the vendors.
```

Read it as if you were the Group CFO. Would you be able to make a decision from
this note without asking a question that the data could have answered?

---

## Step 5 — Debrief (6 min)

The facilitator will ask:

1. **How many comparability problems did your defect report find on the first
   pass?** (There are four.)
2. **Which vendor looked cheapest before normalisation, and were they cheapest
   after?** This is the exercise's punchline.
3. **What did your hand-verification find?**
4. **Did anyone's note recommend a vendor?** If yes — that is Lane drift, in
   the first hour of trying. Notice how natural it felt.

---

## Deliverable

`ex-1-5-<yoursurname>.md` containing:

1. The defect report, and how many of the four issues it caught unprompted.
2. The per-vendor and per-item comparison tables.
3. Your verification record: which line item, the arithmetic you did by hand,
   the second-method total, and whether they reconciled.
4. The Committee note.
5. One sentence: the thing in this data that would most likely have been missed
   if you had simply asked "which vendor is cheapest?".

---

## Scored on

| | Marks |
|---|---|
| Defect report requested **before** any analysis | 2 |
| All four comparability problems identified | 4 |
| Comparison prices all vendors at required quantity on a common GST basis | 3 |
| Incomplete quote handled correctly — neither zeroed nor silently dropped | 2 |
| Hand-verification actually performed and recorded, with the arithmetic shown | 4 |
| Committee note presents options and trade-offs without stating an award | 3 |

---

## Stretch

Test the delivery constraint properly rather than assuming it matters. The
Committee meets Thursday, a purchase order takes about four working days to
issue, and the requirement date is 15 November 2026. Work out, for each vendor,
the actual delivery date implied by their quoted lead time.

Then answer the real question: **does delivery time discriminate between these
four vendors at all?** If it does not, what does that tell you about a note
that uses "faster delivery" to justify paying a premium?

This is a common and subtle failure. When one option is more expensive, it is
easy to reach for a non-price factor to justify it — and easier still when the
factor is real but not actually binding. A good Lead states plainly which
factors separate the options and which do not, *especially* when that removes
the comfortable answer.
