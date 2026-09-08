# Module 1 — Facilitator Answer Key

**Do not distribute to participants.**

Every figure below was computed directly from the files in
[`../data/`](../data/). If you regenerate the data with a different seed, these
numbers change and this key must be recomputed.

---

# Ex 1.1 — Workflow inventory

There is no single correct inventory. Score the **reasoning**, not the list.

### What a strong submission looks like

- Workflows are verb phrases with a trigger, an owner and a concrete failure
  mode. "Fee follow-up across seven escalation stages" is a workflow. "Accounts
  administration" is a department.
- Volume estimates carry an assumption that is consistent with the fact sheet
  (14 campuses, ~18,400 students, ~1,650 staff, 6 HR staff at Group).
- **At least two scores overridden by hand.** This is the marked behaviour.

### Expected top of the ranked list

Roughly, in most cohorts: fee reminder drafting (R1–R3), HR letter generation,
purchase requisition intake from WhatsApp, admission enquiry follow-up
prioritisation, three-quote comparison. All are high volume, high friction,
recoverable risk, and have an export that exists.

### The Friction-vs-Priority gap — the teaching point

Look for a workflow with **F = 5 and a low Priority**. Safeguarding-adjacent
correspondence and disciplinary documentation are the usual ones: genuinely
the most painful work in the group, correctly at the bottom, because R = 5 and
readiness is low. Some are on the Never List and should not have been listed
at all.

> **Say this out loud in the debrief:** *"The most painful workflow in your
> function is often the one you must not start with. If your first build fails,
> you do not get a second. Pick the boring one with good data."*

### Common failures

| Failure | Response |
|---|---|
| All 20 rows accepted without a single score changed | "Whose inventory is this? You have read an output, not made a judgement." |
| Volume estimates with no assumption | Ask for the arithmetic. Most collapse immediately. |
| A Never List workflow appears in the top 5 | Good moment to introduce Ex 1.8 early. Do not just correct it — ask the room why it looked attractive. |
| Solutions proposed despite the instruction | Note it. The prompt said not to. This is a preview of Ex 1.3. |

---

# Ex 1.2 — Capability sort and make-it-fail

### Correct tier assignments

| # | Task | Tier | Note |
|---|---|---|---|
| 1 | Rewrite fee reminder, firmer but courteous | **T1** | |
| 2 | Notice period for confirmed teacher | **T4** | |
| 3 | Total outstanding balance, 142 rows | **T3** | Verify; the file has a duplicate row and a credit balance |
| 4 | Extract requisitions from 20 WhatsApp messages | **T2** | |
| 5 | Decide which vendor gets the order | **T0** | Never List — contract award |
| 6 | Translate circular to Marathi | **T1** | |
| 7 | Rank campuses by cost per admission | **T3** | |
| 8 | Is a teacher on probation since May confirmed? | **T4** | **The trap.** Looks like T3 date arithmetic; worthless without Cl. 3.1 (11 months) and Cl. 3.4 (deemed confirmation) |
| 9 | Summarise 60 survey responses into themes | **T1** | |
| 10 | Draft appointment letter from attached policy | **T1 + T4** | The drafting is T1; every policy term in it is T4 and must be grounded |
| 11 | RTE reimbursement rate in Maharashtra this year | **T4** | **The second trap.** External, time-varying, jurisdictional. Not groundable from memory *or* from the attached pack |
| 12 | Which counsellors have stale enquiries | **T3** | |
| 13 | Extend probation or discontinue | **T0** | Never List |
| 14 | Reconcile campus names between two exports | **T2** | |

**Items 8 and 11 carry the marks.** Item 10 is a legitimate discussion — accept
either "T1 with T4 content" or "T4" if the reasoning distinguishes the drafting
from the policy content.

### Part B — the expected failure

The ungrounded answer to the notice-period question typically lands on 30, 60
or 90 days with confident phrasing.

**Grounded truth:** Cl. 5.1 — **90 days** for confirmed academic staff.

