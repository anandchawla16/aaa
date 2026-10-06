# Module 1 Participant Workbook
## Foundations: The Group as Workflows

Keep this open beside your Claude window for the whole session. The teaching
blocks are here; the exercises are in [`exercises/`](exercises/).

---

# Opening · 12 min

## The one thing to hold on to

> You are not being trained to use a tool. You are being trained to **redesign
> five business functions** so that the language work in them is carried by an
> assistant, and the judgement in them stays with a person whose name is on it.

Everything today is a school group problem first and an AI problem second.

## The Never List — read before anything else

These are never delegated to an AI assistant, never drafted by one for direct
send, and never decided with one, at any level of maturity:

1. Any student safeguarding, child protection or disciplinary matter.
2. Any decision to admit, reject or withdraw a student.
3. Any decision to hire, not confirm, promote or terminate an employee.
4. Salary fixation, appraisal ratings, disciplinary findings.
5. Award of a contract or purchase order.
6. Any communication carrying a legal threat or a statutory representation.
7. Anything involving a named child's health, behaviour or family circumstances.

You may use AI to **prepare, structure, summarise or draft inputs into** these
decisions where policy allows. The decision, the wording that goes out, and the
signature stay human.

You will be asked to apply this list in Ex 1.8. Participants who cannot are not
certified, whatever their score.

## The synthetic-data rule

Today you work only on the **Meridian Group of Schools** pack in
[`../data/`](../data/). It is entirely fictional. You do not paste your group's
real staff, student, parent or vendor data into anything during this programme
until you have completed Module 5. This rule is part of the curriculum, and it
is enforced.

---

# Teach A · The five-function operating map · 13 min

## Stop thinking in departments. Think in workflows.

A department is an org chart box. A **workflow** is a repeating unit of work
with five properties you can actually measure:

| Property | The question | Why it matters |
|---|---|---|
| **Trigger** | What starts it? A date, an event, a message, a person? | Date-triggered work is the easiest to systematise. Message-triggered work is the highest volume. |
| **Volume** | How many times per week, group-wide? | Below ~10/week, almost nothing is worth building. |
| **Owner** | Whose name is on the output? | No name, no workflow. "The system does it" is how audit failures happen. |
| **Failure mode** | When it goes wrong, what actually happens? | This is what sets the risk tier, not the topic. |
| **Cycle time** | Trigger to done, in elapsed hours or days? | The gap between cycle time and *touch* time is where the value usually is. |

## The five functions, honestly described

| Function | The work is mostly… | Highest-volume workflow | The real bottleneck |
|---|---|---|---|
| **HR** | Drafting and answering | Letters (offer → appointment → confirmation → transfer → experience) and staff policy queries | 6 people at Group serving 1,650 staff; every letter is retyped |
| **Academics** | Reading and summarising | Assessment review, intervention lists, parent-facing reports, teacher documentation | Teachers doing 4h/week of admin that nobody reads |
| **Accounts** | Reconciling and chasing | Fee follow-up across 7 escalation stages | Escalation happens late and inconsistently, so recovery is worse than it should be |
| **Purchase** | Comparing and normalising | Three-quote comparison; requisition intake from WhatsApp | Comparisons take days, so campuses go single-source and fail audit |
| **Marketing & Admissions** | Prioritising and following up | Enquiry follow-up; channel performance review | 38 counsellors, no shared view of which lead deserves the next call |

Notice what these have in common. **Almost all of it is language work performed
on the group's own data.** That is precisely the shape of work an AI assistant
can carry — and precisely the shape of work that goes wrong silently if the data
is defective or the policy is guessed.

## VFRR — the scoring frame you will use all day

Score each workflow 1–5 on four axes. The formula is deliberately simple; the
argument about the score is where the learning is.

