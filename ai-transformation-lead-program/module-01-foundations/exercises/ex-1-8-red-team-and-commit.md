# Ex 1.8 — Red-Team Your Own Work, and Commit

**Time:** 20 minutes (15 build · 5 close) · **Mode:** individual, then pairs
**Marks:** 15 · **Competency:** C6 · **Outcome:** LO8 · **Runs at:** 4:40–5:00

> **This exercise carries a floor.** A participant scoring below 50% here does
> not pass Module 1, whatever their total. The reason is simple: someone who
> cannot find the risk in their own work should not be leading this in a school.

---

## Part A — Lane assignment (4 min)

Take the asset you specified in Ex 1.7. Assign its lane, and be honest about
where it will drift.

```text
Here is an asset specification I have written for a school group:
[paste your Ex 1.7 specification]

The group uses a three-lane model:
- Lane 1 Draft: output is language a human reads, edits and sends under their
  own name.
- Lane 2 Decide-support: output is analysis informing a human decision.
- Lane 3 Never: output would itself constitute or determine a decision about a
  person. Not permitted.

The group's Never List: student safeguarding or discipline; any admit, reject
or withdraw decision; any hire, non-confirm, promote or terminate decision;
salary fixation; appraisal ratings; contract award; legal threats; anything
involving a named child's health, behaviour or family circumstances.

1. Assign this asset to a lane. Justify in two sentences.
2. Now argue the opposite - make the strongest case that it belongs in a
   RISKIER lane than I assigned. What would have to be true?
3. Describe the realistic drift path: how does this asset end up operating in
   a riskier lane 12 months from now, without anyone deciding that it should?
   Be concrete about the week it happens and who is busy.
4. What single control, added now, would prevent that drift? It must be
   something that survives the person who installed it leaving.
```

Question 3 is the one that matters. **Assets do not start in the wrong lane.
They drift, one busy week at a time.** Your answer should name a specific
week — exam week, admission season, an audit, a resignation.

---

## Part B — Four attacks (6 min)

```text
Now attack this asset. I want you adversarial, not balanced. Assume it will be
used by a tired person at 6pm in a school with no technical support.

1. WRONG-BUT-PLAUSIBLE. Construct a specific, realistic scenario where this
   asset produces output that is confidently wrong and the owner does not
   notice. Name the input condition that causes it. Then tell me what in my
   acceptance check would have to change to catch it.

2. DISCLOSURE PATH. Trace every piece of personal data that enters this
   workflow: what enters, where it goes, who can see the output, and where it
   is retained. Name the single most likely way personal data ends up somewhere
   it should not. Check it against this clause of our policy:

   "Employee or student personal data shall not be transferred to, pasted into,
   or processed by any third-party system, tool or service that is not on the
   Approved Systems List." (MGS/HR/POL/07 Cl. 9.2)

3. WORST-CASE SEND. If one output went out unreviewed on a Friday evening, what
   is the single worst message a parent, employee or vendor could receive?
   Write that message. Do not soften it - I need to see the worst case, not a
   polite version of it.

4. THE HOSTILE READING. A parent's advocate, a labour lawyer, or an auditor has
   obtained this output and the prompt that produced it. What is the most
   damaging thing they can say about it? What in the design gives them that
   opening?

For each: severity (high/medium/low), and the specific change that closes it -
a change to the design, not a note telling people to be careful.
```

That last constraint matters. **"Train the users to check" is not a control.**
A control is something in the design that makes the failure harder or louder.

---

## Part C — Peer red-team (5 min)

Swap specifications with a **different** partner from the one in Ex 1.3.

Spend three minutes attacking theirs. Your job is to find **one thing they
missed.** You are not being kind; you are being useful. Then two minutes to
exchange findings.

Record on your own sheet:

| | |
|---|---|
| What my partner found that I missed | |
| Why I missed it | |
| What I changed as a result | |

The middle row is the one to think about. There is usually a pattern in what a
person cannot see about their own work, and knowing your own pattern is worth
more than any checklist.

---

## Part D — Your 30-day commitment (5 min, close)

Write this out and date it. It is the last thing you do today, and it is the
first thing asked for in Module 2.

```text
MY 30-DAY COMMITMENT                    Date: ____________

Name: ______________________  Function: ______________________

THE ONE WORKFLOW
  Workflow: _______________________________________________
  VFRR score: V__ F__ R__ Rd__  Priority: ____  (must be >= 8)
  Lane: [ ] 1 Draft   [ ] 2 Decide-support     (Lane 3 is not eligible)

THE BASELINE - I take this measurement BEFORE I build anything
  What I will measure: ____________________________________
  How I will measure it: __________________________________
  I will have this number by (date): ______________________

THE OWNER - a named person who is not me
  Name and role: __________________________________________
  I have asked them: [ ] not yet   [ ] yes, and they agreed
  I will ask them by (date): ______________________________

THE GUARDRAIL
  The one control that keeps this in its lane: ____________
  _________________________________________________________

WHAT I WILL NOT DO
  _________________________________________________________

I will present the baseline number and the owner's name at the start of
Module 2 on ____________.

Signed: ______________________
```

**Three rules on this commitment:**

1. **One workflow. Not three.** A Lead with three pilots at day 30 has evidence
   for none of them.
2. **The baseline comes before the build.** If you build first, you have lost
   the ability to prove anything, permanently. This is the most common and most
   irreversible mistake in the whole programme.
3. **The owner must have agreed.** Not been informed — agreed. If you cannot
   name someone who said yes, your first 30 days are about finding them, and
   that is a legitimate and useful answer to bring to Module 2.

---

## Deliverable

`ex-1-8-<yoursurname>.md` containing:

1. Lane assignment, the counter-argument, the drift path with a named week, and
   the control that prevents it.
2. All four attacks with severity and a design change for each.
3. Your peer red-team record, including what you missed and why.
4. Your signed, dated commitment.

---

## Scored on

| | Marks |
|---|---|
| Lane correctly assigned, with a genuine counter-argument | 2 |
| Drift path is concrete — names a week, a pressure and a person | 3 |
| Wrong-but-plausible scenario names a specific input condition | 2 |
| Disclosure path traced against Cl. 9.2, with a real leak path named | 3 |
| Worst-case message actually written, not softened | 2 |
| Every control is a design change, not "tell users to be careful" | 2 |
| Commitment complete, with baseline dated **before** any build | 1 |

**Floor: 8/15 required to pass Module 1.**

---

## Close · the six sentences

You should now be able to say all six without looking them up:

1. "Here are the six workflows in my function worth changing, in order — and
   here is why the most painful one is not first."
2. "That is a Tier 4 claim. Where is it grounded?"
3. "This prompt has no refuse-to-guess clause, so I do not know what it made up."
4. "I ran a defect report on the export before I trusted the total."
5. "Who owns this on Monday morning when I am not here?"
6. "That is Lane 3. The answer is no — and here is what we can do instead."

The sixth is the one that makes you a Lead rather than a builder.