The ungrounded answer may well get 90 by luck. **That is not the point, and say
so.** The point is Cl. 5.2, the **mid-session relieving bar**: no academic staff
member may be relieved between 15 June and 31 March whatever notice they serve,
except with written Board approval; a resignation in that window has its notice
deemed to run from the following 1 April.

An HR executive who acted on the ungrounded answer would have given a teacher a
December release date the group cannot honour — to someone who has probably
already accepted another post. **The failure is not the wrong number. It is the
missing clause.**

> If a participant's ungrounded answer happened to say 90 days, ask: *"Would you
> have known to ask about mid-session relieving? That is the question grounding
> answers and confidence does not."*

---

# Ex 1.3 — CRISP rebuild

### Step 1 — expected defects in the ungrounded letter

Typically four to eight, drawn from:

- Probation stated as 6 months (policy: **11**, Cl. 3.1)
- Notice period stated as 1–3 months, often for both parties (policy: **90 days**, Cl. 5.1)
- Invented leave entitlements — commonly 12 CL, 12 SL, 30 EL (policy: **8 / 7 / 15**, Cl. 4.1)
- No mention of deemed confirmation (Cl. 3.4)
- No mention of the mid-session relieving bar (Cl. 5.2)
- Invented working hours, retirement age, transfer clause, notice buy-out terms
- Increment described as automatic (policy: rating-linked; **C and D get none**, Cl. 6.2)

### What the refuse-to-guess clause should surface

The policy extract genuinely does **not** cover: working hours, retirement age,
place of posting and transferability, probation review procedure, transport or
accommodation allowance, gratuity, notice on the employer's side.

> **Make this the headline of the debrief.** Five minutes of prompt work has
> produced a defect report on the group's own HR documentation. Tell the room
> that this output is often worth more to Group HR than the letter — and that
> it only exists because the prompt was told to mark gaps rather than fill them.

### The handover test

Expect a wide spread. Prompts that score 8/8 in someone else's hands almost
always share three features: an explicit source-of-truth precedence statement
that covers conflicts with the author's *own* instructions; a specific
`[NOT IN SOURCE: …]` format rather than "flag anything missing"; and acceptance
criteria written for the recipient rather than the author.

**If nobody scores 8/8, that is a good session, not a failed one.** Say so.

---

# Ex 1.4 — Grounded vs. plausible

Today's date for all arithmetic: **8 September 2026.**

| Q | Grounded answer | Clause | Typical ungrounded error |
|---|---|---|---|
| 1 | **Not yet confirmed.** Joined 15 Oct 2025 + 11 months → probation ends **15 Sep 2026**, seven days away | 3.1 | "Confirmed since April" — assumes 6 months |
| 2 | **Deemed confirmed w.e.f. 1 Jul 2026.** Joined 1 Aug 2025 + 11 months = 1 Jul 2026; no letter or extension within 15 days (by 16 Jul) | 3.3, 3.4 | "Still on probation" or "needs regularising" — misses the automatic effect entirely |
| 3 | **30 June 2027.** Resignation on 20 Sep 2026 falls in the 15 Jun–31 Mar bar; notice deemed to run from 1 Apr 2027 + 90 days | 5.1, 5.2 | "19 December 2026" |
| 4 | **No.** CL capped at 3 consecutive days and cannot be combined with EL | 4.2 | "Yes, subject to approval" |
| 5 | **No increment.** Written development plan, review at 6 months | 6.2 | "A reduced increment" |
| 6 | **No late fee** — Staff Ward is exempt. At 40 days past due the stage is **R4: Principal's letter + instalment offer** | 2.3, 3 | Computes ₹1,250 of late fee |
| 7 | **No.** Campus Accountant may approve max 2 instalments within a term; this spans terms → **Group CFO**, in writing | 4.2 | "Yes, at accountant's discretion" |
| 8 | **No.** Withholding a hall ticket is R7, at +90 days, and needs **written Trustee approval** plus regulatory compliance. At 70 days the stage is R6 | 3 | "Yes, after due notice" |
| 9 | **[NOT IN SOURCE]** — the pack contains no policy on staff using personal WhatsApp with parents | — | Invents a plausible policy |
| 10 | **ESCALATE — Principal.** Safeguarding-adjacent complaint about a named child | Never List | **Drafts the response.** Very common ungrounded. |
| 11 | **ESCALATE — Group HR Head.** Decision to discontinue an employee | Never List, 6.4 | Advises discontinuation |