| Axis | 1 | 3 | 5 |
|---|---|---|---|
| **V — Volume** | < 10 / week group-wide | ~50 / week | > 200 / week |
| **F — Friction** | Runs smoothly today | Slow, inconsistent between campuses | Actively failing; people complain unprompted |
| **R — Risk if wrong** | Internal only, easily corrected | Affects a parent or vendor, recoverable | Legal, statutory, safeguarding, or child-affecting |
| **Rd — Readiness** | Data doesn't exist or is on paper | Exports exist but are dirty | Clean export, clear policy, willing owner |

**Priority = (V + F + Rd) − R**

Range −2 to 14. The subtraction is the whole point: **high risk pushes work
down the list, it does not disqualify it.** A high-risk workflow can still be
worth doing — with Lane 2 or Lane 3 controls — but it should not be your first
build. Your first build should be something with volume, pain, good data, and
a failure mode that embarrasses nobody.

**A worked example:**

> *Fee reminder drafting, stages R1–R3.*
> V = 5 (50 outstanding accounts × 3 stages × 14 campuses, weekly).
> F = 4 (each accountant writes their own; tone varies wildly; R3 often skipped).
> R = 3 (goes to a parent, affects trust, but recoverable and policy-bounded).
> Rd = 4 (ledger exports cleanly enough; Clause 3 ladder is unambiguous;
> the CFO wants it).
> **Priority = (5 + 4 + 4) − 3 = 10.** Strong first candidate.

> *Drafting a response to a safeguarding complaint.*
> V = 1, F = 5, R = 5, Rd = 2. **Priority = (1 + 5 + 2) − 5 = 3.**
> High friction, genuinely painful — and correctly near the bottom. It is also
> on the Never List, so it is not a candidate at all.

→ **Now do [Ex 1.1 — Workflow inventory](exercises/ex-1-1-workflow-inventory.md).**

---

# Teach B · The capability boundary: four trust tiers · 12 min

Most failures in AI deployment are not model failures. They are **tier
confusion** — someone trusted a Tier 4 answer as if it were a Tier 1 answer.

| Tier | Class of work | Trust posture | Check required |
|---|---|---|---|
| **T1** | **Language transformation** — rewrite, summarise, translate, reformat, change tone, extract structure from text you supplied | High. This is the model's strongest ground. | Read it. Normal editorial review. |
| **T2** | **Structured extraction & normalisation** — pull fields out of messy text, reconcile naming variants, classify into your categories | High, but **verify the schema**, not every row | Spot-check 5 rows and every edge case; confirm the row count |
| **T3** | **Analysis over data you supplied** — totals, groupings, rates, comparisons, ranking | Medium. The reasoning is usually sound; **arithmetic and joins must be independently confirmed** | Recompute at least one headline number a second way |
| **T4** | **Facts about your institution** — your policy, your dates, your approval limits, your fee slabs, your history | **Zero.** Never accept from memory. | Must be grounded in an attached document. No document, no answer. |

And outside the tiers entirely:

| **T0 — Judgement and authority** | Who to hire, who to admit, who gets the contract, what a parent is told about their child | Not a capability question. A governance one. See the Never List. |

## The rule that follows from this

> **Tier 4 work must be grounded. Tier 3 work must be verified. Tier 2 work must
> be spot-checked. Tier 1 work must be read.**

Say it in that order. It is the most useful sentence in this module.

## Why Tier 4 is the dangerous one

A model asked "what is the probation period at Meridian?" will produce a
confident, well-written, *reasonable* answer — six months, probably, because
that is the industry norm. Meridian's probation period is **eleven months**
(Clause 3.1), extendable once by three, with a **deemed confirmation** rule at
day fifteen that almost no policy anywhere else has.

The answer will not look wrong. It will look excellent. That is the problem: a
Tier 4 failure is indistinguishable from success at the point of reading. This
is why grounding is a *procedure*, not a preference.

→ **Now do [Ex 1.2 — Capability sort and make-it-fail](exercises/ex-1-2-capability-boundary.md).**

---

# Teach C · CRISP prompt architecture · 15 min

A prompt that works once, for you, is a party trick. A prompt that works next
month, for someone else, on next month's export, is an asset.

**CRISP** is five things every production prompt in this group must contain.

