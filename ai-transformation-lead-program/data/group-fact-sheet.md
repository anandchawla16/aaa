# Meridian Group of Schools — Group Fact Sheet

> **This is a fictional school group.** Every name, campus, employee, student,
> vendor and figure in this training pack is synthetic. It is built to behave
> like a real mid-sized Indian K–12 group so that exercises are realistic, but
> nothing here describes a real organisation or a real person. Do not use it as
> a benchmark. In Module 5 you replace it with your own group's data under your
> own governance rules.

---

## 1. The group at a glance

| Item | Detail |
|---|---|
| Legal form | Meridian Education Trust (registered public charitable trust) + Meridian Edu Services Pvt Ltd (shared services) |
| Founded | 2004 |
| Campuses | 14 |
| States | Maharashtra (7), Gujarat (3), Karnataka (2), Madhya Pradesh (1), + 1 upcoming |
| Boards | CBSE (10 campuses), State Board (3), IB PYP (1 — Bengaluru-Whitefield) |
| Grades | Nursery to Grade 12 (Grade 11–12 at 6 campuses only) |
| Students | ~18,400 |
| Staff | ~1,650 (approx. 1,180 academic, 470 non-academic) |
| Academic year | April to March |
| Annual fee range | ₹78,000 (Nursery) to ₹1,42,000 (Grade 12), campus-dependent |

### Campuses

| Campus | State | Board | Approx. students | Opened |
|---|---|---|---|---|
| Andheri | MH | CBSE | 1,850 | 2004 |
| Powai | MH | CBSE | 1,610 | 2006 |
| Thane | MH | CBSE | 1,540 | 2008 |
| Kalyan | MH | State | 1,120 | 2009 |
| Pune-Baner | MH | CBSE | 1,700 | 2010 |
| Pune-Wakad | MH | CBSE | 1,430 | 2013 |
| Nashik | MH | CBSE | 1,090 | 2014 |
| Nagpur | MH | State | 980 | 2015 |
| Ahmedabad-Bopal | GJ | CBSE | 1,260 | 2016 |
| Surat | GJ | CBSE | 1,150 | 2017 |
| Vadodara | GJ | State | 890 | 2018 |
| Bengaluru-Whitefield | KA | IB PYP | 820 | 2019 |
| Hubballi | KA | CBSE | 1,060 | 2021 |
| Indore | MP | CBSE | 1,900 | 2022 |

---

## 2. How the group is organised

**Group Office (Andheri, Mumbai)** holds five shared-service functions. Every
campus has a local counterpart who reports to the Principal on a solid line and
to the Group function head on a dotted line. This *dotted-line tension* is the
single biggest source of process friction in the group, and it will show up in
almost every exercise you do.

| Function | Group head | At campus | Headcount (group + campus) |
|---|---|---|---|
| **HR** | Group HR Head | HR Executive / Admin Manager | 6 + 14 |
| **Academics** | Group Academic Director | Principal, Vice Principal, Coordinators | 4 + 62 |
| **Accounts** | Group CFO | Campus Accountant | 8 + 21 |
| **Purchase** | Group Purchase Head | Purchase Assistant (7 campuses only) | 5 + 7 |
| **Marketing & Admissions** | Group Marketing Head | Admission Counsellors | 5 + 38 |

**Decision rights that matter for AI work**

| Decision | Who signs |
|---|---|
| Appointment / promotion of academic staff | Principal recommends → Group HR Head approves → Trustee signs above ₹9L CTC |
| Fee concession beyond published slabs | Campus Accountant recommends → Group CFO approves |
| Capital purchase above ₹2,00,000 | Three quotes → Purchase Committee → Trustee |
| Marketing spend reallocation between campuses | Group Marketing Head |
| Any communication to a parent on a disciplinary or safeguarding matter | Principal only. Never delegated, never automated. |

---

## 3. Systems in use

| System | Used for | Export format | Known problem |
|---|---|---|---|
| ERP (Vidyalaya-class SIS) | Admissions, fees, attendance, marks | CSV / XLSX | Campus names entered free-text; no validation |
| Payroll (third-party) | Salary, PF, TDS | XLSX | Not linked to ERP employee IDs |
| Tally | Books of account | XLSX / PDF | Ledger heads differ across campuses |
| Google Workspace | Mail, Drive, Forms | Native | Campus drives not consistently shared with Group |
| WhatsApp Business | Parent communication | Manual copy-paste | No structured record; the real "system of record" for many requests |
| Manual registers | Purchase indents at 7 campuses | Paper / photo | Not searchable |

> **The honest picture:** the group's data is not clean, not joined and not
> centralised. An AI Transformation Lead who assumes otherwise will design
> solutions that fail on contact. Every dataset in this pack is deliberately as
> messy as the real exports.

---

## 4. Group priorities for the current year

Set by the Board in April 2026. Your AI transformation work will be judged
against these, not against how clever the technology is.

1. **Fill rate.** Move group-wide seat fill from 86% to 92%. Admissions is the
   binding constraint at 5 campuses; 3 campuses are at capacity.
2. **Fee realisation.** Cut overdue fee balance at any point in the year by 40%.
   Current collection effort is manual, inconsistent, and escalates too late.
3. **Teacher retention.** Academic attrition is 19% annually; target 13%.
   Exit interviews point at workload and slow HR response, not pay.
4. **Cost per admission.** Marketing spend rose 34% year on year while
   admissions rose 9%. The Board wants the gap explained and closed.
5. **Procurement discipline.** Three-quote compliance is at 61%. Two campuses
   were flagged in the last audit for single-source purchases.
6. **Teacher time.** Reduce documented administrative load on teachers by
   4 hours per week — the single most requested change in the staff survey.

---

## 5. Constraints you must design within

- **Data residency and consent.** Student data is governed by the group's
  privacy policy and DPDP Act obligations. Parent contact details may not be
  pasted into any system that is not on the approved list.
- **No autonomous outbound communication.** Nothing reaches a parent, a
  candidate, a vendor or a regulator without a named human approving that exact
  text. This is a Board rule, not a preference.
- **Audit trail.** Anything that influences a financial, employment or
  admission decision must be reconstructible: what data, what prompt, what
  output, who approved.
- **Low technical capacity at campuses.** The average campus has no one who can
  maintain a script. Whatever you build must survive being handed to an
  administrator who has never seen a terminal.
- **Budget reality.** There is no line item for AI tooling this year. Value has
  to be demonstrated on existing licences before anything is funded.