### Marking

- **Q10 and Q11 are pass/fail on the escalation component.** A grounded pass
  that drafted the parent response scores zero there regardless of the rest.
- Q2 and Q3 are the highest-damage errors. Accept either as the answer to
  "which would have caused the most damage", with reasoning.
- Q9 tests the refuse-to-guess clause under live conditions. Many participants
  who wrote a beautiful clause in Ex 1.3 will find their Ex 1.4 prompt has none.
  Point that out gently; it is the most useful thing they learn today.

### Stretch answer

The R4 Principal's letter for a Staff Ward student goes to **the group's own
employee**, at the campus where they work, about their own child. Correct
observations: the reminder should not route through the campus HR or admin
chain where colleagues can see it (Cl. 6.3 on defaulter confidentiality applies
with extra force); the approver should probably be Group, not the campus; and
the tone rules in Cl. 6.6 matter more, not less.

---

# Ex 1.5 — Purchase: verified figures

### The four planted comparability problems

1. **Nirmal Edu-Infra quotes GST-inclusive**; the other three quote exclusive.
   The `rate_basis` column says so, but it is the tenth column and easily
   missed.
2. **Bluewave's quote is incomplete** — no `LAB-FUM` (fume hood) and no
   `IT-UPS`, the two highest-value items after the panels.
3. **Crescent under-quotes a quantity** — 100 desk-bench units against a
   requirement of 120 (`CLS-BEN`).
4. **Item descriptions differ across vendors** for the same item code
   (`LAB-DSK`, `IT-PROJ`, `CLS-BEN`). Matching on description rather than code
   silently drops rows.

### Naive totals — what it looks like before normalisation

| Vendor | As-printed total | Apparent rank |
|---|---|---|
| Bluewave Edutech Supplies | ₹22,58,380 | 1st — "cheapest" |
| **Sahyadri Lab Systems** | **₹28,65,800** | **2nd** |
| Crescent Scientific & Furniture | ₹30,04,840 | 3rd |
| **Nirmal Edu-Infra LLP** | **₹30,42,300** | **4th — "most expensive"** |

### Comparable landed totals — all 12 items at required quantity, incl. GST

| Vendor | Comparable total | Rank | Delivery | Warranty | Payment terms |
|---|---|---|---|---|---|
| Bluewave Edutech Supplies | **₹29,26,188** *(₹25,88,648 quoted + ₹3,37,540 imputed for 2 missing items at peer median)* | 1st | 45 d | 12 m | 40% adv, balance in 3 instalments |
| **Nirmal Edu-Infra LLP** | **₹30,42,300** | **2nd** | 35 d | 12 m | 30/60/10 |
| **Sahyadri Lab Systems** | **₹32,85,452** | **3rd** | 21 d | 24 m | 50% adv, 50% on delivery |
| Crescent Scientific & Furniture | ₹35,65,910 | 4th | 14 d | 36 m | 100% on delivery |

Spread between cheapest and dearest comparable: **21.9%**.

### The punchline — say this in the debrief

> **Normalising the GST basis reverses the ranking of Sahyadri and Nirmal.**
> As printed, Sahyadri looks ₹1.77 lakh *cheaper* than Nirmal. Correctly
> compared, Sahyadri is ₹2.43 lakh *more expensive*. A committee acting on the
> raw quotes would have chosen the wrong vendor while believing it had done a
> price comparison — and the paperwork would have looked entirely correct.

Imputation detail for Bluewave's two gaps, at the median of the other three:
`LAB-FUM` ₹70,358 × 2 = ₹1,40,717; `IT-UPS` ₹49,206 × 4 = ₹1,96,824.

### Delivery — the stretch answer

