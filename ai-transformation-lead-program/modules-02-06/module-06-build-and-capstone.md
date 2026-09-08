# Module 6 — Build, Handover and Capstone

**4:00 in session + 30-day field period · Prerequisite: Modules 1–5**
**Competencies: C5, C7, C8**

---

## Premise

The work is not done when it works. It is done when **someone else runs it.**

Most AI pilots in school groups die at handover, and they die for a reason that
has nothing to do with technology: nobody agreed to own the thing, so when it
broke, nobody fixed it, and when it stopped running, nobody noticed.

---

## Entry requirements

A participant may not begin Module 6 without:

- Modules 1–5 complete.
- **A named sponsor** — a function head who has agreed, in words, to own the
  capstone workflow after handover. Not been informed. Agreed.
- **A baseline already collected**, dated before any build.
- A Module 5 outcome: either an approved real-data case, or an explicit decision
  to run the capstone on synthetic data.

A participant without a sponsor is not ready. That is not a delay to work
around; finding the sponsor **is** the missing work, and it is the most
predictive thing about whether the capstone survives.

---

## Run sheet

| Start | Min | Type | Block |
|---|---|---|---|
| 0:00 | 20 | D | Capstone proposals — 3 minutes each, sponsor and baseline named |
| 0:20 | 25 | T | **Teach A** — Handover design for low-technical-capacity sites |
| 0:45 | 60 | E | **Ex 6.1** — Build the capstone asset |
| 1:45 | 10 | — | Break |
| 1:55 | 30 | E | **Ex 6.2** — Write the run-book |
| 2:25 | 20 | T | **Teach B** — The handover conversation, and the sentence that kills programmes |
| 2:45 | 40 | E | **Ex 6.3** — Rehearse the handover with a sceptical peer |
| 3:25 | 20 | E | **Ex 6.4** — The measurement plan |
| 3:45 | 15 | D | Field period briefing and close |

---

## Teach A — Handover design

The average Meridian campus has nobody who can maintain a script. Design for
that, not around it.

**Five rules:**

1. **The simplest surface that works.** A saved prompt in a Project beats a
   Skill beats anything custom. Every increment of sophistication is a
   maintenance liability at a site with no maintainer.
2. **No step that requires you.** If any step needs the Lead's judgement, the
   asset is not handed over — it is shared, and it will stop when you are busy.
3. **Fails loudly, not silently.** The worst outcome is not breaking; it is
   producing confident wrong output for four months. Build in something that
   changes visibly when the input changes.
4. **One acceptance check, under two minutes.** Five checks means zero checks.
5. **The run-book is the deliverable, not the prompt.** The prompt is the easy
   part.

---

## Teach B — The handover conversation

Rehearsed because it is the moment most transformation programmes die, and it
dies at one specific sentence.

**"Can't you just run it for me?"**

The answer that fails: *"No, it's your process now."* True, and it ends the
relationship. The owner concludes the Lead has handed them work and left.

The answer that works acknowledges the real question underneath — *what happens
when it breaks and I look stupid?* — and addresses that:

> "I'll run it with you the first three times, and I'm on the phone for the next
> month. What I can't do is be the single point of failure — if I'm the only one
> who can run it, it stops the first week I'm on leave, and then you've lost
> something you'd started relying on. Let's make sure that can't happen to you."

Also rehearsed:

- *"What if it gets something wrong and I've sent it?"* → the acceptance check,
  the approval line, and the fact that they are the reviewer, not the machine.
- *"I don't have time for another system."* → what it replaces, measured, not
  claimed. If it replaces nothing, they are right and the design is wrong.
- *"Is this going to replace my team?"* → answer it directly and honestly. An
  evasive answer here is remembered for years and poisons the next five
  workflows.

---

## Ex 6.1 — Build the capstone asset · 60 min

Build it, on the chosen surface, using everything from Modules 1–5.

Non-negotiables, checked before the session ends:

- [ ] CRISP-structured, with a refuse-to-guess clause
- [ ] Grounded in a named governing document
- [ ] Correct lane, with the control that keeps it there
- [ ] Personal data minimised; every retained field justified
- [ ] One acceptance check, under two minutes
- [ ] Failure behaviour stating what to **do**
- [ ] Named owner who has agreed
- [ ] Audit trail: the five elements, and where they are kept

The facilitator signs each checklist item before the participant proceeds to the
run-book.

---

## Ex 6.2 — The run-book · 30 min

One page. Written for the owner, not for the Lead.

| Section | Content |
|---|---|
| What this does, in one sentence | In the owner's language, not yours |
| When to run it | A specific trigger |
| What you need before you start | The exact export, from where, how |
| How to run it | Numbered steps, no jargon |
| How to check it | The one check |
| What "wrong" looks like | Concrete examples of bad output |
| What to do when it looks wrong | Steps, then who to call |
| What never to do with this | Explicit |
| Who owns this | Name, and cover |

**The test:** hand it to someone from a different function who has never seen
the workflow. If they cannot run it, it is not finished. Do this in the room.

---

## Ex 6.3 — Rehearse the handover · 40 min

In threes: the Lead, the sceptical owner, an observer.

The owner is briefed to be realistically difficult — time-poor, has been through
two failed system rollouts, worried about being blamed, and will ask "can't you
just run it for me?" at some point.

Fifteen minutes each, five minutes of observer feedback. The observer watches
for one thing specifically: **the moment the Lead starts explaining the
technology instead of answering the concern.** It happens in almost every
rehearsal, and naming it is the whole value of the exercise.

---

## Ex 6.4 — The measurement plan · 20 min

| | |
|---|---|
| Metric | The same one as the baseline. Not a better one thought of since. |
| Baseline | The number, and the date it was taken — before the build |
| Method | Identical to the baseline method |
| Collection | When, by whom, how often during the 30 days |
| Confounders | What else changes in this period, and how you will note it |
| Counterfactual | What would have happened anyway, and how you will estimate it |
| Failure log | How every failure gets recorded, including near-misses |

---

## The field period · 30 days

The asset runs weekly at a real site, owned by a named person who is not the
participant.

**Submitted:**

1. Baseline, with its date, taken before the build
2. The asset as deployed, plus every change made during the 30 days and why
3. Usage log: date, who ran it, output, whether the check was performed
4. **Failure log** — every time output was wrong, unusable, or not run
5. After measurement, same metric, same method
6. Owner's statement, half a page, in their words

> **A submission with an empty failure log is returned.** In thirty days of real
> use at a school, something goes wrong. An empty log means the participant was
> not looking, was not told, or is not reporting — and each of those is more
> serious than the failures would have been.

**Facilitator contact:** once at day 7, once at day 21. Both short. The day 7
call is the one that matters — it catches the workflows that never actually
started, which is most of the ones that fail.

---

## Certification panel · 20 minutes

| Section | Min |
|---|---|
| The workflow and why it was chosen — including what was deprioritised | 4 |
| The build and the guardrails | 5 |
| The evidence | 5 |
| **What went wrong** | 4 |
| Panel questions | 2 |

The five questions always asked:

1. "What does the owner do when the output looks wrong and you are unreachable?"
2. "Show me the baseline. When was it taken, relative to the build?"
3. "What in this workflow could still cause harm, and what stops it?"
4. **"What did you refuse to build, and who asked for it?"**
5. "If you left tomorrow, does this survive?"

Question 4 separates a Lead from a builder. A candidate who has never refused
anything has not been doing the job.

---

## After certification

The Lead's next thirty days are not a bigger build. They are:

- **Hand over one more workflow** from their own portfolio to someone else.
- **Re-score their function's inventory** with the function head, not alone.
- **Train one person** in the function to write a CRISP prompt.

The measure of the role is how much runs without the Lead. A Lead who has become
indispensable has failed, however much value they have created — because the
value stops the day they change jobs, and in a school group, they will.
