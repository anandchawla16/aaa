# Ex 1.7 — Reusable Asset Specification

**Time:** 15 minutes (11 build · 4 debrief) · **Mode:** individual
**Marks:** 10 · **Competency:** C5 · **Outcome:** LO7 · **Runs at:** 4:15–4:30

---

## The task

Take one thing you built today and specify it as an asset that **someone who is
not you** runs every week, without asking you anything.

The test is not whether it works. You already know it works — you ran it two
hours ago. The test is whether it survives being handed to a campus
administrator on a Monday morning in November when you are on leave.

---

## Choose one

Pick the piece of work from today that your own function would actually use:

| From | Asset it becomes | Likely owner |
|---|---|---|
| Ex 1.3 | Appointment letter drafter | HR Executive, Group Office |
| Ex 1.4 | Policy query responder with escalation routing | HR Executive / Campus Accountant |
| Ex 1.5 | Three-quote comparison note builder | Purchase Officer |
| Ex 1.6 | Monthly funnel and cost-per-admission review | Regional Marketing Manager |

Pick the one closest to your real job. You will carry it into Module 6.

---

## Step 1 — Choose the surface (2 min)

| Surface | Use when | Effort |
|---|---|---|
| **Saved prompt** | One repeated task, one input, one output | Lowest |
| **Project with standing context** | A whole function's work sharing the same background documents | Low |
| **Skill** | A repeatable procedure with rules, templates and a defined output shape, used across many tasks | Medium |
| **Artifact** | Something people look at or work from — a checklist, a worklist, a review page | Medium |

**Choose the lowest-effort surface that survives handover.** Most first builds
are a saved prompt inside a Project. If you are reaching for the most capable
option, ask what specifically fails with the simpler one.

Write down: the surface, and the one-sentence reason a simpler one would not do.

---

## Step 2 — Draft the specification (6 min)

```text
I am specifying a reusable asset for Meridian Group of Schools so that a
non-technical colleague can run it weekly without me.

The asset: [describe in one sentence]
The surface: [saved prompt / Project / Skill / artifact]
The prompt I built earlier today:
[paste your prompt from Ex 1.3 / 1.4 / 1.5 / 1.6]

Turn this into a specification with exactly these six sections:

1. TRIGGER - when it runs, and what starts it. Be specific: a date, an export
   landing, an event. "As needed" is not a trigger.
2. OWNER - the named role who runs it and whose name is on the output. Also:
   who covers when that person is on leave.
3. INPUTS - the exact file, from which system, exported how, with what columns.
   Include what the owner should check about the input BEFORE running anything.
4. STEPS - the prompt itself, cleaned up for someone who was not in the room
   when it was written.
5. OUTPUT AND ACCEPTANCE CHECK - what is produced, and the ONE check the owner
   performs before acting on it. One check, not five - it must be something a
   busy person will actually do.
6. FAILURE BEHAVIOUR - what the owner does when the output looks wrong, what
   they must never do, and who they contact.

Then critique your own specification: what are the three most likely reasons
this asset is abandoned within two months? Be specific to a school group with
low technical capacity at campuses - not generic change-management points.
```

---

## Step 3 — The Monday morning test (3 min)

Read your specification back and answer these five questions honestly. Any
"no" is a defect to fix now, not later.

| | Yes / No |
|---|---|
| Could a campus administrator who has never met me run this from the spec alone? | |
| Does the spec name a **person's role**, not "the team"? | |
| Is the acceptance check something a busy person does in under two minutes? | |
| Does the failure behaviour say what to do, not just who to call? | |
| If the export format changes next term, would the owner notice before acting on a wrong output? | |

That last question is the one that kills assets. Exports change silently. An
asset with no way to notice will keep producing confident, wrong output for
months.

---

## Step 4 — Debrief (4 min)

1. Who chose a surface **simpler** than they first reached for? What made you
   downgrade?
2. Read out your failure behaviour section. The facilitator will pressure-test
   one or two: *"It's Monday, the output looks odd, the owner is busy, you are
   unreachable. What does the spec tell them to do?"*
3. What was your top reason for abandonment? Compare around the room — the most
   common honest answer is "the owner never actually agreed to own it."

---

## Deliverable

`ex-1-7-<yoursurname>.md` containing:

1. Surface chosen, with the reason a simpler one would not do.
2. The full six-section specification.
3. The completed Monday morning test, with any "no" and how you fixed it.
4. Your three abandonment risks.

---

## Scored on

| | Marks |
|---|---|
| All six sections present and specific | 3 |
| Trigger is concrete; owner is a named role with cover identified | 2 |
| Acceptance check is a single, genuinely doable check | 2 |
| Failure behaviour says what to do, including what must never be done | 2 |
| Abandonment risks are specific to a school group, not generic | 1 |

---

## Stretch

Write the **handover conversation** as a script: eight lines, you and the owner.
Include the moment where they say "can't you just run it for me?" — and your
answer. Most transformation programmes die at that exact sentence, and the
answer that works is not "no".