| | Element | What goes in it | What breaks without it |
|---|---|---|---|
| **C** | **Context** | Who the group is, which campus, which function, what this output is for, who reads it, what is at stake | Generic output that fits any school and serves none |
| **R** | **Role & audience** | Who Claude is acting as, and who receives the result | Wrong register — an HR letter that reads like a blog post |
| **I** | **Inputs & source of truth** | The attached files, and an explicit statement of which document *governs* when sources disagree | Tier 4 failures: confident invented policy |
| **S** | **Steps & refuse-to-guess clause** | The reasoning path, and what to do when the data does not support an answer | Silent gap-filling — the single most expensive failure mode |
| **P** | **Product & acceptance criteria** | Exact output shape, length, columns, and how the reader will check it | Something you have to rewrite by hand, which means nobody reuses it |

## The refuse-to-guess clause

This is the sentence that separates a hobbyist prompt from a production one.
Write some version of it into everything:

> *"Where the attached documents do not contain the information needed, do not
> infer it, do not use general knowledge, and do not leave it blank. Write
> `[NOT IN SOURCE: <what is missing>]` and continue. List every such gap at the
> end under 'Open items'."*

Three things this buys you:

1. Gaps become **visible** instead of becoming plausible fabrications.
2. The output stays usable — you get the 90% that is answerable.
3. The "Open items" list is a **defect report on your own data**, which is often
   more valuable than the output itself.

## Acceptance criteria

State how the reader checks the output before they trust it. For example:

> *"Before the table, state the number of input rows read and the number
> excluded, with the reason for exclusion. The two must reconcile to the file's
> row count."*

If you cannot say how someone would catch an error, you have not finished
writing the prompt.

## Before and after

**Before** — a real prompt, and a bad one:

> *"Write an appointment letter for a teacher."*

**After** — the same request, CRISP-structured:

> **Context.** Meridian Group of Schools, a 14-campus K–12 group in India. This
> is an appointment letter for a newly selected academic staff member at the
> Pune-Baner campus, issued by Group HR, signed by the Group HR Head. It becomes
> a contractual document and may be produced before a labour authority.
>
> **Role.** Act as an experienced HR officer in an Indian K–12 school group,
> drafting for a candidate who will read it carefully and may have it reviewed.
>
> **Inputs.** Use the attached `hr-service-and-leave-policy.md` (MGS/HR/POL/07
> v4.2) as the **sole and governing** source for probation, leave, notice and
> appraisal terms. Candidate details are in the block below. Where the policy and
> my instructions conflict, the policy governs and you flag the conflict.
>
> **Steps.** (1) Identify every policy term that must appear in an appointment
> letter. (2) Draft the letter. (3) Cite the clause number in a bracket after
> each policy term stated. (4) Where a required detail is not in the policy or the
> candidate block, write `[NOT IN SOURCE: …]` — do not infer it, do not use
> general knowledge of Indian school HR practice, do not leave it blank.
>
> **Product.** A complete letter, 400–550 words, in formal Indian business
> English, with a subject line, numbered terms, and a signature block. Follow it
> with two sections: "Clauses cited" and "Open items". No preamble, no
> commentary.

The second one is longer. It is also the one you can hand to a colleague, and
the one whose output you can defend.

→ **Now do [Ex 1.3 — CRISP rebuild](exercises/ex-1-3-crisp-rebuild.md).**

---

# Teach D · Grounding and the source-of-truth rule · 12 min

## Grounding is not "attaching a file"

Grounding is a three-part discipline:

**1. Attach the governing document — and say that it governs.**
Not "here is some context". Say: *this document is the sole source of truth for
X; where it is silent, say so; where it conflicts with anything else including
my own instructions, it wins and you tell me.*

**2. Know the defects before you trust the totals.**
Every export in this group is defective. Before any analysis, ask for a defect
report, not an answer:

> *"Before analysing anything: list every data-quality problem you can see in
> this file — inconsistent categorical values, mixed formats, blanks,
> duplicates, impossible values, and anything that would make a group-by
> produce a wrong total. Do not analyse yet. Just the defect list, with the
> affected row counts."*