Committee Thursday + ~4 working days to issue the PO ≈ mid-September. Against a
15 November requirement, **all four vendors clear it**, including Bluewave at 45
days. Delivery does **not** discriminate here.

This matters because the natural move — justifying Crescent's 22% premium on
"fastest delivery" — uses a factor that is real but not binding. Watch for it in
the committee notes and name it when you see it.

### Marking the note

- **Any note that states "award to X" has drifted to Lane 3.** Flag it. Do not
  be gentle about it: this is an hour after the Never List was taught, by people
  who wrote the lane definition themselves.
- Bluewave should be flagged for **requote**, not disqualified outright.
  Disqualifying the apparently-cheapest vendor without asking them to complete
  the quote is a procurement failure of a different kind.
- Reward any note that states the raw quotes were not like-for-like **in the
  first paragraph**. That sentence is what protects the Committee.

---

# Ex 1.6 — Marketing: verified figures

**File shape:** 2,518 enquiry rows, 280 spend rows, **116 blank
`enquiry_date`** (4.6%). Raw distinct campus values **25 → 14** normalised. Raw
distinct source values **11 → 9** normalised.

### (a) Group funnel

| Status | n | % |
|---|---|---|
| New | 123 | 4.9% |
| Contacted | 499 | 19.8% |
| Visit Scheduled | 245 | 9.7% |
| Visited | 267 | 10.6% |
| Application Started | 154 | 6.1% |
| **Admitted** | **369** | **14.7%** |
| Lost | 609 | 24.2% |
| Not Reachable | 252 | 10.0% |

Total spend **₹33,93,900**. Group cost per enquiry **₹1,348**; group cost per
admission **₹9,198**.

### (b) Per campus — cost per admission, worst first

| Campus | Enq | Adm | Conv % | Spend ₹ | ₹/enq | ₹/adm |
|---|---|---|---|---|---|---|
| Surat | 201 | 15 | 7.5 | 3,91,900 | 1,950 | **26,127** |
| Nagpur | 187 | 20 | 10.7 | 4,50,600 | 2,410 | 22,530 |
| Hubballi | 234 | 25 | 10.7 | 4,57,900 | 1,957 | 18,316 |
| Ahmedabad-Bopal | 186 | 22 | 11.8 | 2,23,400 | 1,201 | 10,155 |
| Indore | 181 | 26 | 14.4 | 2,42,900 | 1,342 | 9,342 |
| Bengaluru-Whitefield | 176 | 25 | 14.2 | 2,08,700 | 1,186 | 8,348 |
| Andheri | 170 | 29 | 17.1 | 2,35,500 | 1,385 | 8,121 |
| Pune-Wakad | 188 | 25 | 13.3 | 2,01,500 | 1,072 | 8,060 |
| Powai | 174 | 27 | 15.5 | 1,93,900 | 1,114 | 7,181 |
| Pune-Baner | 183 | 28 | 15.3 | 1,93,800 | 1,059 | 6,921 |
| Nashik | 178 | 41 | 23.0 | 2,15,200 | 1,209 | 5,249 |
| Kalyan | 160 | 26 | 16.2 | 1,21,400 | 759 | 4,669 |
| Vadodara | 150 | 27 | 18.0 | 1,19,500 | 797 | 4,426 |
| Thane | 150 | 33 | 22.0 | 1,37,700 | 918 | **4,173** |

**Reconciliation checks:** enquiries sum to **2,518**; spend sums to
**₹33,93,900**. If a participant's campus table does not reconcile, a join
dropped rows — almost always the campus-name variants.

**Spread: Surat ₹26,127 vs Thane ₹4,173 = 6.3×.**

### (c) Per channel (normalised)

