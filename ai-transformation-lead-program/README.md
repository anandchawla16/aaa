# AI Transformation Lead — Training Programme for a School Group

A complete, runnable training programme that turns a school-group manager into
an **AI Transformation Lead**: the person who redesigns workflows across HR,
Academics, Accounts, Purchase, and Marketing & Admissions so that an AI
assistant carries the language work, while a named human keeps the judgement and
the signature.

**Everything runs inside Claude.** No spreadsheets to install, no scripts, no
third-party tooling, no integrations. A participant uploads a file from the data
pack, works in the conversation, and produces something they keep.

---

## What is here

| | |
|---|---|
| **6 modules** | 24 facilitated hours + a 30-day supervised field period |
| **Module 1** | **Fully built — 5:00 elapsed, 4h 33m instructional, 8 scored exercises** |
| **Modules 2–6** | Specified to run-sheet and exercise-brief level |
| **Data pack** | 7 CSVs (3,500+ rows), 3 grounding documents, 1 unstructured inbox — all synthetic, all deliberately defective |
| **Assessment** | Rubrics, a competency model, three award levels, a certification panel |
| **Facilitator materials** | Answer key with figures verified against the data, run sheets, timing recovery, setup checklist |

```
00-program/          Role charter · competency model · curriculum map ·
                     facilitator guide · assessment · setup checklist
module-01-foundations/
   README.md              Run sheet, outcomes, materials
   participant-workbook.md  Six teaching blocks
   exercises/             Ex 1.0 – 1.8, each fully runnable
   rubrics.md             110 marks, banded
   facilitator-answer-key.md   Verified figures. Do not distribute.
modules-02-06/       Outlines for Modules 2–6
data/                The synthetic Meridian Group data pack
tools/gen_data.py    Regenerates the data (fixed seed)
```

---

## Business scope

One fictional school group — **Meridian Group of Schools**, 14 campuses,
~18,400 students, ~1,650 staff — running through every exercise, across all five
functions:

| Function | What participants actually work on |
|---|---|
| **HR** | Appointment letters grounded in policy; probation and confirmation arithmetic; the deemed-confirmation exposure; staff query answering with escalation routing |
| **Academics** | Assessment analysis at cohort level; finding an anomaly that campus-level reporting hides; designing the teacher-time audit |
| **Accounts** | Fee ageing against a seven-stage escalation ladder; who must *not* be chased; drafting reminders that survive the conduct rules |
| **Purchase** | Normalising four non-comparable quotations; structuring a WhatsApp requisition inbox; a committee note that recommends without deciding |
| **Marketing & Admissions** | A funnel across 2,518 enquiries; cost per admission; a 6× spread between campuses; and whether the follow-up effect is causal |

---

## Start here

| You are… | Read |
|---|---|
| **Running the programme** | [`00-program/04-facilitator-guide.md`](00-program/04-facilitator-guide.md) → [`00-program/06-setup-checklist.md`](00-program/06-setup-checklist.md) → [`module-01-foundations/facilitator-answer-key.md`](module-01-foundations/facilitator-answer-key.md) |
| **Attending it** | [`00-program/01-role-charter.md`](00-program/01-role-charter.md) → [`data/group-fact-sheet.md`](data/group-fact-sheet.md) → [`module-01-foundations/participant-workbook.md`](module-01-foundations/participant-workbook.md) |
| **Deciding whether to buy it** | [`00-program/03-curriculum-map.md`](00-program/03-curriculum-map.md) → [`00-program/02-competency-model.md`](00-program/02-competency-model.md) |
| **Adapting it to your group** | [`data/README.md`](data/README.md) and the note at the bottom of this page |

---

## Module 1 at a glance

**5:00 elapsed · 4h 33m instructional · 27m breaks.** A marked four-hour core
path is documented for cohorts that cannot lose a full day.