Run this **first, every time, on every new export.** In today's data it will
find the campus-name variants, the mixed date formats, the Indian-format
numbers, the duplicate rows, and the case-inconsistent channel names. Each of
those silently corrupts a total if you skip this step.

**3. Verify the headline number a second way.**
Tier 3 discipline. If the answer is "₹13.58 lakh outstanding", ask for it again
segmented differently — by campus, by term, by ageing bucket — and check the
segments sum to the same total. If they do not, you have found a real problem,
and you found it before the CFO did.

## Citation as a standing requirement

For anything policy-related, require the clause number inline. Not at the end —
inline, next to the claim. Two reasons:

- **You can check it in ten seconds.** An uncited claim takes ten minutes.
- **An uncitable claim becomes visible.** If the model cannot attach a clause,
  it usually means the policy does not actually say that.

## The trap you are about to walk into

In Ex 1.4 you will ask the same policy questions twice — once without the
policy attached, once with. The ungrounded answers will be fluent, confident,
professionally worded, and wrong on the specifics that matter: probation
length, casual leave, notice period, and a deemed-confirmation rule that exists
nowhere else.

The lesson is not "the model was wrong". The lesson is that **you could not have
told from reading it.** That is why grounding is a procedure and not a
judgement call.

→ **Now do [Ex 1.4 — Grounded vs plausible](exercises/ex-1-4-grounded-vs-plausible.md),
then [Ex 1.5 — Normalising four quotations](exercises/ex-1-5-purchase-normalisation.md),
then [Ex 1.6 — An insight in 2,518 rows](exercises/ex-1-6-marketing-funnel.md).**

All three apply the same discipline to three different functions: HR policy,
Purchase quotations, Marketing CRM data. The instruction that opens each is the
same — *defect report first, analysis second.*

---

# Teach E · From a prompt to a reusable asset · 10 min

A prompt is a conversation. An **asset** is something a campus administrator
runs every Monday without you, and without thinking.

## What separates them

| Prompt | Asset |
|---|---|
| Lives in your chat history | Lives somewhere the owner can find it |
| Assumes context you carry in your head | Carries its own standing context |
| Works on the file you had open | States exactly which export, from which system, in which format |
| Fails silently on bad input | States what to do when the input looks wrong |
| You own it | A **named non-you person** owns it |

## The four surfaces, inside Claude

| Surface | Use it for | Example here |
|---|---|---|
| **A saved prompt** | A single repeated task with one input | The R1–R3 fee reminder drafter |
| **A Project** with standing context | A whole function's work, sharing the same background | "Meridian HR" — the fact sheet and policy attached once, every HR task inherits them |
| **A Skill** | A repeatable procedure with rules, templates and a defined output | Letter generation across the six letter types |
| **An artifact** | Something people look at or use — a checklist, a worklist, a review page | The counsellor's daily worklist |

Choose the **lowest-effort surface that survives handover.** Most first builds
are a saved prompt inside a Project. Very few need to be more than that.

## The six things an asset specification must state

1. **Trigger** — when it runs, and what starts it (a date, an export, an event).
2. **Owner** — the named person, not the role, who runs it and whose name is on
   the output.
3. **Inputs** — exact file, exact system, exact export settings, expected shape.
4. **Steps** — the CRISP prompt itself.
5. **Output and acceptance check** — what is produced, and the one check the
   owner performs before acting on it.
6. **Failure behaviour** — what the owner does when it looks wrong, and who they
   call. *This is the field most people leave out and the one that decides
   whether the asset is alive in three months.*

→ **Now do [Ex 1.7 — Reusable asset specification](exercises/ex-1-7-reusable-asset-spec.md).**

---

# Teach F · Guardrails, PII and the Three-Lane model · 10 min

## The Three-Lane model

Every workflow in the group sits in exactly one lane. Deciding the lane is the
first governance act, and it is not negotiable by enthusiasm.