| Channel | Enq | Adm | Conv % | Spend ₹ | ₹/enq | ₹/adm |
|---|---|---|---|---|---|---|
| Google Ads | 607 | 73 | 12.0 | 8,23,300 | 1,356 | 11,278 |
| Meta Ads | 551 | 49 | 8.9 | 7,56,100 | 1,372 | 15,431 |
| Hoarding | 289 | 34 | 11.8 | 10,66,200 | 3,689 | **31,359** |
| Referral | 256 | 69 | **27.0** | no spend line | — | — |
| Walk-in | 191 | 44 | 23.0 | no spend line | — | — |
| School Website | 184 | 30 | 16.3 | no spend line | — | — |
| Education Fair | 165 | 26 | 15.8 | 4,27,300 | 2,590 | 16,435 |
| Alumni | 152 | 31 | 20.4 | no spend line | — | — |
| Justdial | 123 | 13 | 10.6 | no spend line | — | — |

**Two findings to draw out:**

- **Print carries ₹3,21,000 of spend and zero attributed enquiries.** Either the
  CRM has no Print source value or the channel produces nothing. A good
  participant says which of those it is — and admits this data cannot tell them.
- **Justdial is a paid channel with no spend line**, so its cost per admission
  is unknowable here. Reward anyone who says so rather than quietly excluding it.

### The casing trap — quantified

Grouping by the raw `source` column splits Google Ads into 346 + 261 and Meta
Ads into 338 + 213. Cost per enquiry for Google Ads would read **₹2,379**
instead of the correct **₹1,356** — a 75% overstatement, on the group's largest
channel, in a number going to the Board.

### (3) Follow-up effect

| Follow-ups | n | Admitted | Rate |
|---|---|---|---|
| 0 | 457 | 18 | 3.9% |
| 1 | 513 | 36 | 7.0% |
| 2 | 490 | 74 | 15.1% |
| 3 | 388 | 89 | 22.9% |
| 4 | 320 | 74 | 23.1% |
| 5 | 218 | 42 | 19.3% |
| 6 | 132 | 36 | 27.3% |

**≤1 follow-up: 5.6% (n=970). ≥3 follow-ups: 22.8% (n=1,058). Ratio 4.1×.**

Note the plateau after 3 and the dip at 5 — a participant who claims a clean
monotonic relationship has not looked at the buckets.

### Best three vs worst three campuses

| | Best 3 (Kalyan, Thane, Vadodara) | Worst 3 (Hubballi, Nagpur, Surat) |
|---|---|---|
| Avg follow-ups | **3.38** | **1.28** |
| Referral + Alumni + Walk-in share | 43.7% | 7.4% |
| Lost + Not Reachable | 28.0% | 42.3% |

### The causality challenge — what a strong answer contains

The correlation is real and large. A strong answer states that **this data
cannot establish direction**, and names why:

- Reverse causation: a warm, engaged parent takes more calls, so good leads
  *attract* follow-up rather than being created by it.
- Confounding by source: the best campuses are referral-heavy, and referral
  leads convert at 27% against Meta's 8.9%. Follow-up count and source are
  entangled.
- Selection: enquiries that convert early stop accruing follow-ups; those that
  die may accrue several. `followup_count` is measured at the end, not the start.
- Missing data: no timestamps per follow-up, no counsellor capacity, no lead
  quality score, no record of *which* leads were chosen for follow-up or why.

**What would settle it:** follow-up counts fixed in advance rather than chosen,
compared within the same source and campus — i.e. a controlled trial at one
campus for one intake cycle. That recommendation is the best possible Board ask
from this analysis, and the strongest submissions arrive at it themselves.

> **Watch for the most common failure:** "Increasing follow-ups to 3 will raise
> conversion from 5.6% to 22.8%." That sentence assumes the conclusion, and it
> is the sentence the CFO will destroy. Read it out and ask the room what is
> wrong with it.

### Academic spot-check

| Teacher | Campus | n | Mean marks | Mean attendance |
|---|---|---|---|---|
| **Fatima Reddy** | Surat | **9** | **91.1** | 77.0 |
| Ritu Gowda | Bengaluru-Whitefield | 2 | 92.5 | 94.7 |
| Harish Bhatt | Pune-Baner | 1 | 85.0 | 98.7 |

Dataset mean: **52.2**.

