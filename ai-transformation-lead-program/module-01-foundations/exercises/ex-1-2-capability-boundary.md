# Ex 1.2 — Capability Sort and Make-It-Fail

**Time:** 18 minutes (13 build · 5 debrief) · **Mode:** individual, then pairs
**Marks:** 10 · **Competency:** C2 · **Outcome:** LO2 · **Runs at:** 1:27–1:45

---

## The task

Two halves. First, sort real school-group tasks into the four trust tiers.
Second — and this is the half that teaches — **make Claude fail on purpose, on
a task you chose, and document exactly how the failure looked.**

The second half matters because a failure you have personally produced is
something you will remember at the moment it counts. A warning you have read is
not.

---

## Part A — The sort (6 min)

Start a **new conversation**. No files needed.

```text
I am training AI Transformation Leads for a 14-campus school group in India. We
classify work into four trust tiers:

T1 Language transformation - rewrite, summarise, translate, reformat, change
   tone, extract structure from text I supplied. Trust: high, read the output.
T2 Structured extraction and normalisation - pull fields from messy text,
   reconcile naming variants, classify into my categories. Trust: high on
   schema, spot-check rows.
T3 Analysis over data I supplied - totals, groupings, rates, comparisons,
   rankings. Trust: medium, arithmetic and joins must be independently
   confirmed.
T4 Facts about my institution - our policy, our dates, our approval limits, our
   fee slabs, our history. Trust: zero from memory. Must be grounded in an
   attached document.
T0 Judgement and authority - who to hire, who to admit, who gets a contract,
   what a parent is told about their child. Not a capability question.

Classify each task below into exactly one tier. For each: the tier, a
one-sentence reason, and - this is the important column - THE SPECIFIC CHECK a
school administrator should perform before acting on the output.

1.  Rewrite a fee reminder so it is firmer but still courteous.
2.  Tell me the notice period for a confirmed teacher at our group.
3.  Total the outstanding fee balance in an attached ledger of 142 rows.
4.  Pull structured requisitions out of 20 WhatsApp messages about purchases.
5.  Decide which of four vendors should get the furniture order.
6.  Translate a parent circular into Marathi.
7.  Rank our 14 campuses by cost per admission from attached spend and CRM data.
8.  Tell me whether a teacher on probation since last May is now confirmed.
9.  Summarise 60 open-ended staff survey responses into themes.
10. Draft an appointment letter using our attached policy document.
11. Tell me what the RTE reimbursement rate is in Maharashtra this year.
12. Identify which counsellors have the most stale enquiries in an attached CRM
    export.
13. Decide whether to extend a probation or discontinue an employee.
14. Reconcile campus names between two exports that spell them differently.

Output as a table. Be decisive - no "it depends" without saying what it depends
on. Where a task looks like one tier but is really another, say so explicitly.
```

**Then check yourself.** Before you read on: which of the 14 did you personally
misjudge? Items 8 and 11 catch most people. Item 8 *looks* like arithmetic (T3)
but the arithmetic is worthless without the eleven-month probation rule and the
deemed-confirmation clause — it is T4 wearing a T3 costume. Item 11 looks like
a simple fact but it is an external, time-varying, jurisdiction-specific figure
— which is T4's cousin and equally ungroundable from memory.

---

## Part B — Make it fail (7 min)

Pick **one** T4 task from the list — ideally item 2, 8 or 11.

**Step 1.** Ask it cold, with nothing attached:

```text
What is the notice period for a confirmed academic staff member at Meridian
Group of Schools? Answer in one line, as you would to an HR executive who
needs to act on it today.
```

**Step 2.** Record the answer verbatim. Note three things about *how it reads*:

- Is it confident?
- Is it specific (a number, not a hedge)?
- Would you have questioned it if you did not already know it was ungrounded?

**Step 3.** Now attach
[`../../data/hr-service-and-leave-policy.md`](../../data/hr-service-and-leave-policy.md)
and ask again:

```text
Attached is MGS/HR/POL/07 v4.2, the governing service and leave policy for
Meridian Group of Schools. It is the sole source of truth.

Answer again: what is the notice period for a confirmed academic staff member?
Cite the clause. Then tell me anything else in this policy that affects when
that person can actually be relieved - I want to know what I would have missed
if I had trusted your previous answer.
```

**Step 4.** Compare. Write down, in your own words:

| | |
|---|---|
| The ungrounded answer said | |
| The policy actually says (with clause) | |
| The thing I would have completely missed | |
| Would I have caught this in a real workday? | |

The third row is the one that lands. Most people's ungrounded answer will land
somewhere near a plausible notice period. Almost nobody's will include
**Clause 5.2**, the mid-session relieving bar, which is the provision that
would actually have caused the problem — an HR executive who acted on the
ungrounded answer would have promised a teacher a release date the group cannot
legally give.

---

## Part C — Pair check (5 min, debrief)

Turn to the person next to you. Ninety seconds each:

1. Show them your Step 2 answer and your Step 4 table.
2. Ask them: *"Would you have caught this?"*
3. Agree on one sentence: **the check we will each perform, from now on, before
   trusting any statement about our own institution.**

Write that sentence at the top of your notes. It is the single most useful
output of this exercise.

---

## Deliverable

`ex-1-2-<yoursurname>.md` containing:

1. Your completed 14-row tier table, with any item you initially got wrong
   marked and corrected.
2. Your Part B record: the ungrounded answer verbatim, the grounded answer with
   clause, and the four-row comparison table.
3. The one-sentence check you agreed with your pair.

---

## Scored on

| | Marks |
|---|---|
| Tier assignments correct, with items 8 and 11 correctly identified as T4 | 3 |
| The "specific check" column is genuinely actionable, not generic | 2 |
| Failure documented verbatim, with an honest answer on whether you would have caught it | 3 |
| Identified Clause 5.2 (or equivalent) as the missed provision | 2 |

---

## Stretch

Try to produce a **T3 failure**: give Claude a small table where the correct
total requires noticing something (a duplicate row, a credit balance, a
different unit) and see whether the total comes back wrong. Then work out what
you would have had to already know in order to catch it. That question — *what
did I need to know to catch this?* — is the whole of verification discipline.
