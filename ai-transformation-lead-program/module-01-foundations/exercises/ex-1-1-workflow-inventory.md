# Ex 1.1 — Workflow Inventory Across Five Functions

**Time:** 27 minutes (20 build · 7 debrief) · **Mode:** individual build, plenary debrief
**Marks:** 15 · **Competency:** C1 · **Outcome:** LO1 · **Runs at:** 0:38–1:05

---

## The task

Produce a scored, ranked inventory of candidate workflows across all five
Meridian functions, then defend one ranking decision out loud.

You are not looking for AI use cases. You are looking for **workflows** — with
a trigger, a volume, an owner and a failure mode. Whether AI helps is the next
question, not this one.

---

## Setup (2 min)

Start a **new conversation**. Upload:

- [`../../data/group-fact-sheet.md`](../../data/group-fact-sheet.md)

That is the only file you need. This exercise is about structured thinking, not
data.

---

## Step 1 — Generate the candidate list (6 min)

```text
Attached is the fact sheet for Meridian Group of Schools, a 14-campus K-12
group in India. Read it fully, including the Board priorities and the
constraints section.

Act as an operations analyst who has spent a week inside a school group's
Group Office. Your job is to inventory WORKFLOWS, not to propose solutions.

Produce 20 candidate workflows - exactly four from each of the five functions
(HR, Academics, Accounts, Purchase, Marketing & Admissions).

For each workflow give:
- Function
- Workflow name (a verb phrase: what gets done, not a department name)
- Trigger (date-driven / event-driven / message-driven / person-driven)
- Estimated volume per week group-wide, and state the assumption behind your
  estimate in six words or fewer
- Owner (the role whose name is on the output)
- Failure mode: what actually happens when this goes wrong, in one concrete
  sentence - not "errors occur"
- Cycle time today (trigger to done)

Rules:
- Ground every workflow in something the fact sheet actually says. If you are
  inferring, mark the row with (inferred).
- Do NOT mention AI, automation, or tooling anywhere in this output.
- No workflow that appears on this group's Never List (safeguarding,
  admit/reject decisions, hire/fire decisions, salary fixation, contract award,
  legal threats, anything about a named child's health or behaviour).
- Output as a markdown table. No preamble.
```

**Read the output critically before continuing.** Two failure modes to look for:

- Rows that are *departments* rather than workflows ("HR administration").
- Volume estimates with no stated assumption, or assumptions that contradict
  the fact sheet's headcount and campus numbers.

If you see either, say so and ask for a corrected table. Getting this right is
part of the exercise.

---

## Step 2 — Score with VFRR (6 min)

```text
Now score all 20 workflows using this frame. Score each axis 1-5.

V  Volume:     1 = <10/week group-wide, 3 = ~50/week, 5 = >200/week
F  Friction:   1 = runs smoothly today, 3 = slow and inconsistent between
                   campuses, 5 = actively failing, people complain unprompted
R  Risk if wrong: 1 = internal only and easily corrected, 3 = affects a parent
                   or vendor but recoverable, 5 = legal, statutory,
                   safeguarding, or affects a child
Rd Readiness:  1 = data doesn't exist or is on paper, 3 = exports exist but are
                   dirty, 5 = clean export, clear policy, willing owner

Priority = (V + F + Rd) - R

Output a table sorted by Priority descending: Function | Workflow | V | F | R |
Rd | Priority | One-line justification for the LOWEST-scoring axis of that row.

Then answer three questions in under 80 words each:
1. Which workflow has the largest gap between Friction and Priority, and what
   does that gap tell us?
2. Which two workflows would you NOT start with despite a high Priority score,
   and why?
3. Which Board priority from the fact sheet is least served by this top-10, and
   what workflow is missing from the list?
```

Question 1 is the one that matters. A large Friction-to-Priority gap means
**the most painful work is not the work to start with** — usually because it is
high-risk or the data is not ready. Learning to hold that distinction is the
point of this exercise.

---

## Step 3 — Bring it to your own function (6 min)

```text
I actually work in [YOUR FUNCTION] at a school group.

Here is my real week, from an earlier exercise:
[paste your Ex 1.0 Part A table]

Re-score just my three real tasks on the same VFRR frame. Where my description
is too vague to score an axis, say "insufficient information" and tell me the
single question you would need answered - do not guess a score.

Then tell me, in under 100 words, which ONE of my three I should take into the
rest of this programme, and the strongest argument AGAINST that choice.
```

The "strongest argument against" is not decoration. You will be asked for it in
the debrief.

---

## Step 4 — Debrief (7 min, plenary)

Come prepared to answer, in under 60 seconds:

1. Which workflow did you rank first, and what did you have to *deprioritise* to
   put it there?
2. Where did you disagree with the scoring Claude produced, and did you override
   it?
3. What was the strongest argument against your own choice?

> The facilitator will push on question 2. A participant who accepted all 20
> scores without changing one has not done the exercise — they have read an
> output. **The scoring is yours. The output is a draft of your thinking, not a
> replacement for it.**

---

## Deliverable

A single markdown file or document containing:

1. Your final scored table for all 20 Meridian workflows, **with at least two
   scores you changed by hand and a one-line reason for each change.**
2. Your answers to the three questions in Step 2.
3. Your own function's three tasks, re-scored, with your chosen workflow and the
   argument against it.

Name it `ex-1-1-<yoursurname>.md`.

---

## Scored on

See [`../rubrics.md`](../rubrics.md) for the full rubric. In summary:

| | Marks |
|---|---|
| Workflows are genuine workflows (verb phrases, trigger, owner, concrete failure mode) — not departments | 3 |
| Volume estimates carry stated assumptions consistent with the fact sheet | 2 |
| At least two scores independently overridden, with defensible reasons | 4 |
| Correct reading of the Friction-vs-Priority gap | 3 |
| Own-function application, with a real argument against your own choice | 3 |

---

## Stretch (if you finish early)

Ask for the **inverse** list: the five workflows in the group that look most
attractive to change but should be left alone, and why. The best answers here
involve workflows where the friction is the *control* — the slow step is slow
because someone is checking something, and speeding it up removes the check.
