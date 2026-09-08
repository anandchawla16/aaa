# Ex 1.6 — An Insight in 2,518 Rows

**Time:** 25 minutes (19 build · 6 debrief) · **Mode:** individual
**Marks:** 15 · **Competency:** C4, C7 · **Outcome:** LO6 · **Runs at:** 3:40–4:05

---

## The situation

Board priority 4: *"Marketing spend rose 34% year on year while admissions rose
9%. The Board wants the gap explained and closed."*

You have the CRM enquiry export (2,518 rows, May–August 2026, all 14 campuses)
and the channel spend file. The Group Marketing Head has fifteen minutes on
next week's Board agenda.

Nobody in this group has ever read all 2,518 rows. This is the first exercise
today where the data is genuinely beyond human inspection — which is exactly the
condition under which a wrong answer is hardest to catch.

---

## Setup

Start a **new conversation**. Upload:

- [`../../data/marketing_admission_enquiries.csv`](../../data/marketing_admission_enquiries.csv)
- [`../../data/marketing_channel_spend.csv`](../../data/marketing_channel_spend.csv)

---

## Step 1 — Defect report first (4 min)

```text
Attached are two files from Meridian Group of Schools: an admission enquiry
export from the CRM (May-August 2026, 14 campuses) and a marketing channel
spend file for the same period.

Do NOT analyse anything yet.

Produce a data-quality report covering both files. I specifically need to know
every problem that would corrupt a GROUP-BY or a JOIN between these two files.
Check at minimum:

- categorical values that refer to the same thing but are spelled or cased
  differently, in EVERY text column of BOTH files
- blank or malformed values, with counts
- whether the campus values in the two files match exactly, and if not, exactly
  which values differ and how many rows each affects
- duplicates
- anything that would make a per-campus or per-channel total wrong

For each issue: the column, the variants found, the row count affected, and the
specific normalisation needed.

Then state the exact row count of each file and the number of distinct campuses
in each. Nothing else.
```

**Two things to check before continuing:**

1. Did it find the campus-name variants in **both** files? The spend file uses
   canonical names; the CRM export does not.
2. Did it find the **case inconsistency in the `source` column**? `Google Ads`
   and `google ads` are the same channel. If you group by the raw column, your
   two largest paid channels each split into two, and every cost-per-lead number
   you produce is roughly double what it should be.

If either was missed, name it and ask for a corrected report. **The rest of this
exercise is worthless without this step**, and that is the lesson.

---

## Step 2 — The funnel (5 min)

```text
Now apply the normalisations you identified - campus names and source names
both - and build the analysis. State the normalisation mapping you applied
before the tables.

Produce:

(a) Group funnel: count and percentage at each status (New, Contacted, Visit
    Scheduled, Visited, Application Started, Admitted, Lost, Not Reachable).
    Give the overall enquiry-to-admission conversion rate.

(b) Per-campus table, 14 rows: total enquiries, admitted, conversion %, total
    spend, cost per enquiry, and cost per admission. Sort by cost per
    admission, worst first.

(c) Per-channel table: enquiries, admissions, conversion %, and - only for
    channels that have spend attributed to them - cost per enquiry and cost per
    admission. Say explicitly which channels have no spend line and are
    therefore not costed.

Rules:
- Rows with a blank enquiry_date: include them in status counts, exclude them
  from any month-based cut, and tell me how many rows that affects and where.
- State every assumption you make about attribution.
- Show totals so I can check them: total enquiries, total admissions, total
  spend.
```

**Verify before you read further.** Total spend should reconcile to the sum of
the spend file. Per-campus enquiry counts must sum to 2,518. If they sum to
less, rows were silently dropped by a failed join — the most common and most
invisible error in this kind of work.

---

## Step 3 — Find the driver (5 min)

The per-campus table will show a large spread in cost per admission. Now find
out *why*, rather than reporting *that*.