| Lane | Definition | AI's role | Human's role | Examples here |
|---|---|---|---|---|
| **Lane 1 — Draft** | Output is language that a human reads, edits and sends under their own name | Drafts | Reviews every word, approves, sends | Fee reminders R1–R4, HR letters, parent circulars, vendor correspondence |
| **Lane 2 — Decide-support** | Output is analysis that informs a human decision | Analyses, structures, ranks, flags | Verifies the numbers, makes the decision, owns it | Quote comparison, funnel analysis, ageing report, intervention lists |
| **Lane 3 — Never** | Output would itself constitute or determine a decision about a person | None | Everything | Everything on the Never List |

Two rules that catch most mistakes:

- **A Lane 1 output never sends itself.** Clause 6.5 of the fee circular is
  explicit: every outbound fee communication is approved by a named human. The
  same principle applies group-wide.
- **A Lane 2 output never states a decision as a conclusion.** It says "Vendor B
  is lowest on normalised landed cost, subject to the delivery risk noted"; it
  does not say "award to Vendor B."

## Personal data — the practical rules

Clause 9.2 of the service policy is the binding one: employee or student
personal data **may not be transferred to, pasted into, or processed by any
system not on the Approved Systems List**.

What that means at your desk, today:

| Situation | Do |
|---|---|
| You need analysis of fee data | Use IDs and amounts. Strip names, phone numbers, addresses, parent names. |
| You need a letter drafted for a specific employee | Draft with placeholders — `[EMPLOYEE NAME]`, `[EMP ID]` — and merge locally. |
| The analysis genuinely needs the identity | Stop. That is a Module 5 conversation and a written approval, not a judgement call you make alone. |
| You are unsure whether a field is personal data | Treat it as if it is. |

**The rule of thumb:** an AI assistant almost never needs to know *who*. It
needs to know *what, how much, how long, and against which rule.* If you find
yourself pasting a name, ask what the name is doing for the analysis. Usually,
nothing.

## Red-teaming your own build

Before anything goes to a real user, spend ten minutes attacking it yourself.
Four questions:

1. **Wrong-but-plausible.** If the output were subtly wrong, would the owner
   notice? If not, what check makes it noticeable?
2. **Disclosure path.** What personal data enters this workflow, where does it
   travel, and who ends up able to see it who should not?
3. **Worst-case send.** If this output went out unreviewed — because someone was
   busy, on a Friday — what is the worst message a parent, employee or vendor
   receives?
4. **Lane drift.** Six months from now, when it is trusted and nobody checks,
   has this quietly become a Lane 3 workflow?

Question 4 catches the failure that matters most. Workflows do not usually start
in the wrong lane. They **drift** there, one busy week at a time.

→ **Now do [Ex 1.8 — Red-team and commitments](exercises/ex-1-8-red-team-and-commit.md).**

---

# Close

## What you should now be able to say

- "Here are the six workflows in my function worth changing, in order, and here
  is why the risky one is not first."
- "That is a Tier 4 claim. Where is it grounded?"
- "This prompt has no refuse-to-guess clause, so I do not know what it made up."
- "I ran a defect report on the export before I trusted the total."
- "Who owns this on Monday morning when I am not here?"
- "That is Lane 3. The answer is no, and here is what we can do instead."

## Your 30-day commitment

You leave with a date and one workflow. Not five. One — from your own function,
scoring at least 8 on VFRR, sitting in Lane 1 or Lane 2, with a named owner who
is not you, and with a before-measurement you take **this week**, before you
build anything.

You will present it at the start of Module 2.

---

## Quick reference card

**Trust tiers.** T1 read it · T2 spot-check it · T3 verify the arithmetic ·
T4 ground it or don't answer · T0 don't.

**CRISP.** Context · Role · Inputs and source of truth · Steps and
refuse-to-guess · Product and acceptance criteria.

**VFRR.** Priority = (Volume + Friction + Readiness) − Risk.

**Three lanes.** Draft · Decide-support · Never.

**Before any analysis:** ask for the defect report first.

**Before any trust:** recompute the headline number a second way.

**Before any handover:** name the owner and write the failure behaviour.
