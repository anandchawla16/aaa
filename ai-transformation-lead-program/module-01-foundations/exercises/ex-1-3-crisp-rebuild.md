# Ex 1.3 — CRISP Rebuild: The HR Appointment Letter

**Time:** 25 minutes (19 build · 6 debrief) · **Mode:** individual, then swap
**Marks:** 15 · **Competency:** C3 · **Outcome:** LO3 · **Runs at:** 2:00–2:25

---

## The task

Take a bad prompt. Watch it produce something that looks fine. Rebuild it with
CRISP. Then hand your prompt to a colleague and see whether it survives contact
with someone who is not you.

That last step is the assessment. A prompt only counts as an asset if someone
else can run it.

---

## Setup

Start a **new conversation**. Upload:

- [`../../data/hr-service-and-leave-policy.md`](../../data/hr-service-and-leave-policy.md)
- [`../../data/group-fact-sheet.md`](../../data/group-fact-sheet.md)

---

## Step 1 — Run the bad prompt (3 min)

```text
Write an appointment letter for a teacher joining our school.
```

Read what comes back. It will be a competent, complete-looking letter.

Now audit it against the attached policy. Ask:

```text
Check the letter you just wrote against the attached policy MGS/HR/POL/07 v4.2.
List every statement in your letter that contradicts the policy, is absent from
the policy, or was supplied from general knowledge of Indian school employment
rather than from the attached document. Be exhaustive and be blunt about your
own output.
```

**Write down how many defects it found.** Most participants see somewhere
between four and eight — commonly a wrong probation period, a wrong notice
period, invented leave entitlements, an invented working-hours clause, and no
mention at all of the deemed-confirmation rule or the mid-session relieving bar.

The letter *looked* right. That is the entire lesson of this exercise, and you
now have your own evidence for it.

---

## Step 2 — Rebuild with CRISP (10 min)

Write a full CRISP prompt for the same task. All five elements, explicitly.

Use this scaffold. **Do not just fill in the blanks mechanically** — the marks
are for the judgement in the Steps and Product sections.

```text
CONTEXT
[Which group, how many campuses, which campus this is for, who issues it, who
signs it, what the document becomes legally, who might read it later.]

ROLE AND AUDIENCE
[Who Claude is acting as. Who receives the letter and how carefully they will
read it.]

INPUTS AND SOURCE OF TRUTH
[Which attached files. Which one GOVERNS. What happens when sources conflict -
including when the conflict is with MY OWN instructions.]

Candidate details:
  Name: [CANDIDATE NAME]
  Employee ID: [TO BE ALLOTTED]
  Designation: TGT - Science
  Campus: Pune-Baner
  Date of joining: 1 October 2026
  Employment type: Permanent (on probation)
  Annual CTC: Rs 6,80,000
  Reporting to: Vice Principal, Pune-Baner

STEPS
[The reasoning path. Include a refuse-to-guess clause. Include the instruction
to cite clause numbers inline. Consider: what should happen if a term that
belongs in an appointment letter is simply not covered by the attached policy?]

PRODUCT AND ACCEPTANCE CRITERIA
[Exact shape, length, register, sections. And: how will the HR executive who
receives this CHECK it before sending? Say so explicitly.]
```

Run it. Read the output. Then **iterate at least once** — find one thing that is
still not right and fix the prompt, not the output.

> Fixing the output is the habit to break. If you correct the letter by hand,
> you have solved today's problem. If you correct the prompt, you have solved
> every future instance of it. The whole difference between using AI and leading
> an AI transformation is in that choice.

---

## Step 3 — The handover test (6 min)

Swap prompts with the person next to you. Do not explain yours. Do not answer
questions about it.

Each of you:

1. Open a **fresh conversation**, attach the same two files.
2. Run *their* prompt exactly as written, changing only the candidate name to
   `Priya Nair`.
3. Score what comes back against this checklist:

| Check | Yes / No |
|---|---|
| Is the probation period 11 months, with the 3-month single extension? (Cl. 3.1–3.2) | |
| Is the notice period 90 days for confirmed academic staff? (Cl. 5.1) | |
| Is the mid-session relieving bar mentioned? (Cl. 5.2) | |
| Are leave entitlements correct — CL 8, SL 7, EL 15? (Cl. 4.1) | |
| Are clause numbers cited inline? | |
| Are gaps marked `[NOT IN SOURCE: …]` rather than invented? | |
| Is there an "Open items" list at the end? | |
| Could you send this after a proofread, without rewriting it? | |

4. Give it back with your scores and **one sentence** on the weakest element of
   their prompt.

**A prompt scoring below 6/8 in someone else's hands is not yet an asset**,
however well it worked for its author. That is not a criticism; it is the
standard.

---

## Step 4 — Debrief (6 min)

The facilitator will ask two questions of the room:

1. Whose prompt scored 8/8 in someone else's hands? What did it contain that
   others' did not?
2. What did the refuse-to-guess clause actually catch? (Expect: working hours,
   probation review procedure, transport allowance, retirement age, place-of-
   posting transferability — all things an appointment letter needs and this
   policy extract does not cover.)

Question 2 is the valuable one. **The `[NOT IN SOURCE]` list is a defect report
on your own policy documentation.** Five minutes of prompt work has just told
Group HR which clauses their policy is missing. That output is often worth more
than the letter.

---

## Deliverable

`ex-1-3-<yoursurname>.md` containing:

1. The defect list from Step 1 (how many, and the three most serious).
2. Your final CRISP prompt, in full.
3. The letter it produced.
4. Your colleague's completed 8-point checklist on your prompt, and their
   one-sentence critique.
5. Two sentences: what you changed after the handover test, and why.

---

## Scored on

| | Marks |
|---|---|
| All five CRISP elements present and substantive | 4 |
| Refuse-to-guess clause present, specific, and demonstrably triggered in the output | 3 |
| Source-of-truth precedence stated, including precedence over your own instructions | 2 |
| Acceptance criteria state how the recipient checks the output | 2 |
| Scored ≥ 6/8 on a colleague's handover test | 3 |
| Evidence of iterating the prompt rather than editing the output | 1 |

---

## Stretch

Extend your prompt to handle all six letter types in the group's letter family
(offer, appointment, confirmation, promotion, transfer, experience) by
parameterising the type — without the prompt becoming six prompts glued
together. Ask yourself what is genuinely shared between them and what is not.
This is the design problem you will meet again in Module 2, and the honest
answer is that two of the six do not belong in the same asset.