```text
The cost-per-admission spread across campuses is large. I need the cause, not
the observation.

1. Compare the best three and worst three campuses on cost per admission. For
   each group, give the source mix (share of enquiries by channel), the average
   followup_count, and the share of enquiries ending in "Not Reachable" or
   "Lost".

2. Then test this specifically: group ALL 2,518 enquiries by followup_count
   (0, 1, 2, 3, 4, 5, 6) and give the admission rate for each bucket, with the
   number of enquiries in each bucket.

3. Then challenge your own finding. Give me the strongest argument that
   follow-up count is NOT the cause of the difference - including whether
   better leads might simply attract more follow-up, and what in this dataset
   would let me distinguish the two explanations. Be specific about what data
   we do not have.

4. State what we CAN and CANNOT conclude from this data, in two short lists.
```

Step 3.3 is the part that separates an analyst from a reporter. **The
correlation in this data is real and strong. Whether it is causal is not
something this dataset can settle**, and a Lead who presents it as settled will
be corrected in front of the Board.

---

## Step 4 — The Board slide (5 min)

```text
Draft the Board read-out. Meridian Group of Schools, Board of Trustees, next
week. The Group Marketing Head has 15 minutes and this is one slide of it.

Constraints:
- One headline finding, stated as a number.
- Three supporting sentences maximum.
- One table, at most six rows.
- One recommended action, framed as a decision the Board must take, with what
  it would cost and what it is expected to return.
- One line stating the main caveat on the analysis, in plain words. Do not bury
  it and do not omit it.
- Total under 200 words. No adjectives. No "leverage", "optimise" or "synergy".

Then, separately, list the three questions a sceptical CFO will ask about this
slide, and the honest answer to each - including where the honest answer is
"we don't know from this data".
```

---

## Step 5 — Academic spot-check (optional, 3 min)

*Cut this if running late.*

In a **new conversation**, upload
[`../../data/academic_assessment_results.csv`](../../data/academic_assessment_results.csv):

```text
420 assessment records from Meridian Group of Schools: marks, attendance,
campus, grade, subject, teacher.

Marks generally track attendance across this dataset. Find every place where
that relationship does NOT hold. Segment by campus first, then by teacher
within campus.

For anything you flag: state the segment, the number of records it is based on,
what makes it anomalous in numbers, and - importantly - whether the sample is
large enough to support a conclusion. If it is not, say so plainly and say what
you would need.

Do not name any student. Do not suggest any action about any individual.
```

There is one clear anomaly. **Note the record count behind it before you form a
view.** The correct professional answer includes the phrase "this is based on
a small number of records and is a question to ask, not a finding to report" —
and a participant who states it as a finding has learned the wrong lesson from
an exercise designed to teach the right one.

---

## Step 6 — Debrief (6 min)

1. Who found the `source` casing problem **in Step 1**, before it corrupted
   anything? Who found it later, and how did you notice?
2. What is the spread between the best and worst campus on cost per admission?
   Compare answers around the room — **if numbers differ, one of you dropped
   rows in a join.**
3. What was the follow-up effect? Did anyone present it as causal?
4. What is the honest caveat on the Board slide?

---

## Deliverable

`ex-1-6-<yoursurname>.md` containing:

1. The defect report, and whether it caught the campus and source problems
   unprompted.
2. Your normalisation mapping.
3. The three funnel tables, with reconciling totals.
4. The follow-up bucket table and the counter-argument from Step 3.3.
5. The Board slide and the three CFO questions with honest answers.
6. If done: the academic anomaly, with its record count and your judgement on
   whether it is reportable.

---

## Scored on

| | Marks |
|---|---|
| Defect report run first; campus **and** source variants both caught | 4 |
| Enquiry counts reconcile to 2,518; spend reconciles to the file total | 3 |
| Per-campus cost-per-admission table correct and correctly sorted | 2 |
| Follow-up effect quantified with bucket sizes shown | 2 |
| Counter-argument to causality is substantive and names the missing data | 3 |
| Board slide states the caveat plainly rather than burying it | 1 |

---

## Stretch

Cost per admission is not the right metric for a Board making a capital
allocation decision, and a good Lead says so. Two campuses are at capacity — the
fact sheet says three campuses are full and five are the binding constraint on
fill rate. Work out what happens to your recommendation when you exclude
at-capacity campuses from the spend-reallocation logic, and write the two
sentences that would prevent the Board from moving budget into a campus that has
no seats to sell.