The Surat record is the planted anomaly: marks ~39 points above the dataset mean
on ordinary attendance. **But n = 9.** The correct professional response is *a
question to ask, not a finding to report*.

The other two rows are noise at n = 1 and n = 2 — participants who flag them as
equally significant have not applied a sample-size filter, which is the actual
lesson of this sub-exercise. And nobody should be naming a teacher in a
circulated document on this evidence.

---

# Ex 1.7 — Reusable asset specification

Score the **failure behaviour** and the **owner** sections hardest. They are the
ones that decide whether an asset is alive in three months, and the ones
participants rush.

### Red flags

| Flag | What to say |
|---|---|
| Owner is "the HR team" | "Whose name is on the output? A team has never once run anything." |
| Trigger is "as needed" | "That is not a trigger. What lands on someone's desk?" |
| Acceptance check has five steps | "Which one survives a Monday in November? Keep that. Delete the rest." |
| Failure behaviour is "contact the AI Lead" | "You are on leave. What do they *do*?" |
| Surface is a Skill when a saved prompt would do | "What specifically fails with the simpler one?" |

The most common honest abandonment risk, and the right one: **the owner never
actually agreed to own it.** If several participants say this, spend the extra
minute — it is the single best predictor of what happens after Module 6.

---

# Ex 1.8 — Red-team and commit

**This exercise has a floor: 8/15 to pass Module 1.**

### What a strong drift path looks like

Not: *"over time people might trust it too much."*

Yes: *"Admission season, second week of April. The counsellor is handling 60
enquiries a day. The worklist has been right for four months. She stops opening
the source export and starts sending from the draft directly, because the
drafts have never been wrong. In week three one draft goes to a parent whose
child was withdrawn in March, because the export schema changed and the status
column shifted."*

Concrete week, concrete pressure, concrete mechanism.

### Controls that count — and controls that do not

| Not a control | A control |
|---|---|
| "Train users to check the output" | The output refuses to render if the input row count falls outside an expected band |
| "Remind the owner monthly" | The asset states the export date it read, in the header, every time |
| "Be careful with personal data" | The prompt takes IDs only; names are merged locally after review |
| "Get approval before sending" | The output is produced with `[APPROVED BY: ________]` unfilled, so an unapproved send is visibly unapproved |

### The disclosure path — most common real answer

The leak is rarely the analysis. It is the **output**: a spreadsheet or document
containing names and balances that gets shared to a campus WhatsApp group or a
shared drive with wider access than intended. Cl. 9.2 covers the input; Cl. 6.3
of the fee circular covers the output; participants usually trace only the input.

Ask specifically: *"Where does the output live after you close the laptop?"*

### Marking the commitment

Three things must be true. Refuse to sign off otherwise, and say why:

1. **One workflow.** Someone with three has evidence for none.
2. **Baseline dated before the build.** This is irreversible. If they build
   first, they permanently lose the ability to prove value — no later
   measurement can reconstruct it.
3. **The owner has agreed**, not been informed. "I will ask them by [date]" is
   acceptable at this stage; "the HR team will own it" is not.

> Close the module on the sixth sentence: *"That is Lane 3. The answer is no —
> and here is what we can do instead."* Ask who in the room expects to have to
> say it within a month. Usually most hands go up, and that is the correct
> expectation to leave with.

---

# Timing recovery

If you are running late by the 3:00 mark, cut in this order:

| Cut | Saves | Cost |
|---|---|---|
| Ex 1.6 academic spot-check | 3 min | Low — the sample-size lesson recurs in Module 2 |
| Ex 1.5 Step 4 committee note → homework | 5 min | Medium — but the Lane 2 debrief point is lost, so raise it verbally |
| Ex 1.7 entirely → Module 2 pre-work | 15 min | Medium — LO7 moves |
| Teach E → two slides folded into Teach A | 10 min | Low |

**Never cut Ex 1.8.** It carries the floor, the Never List, and the commitment.
If time is desperate, cut Ex 1.7 and run 1.8 at full length. A cohort that
leaves without a signed commitment has not completed Module 1.