| Ex | What the participant does | Marks |
|---|---|---|
| 1.0 | Baseline diagnostic — their own week, and eight beliefs, half of which are wrong | — |
| 1.1 | Scores 20 workflows across five functions on Volume, Friction, Risk, Readiness | 15 |
| 1.2 | Sorts 14 tasks into trust tiers, then **makes Claude fail on purpose** and documents it | 10 |
| 1.3 | Rebuilds a bad prompt with CRISP, then hands it to a colleague to run | 15 |
| 1.4 | Answers 11 policy questions twice — ungrounded, then grounded — and measures the gap | 12 |
| 1.5 | Normalises four vendor quotations that are not comparable, and verifies by hand | 18 |
| 1.6 | Finds a decision-grade insight in 2,518 rows, then argues against their own finding | 15 |
| 1.7 | Specifies a reusable asset a campus administrator runs without them | 10 |
| 1.8 | Red-teams their own build, then signs a dated 30-day commitment | 15 |

Pass: **77/110**, with a floor of 8/15 on Ex 1.8.

### The five ideas the module is built on

- **Trust tiers** — T1 read it · T2 spot-check · T3 verify the arithmetic ·
  T4 ground it or don't answer · T0 don't.
- **CRISP** — Context · Role · Inputs and source of truth · Steps and
  refuse-to-guess · Product and acceptance criteria.
- **VFRR** — Priority = (Volume + Friction + Readiness) − Risk. High risk pushes
  work *down* the list; it does not disqualify it.
- **Three Lanes** — Draft · Decide-support · Never.
- **The habit** — *"How would I know if that were wrong?"*

---

## Why the data is broken on purpose

Every file in [`data/`](data/) carries the defects a real ERP export carries:
campus names spelled four ways, source names in mixed case, three date formats,
Indian-format numbers, duplicate rows, a credit balance, an incomplete vendor
quote, and a vendor quoting GST-inclusive rates without an obvious flag.

**None of it is labelled.** Finding it is the exercise. Two consequences are
built into Module 1 and verified in the answer key:

- In Ex 1.5, normalising the GST basis **reverses** the ranking of two vendors.
  A committee acting on the raw quotes picks the wrong one while believing it has
  done a price comparison.
- In Ex 1.6, failing to normalise `Google Ads` / `google ads` overstates cost per
  enquiry on the group's largest channel by **75%** — in a number going to the
  Board.

Both are recoverable in one line of instruction, and invisible without it. That
is the lesson the module exists to deliver.

---

## Safety and governance, built in

- **The Never List** is read aloud in the first two minutes and applied in every
  module: no safeguarding, no admit/reject, no hire/fire, no salary fixation, no
  appraisal ratings, no contract award, no legal threats, nothing about a named
  child's health or behaviour.
- **The synthetic-data rule.** Participants use only the fictional Meridian pack
  until Module 5 is complete and a written real-data case is approved.
- **Ex 1.8 carries a hard floor.** A participant who cannot find the risk in
  their own work does not pass Module 1, whatever their total score.
- **Certification is withheld** — regardless of score — for putting real
  personal data into an unapproved system at any point in the programme.

---

## Verification

Every figure in the facilitator answer key was computed directly from the files
in `data/`, not estimated. To reproduce them:

```bash
python3 tools/gen_data.py      # fixed seed 20260908, byte-identical output
```

If you change the generator, the answer key's numbers change and must be
recomputed.

---

## Adapting this to your own group

The programme is written against a fictional group so that it can be run
immediately, by anyone, without a data-governance conversation first. To adapt
it:

1. **Replace `data/group-fact-sheet.md`** with your own group's profile — the
   campuses, the org structure, the systems, and most importantly your Board's
   actual priorities. Every exercise scores against those priorities.
2. **Replace the two policy documents** with your own HR policy and fee circular.
   Keep the clause-numbered structure; the grounding exercises depend on it.
3. **Keep the synthetic CSVs for Modules 1–4.** Do not substitute real data
   before Module 5 — that sequencing is a deliberate control, not an oversight.
4. **Recompute the answer key** against whatever data you use. The figures are
   exact, and stale numbers in a facilitator's hands are worse than none.
5. **Rewrite the Never List** with your own Board. It must be theirs, not
   inherited from this document, or nobody will enforce it.
