"""Generate the synthetic Meridian Group of Schools datasets used by the
AI Transformation Lead training programme. Deterministic (fixed seed).

The data is deliberately imperfect: inconsistent casing, mixed date formats,
Indian-format numbers, duplicates, blanks. Cleaning it is part of the training.
"""
import csv
import os
import random
from datetime import date, timedelta

random.seed(20260908)

OUT = os.path.join(os.path.dirname(__file__), "out")
os.makedirs(OUT, exist_ok=True)

CAMPUSES = [
    "Andheri", "Powai", "Thane", "Kalyan", "Pune-Baner", "Pune-Wakad",
    "Nashik", "Nagpur", "Ahmedabad-Bopal", "Surat", "Vadodara",
    "Bengaluru-Whitefield", "Hubballi", "Indore",
]
# Campus name variants, so participants must normalise before joining datasets.
CAMPUS_VARIANTS = {
    "Pune-Baner": ["Pune-Baner", "Pune - Baner", "PUNE BANER", "Pune Baner"],
    "Pune-Wakad": ["Pune-Wakad", "Pune - Wakad", "Pune Wakad"],
    "Ahmedabad-Bopal": ["Ahmedabad-Bopal", "Ahmedabad Bopal", "A'bad-Bopal"],
    "Bengaluru-Whitefield": ["Bengaluru-Whitefield", "Bangalore-Whitefield",
                             "Bengaluru Whitefield"],
    "Andheri": ["Andheri", "Andheri ", "andheri"],
}


def campus_variant(c):
    return random.choice(CAMPUS_VARIANTS.get(c, [c]))


FIRST_M = ["Aarav", "Vivaan", "Rohan", "Karthik", "Siddharth", "Imran", "Nikhil",
           "Pranav", "Aditya", "Rahul", "Yash", "Manish", "Sameer", "Vikram",
           "Devendra", "Joseph", "Harish", "Anil", "Tarun", "Faisal"]
FIRST_F = ["Ananya", "Diya", "Meera", "Sneha", "Kavita", "Priya", "Fatima",
           "Shalini", "Nandini", "Rupal", "Aisha", "Deepa", "Trupti", "Neha",
           "Gauri", "Reshma", "Lakshmi", "Vaishali", "Ritu", "Sarah"]
LAST = ["Sharma", "Iyer", "Deshpande", "Nair", "Patel", "Khan", "Reddy", "Joshi",
        "Kulkarni", "Menon", "Bhatt", "Rao", "Shetty", "Mehta", "Gowda",
        "Chatterjee", "Pillai", "Sinha", "Verma", "D'Souza", "Kaur", "Bose"]


def person(gender=None):
    g = gender or random.choice("mf")
    f = random.choice(FIRST_M if g == "m" else FIRST_F)
    return f"{f} {random.choice(LAST)}"


def d(dt, fmt="%Y-%m-%d"):
    return dt.strftime(fmt)


def inr(n):
    """Indian-format a number, e.g. 125000 -> 1,25,000."""
    s = str(int(n))
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:])
        head = head[:-2]
    if head:
        parts.insert(0, head)
    return ",".join(parts) + "," + tail


def write(name, header, rows):
    p = os.path.join(OUT, name)
    with open(p, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(rows)
    print(f"{name}: {len(rows)} rows")


# ---------------------------------------------------------------- HR roster
DEPTS = {
    "Academic": [("PRT", 4.2, 6.4), ("TGT", 5.4, 8.2), ("PGT", 7.0, 11.5),
                 ("Coordinator", 8.5, 13.0), ("Vice Principal", 12.0, 18.0),
                 ("Principal", 18.0, 28.0)],
    "Administration": [("Admin Executive", 3.0, 5.2), ("Front Office", 2.6, 4.0),
                       ("Admin Manager", 6.5, 10.0)],
    "Accounts": [("Accounts Assistant", 3.0, 4.8), ("Accountant", 4.5, 7.5),
                 ("Accounts Manager", 8.0, 13.0)],
    "Marketing": [("Admission Counsellor", 3.2, 5.6),
                  ("Marketing Executive", 4.0, 7.0),
                  ("Regional Marketing Manager", 9.0, 15.0)],
    "Purchase": [("Purchase Assistant", 3.0, 4.6),
                 ("Purchase Officer", 5.0, 8.0)],
    "Support": [("Lab Assistant", 2.4, 3.6), ("Librarian", 3.2, 5.0),
                ("Sports Coach", 3.4, 5.8), ("Housekeeping Supervisor", 2.2, 3.4)],
}
SUBJECTS = ["English", "Mathematics", "Science", "Social Studies", "Hindi",
            "Marathi", "Computer Science", "Physics", "Chemistry", "Biology",
            "Economics", "Commerce", "Physical Education", "Art", ""]
QUALS = ["B.Ed, B.A.", "B.Ed, B.Sc.", "M.A., B.Ed", "M.Sc., B.Ed", "M.Com",
         "B.Com", "MBA", "M.Ed", "D.El.Ed", "B.P.Ed", "M.A."]

hr_rows = []
for i in range(1, 91):
    campus = random.choice(CAMPUSES)
    dept = random.choices(list(DEPTS), weights=[55, 12, 8, 10, 5, 10])[0]
    desig, lo, hi = random.choice(DEPTS[dept])
    doj = date(2016, 1, 1) + timedelta(days=random.randint(0, 3500))
    ctc = round(random.uniform(lo, hi) * 100000, -2)
    emp_type = random.choices(["Permanent", "Probation", "Contract", "Visiting"],
                              weights=[62, 18, 15, 5])[0]
    conf = "Confirmed" if emp_type == "Permanent" else (
        "Pending" if emp_type == "Probation" else "N/A")
    rating = random.choice(["A", "A", "B", "B", "B", "C", "C", "D", ""])
    name = person()
    # Deliberate dirt
    doj_str = d(doj)
    if i % 11 == 0:
        doj_str = d(doj, "%d/%m/%Y")
    if i % 17 == 0:
        doj_str = d(doj, "%d-%b-%y")
    if i % 23 == 0:
        doj_str = ""
    ctc_str = str(int(ctc))
    if i % 9 == 0:
        ctc_str = inr(ctc)
    if i % 29 == 0:
        ctc_str = ""
    email = (name.lower().replace(" ", ".").replace("'", "")
             + f"@meridianschools.example.in")
    hr_rows.append([
        f"MGS-{1000 + i}", name if i % 13 else f"  {name} ",
        campus_variant(campus), dept, desig,
        random.choice(["G3", "G4", "G5", "G6", "G7"]),
        doj_str, emp_type, random.choice(QUALS),
        random.choice(SUBJECTS) if dept == "Academic" else "",
        ctc_str, conf, rating, email,
    ])
# Duplicate employee (same person, two IDs) - a real data-quality trap
dup = list(hr_rows[7])
dup[0] = "MGS-1207"
dup[2] = campus_variant(CAMPUSES[0])
hr_rows.append(dup)

write("hr_staff_roster.csv",
      ["emp_id", "employee_name", "campus", "department", "designation", "grade",
       "date_of_joining", "employment_type", "qualification", "subject_taught",
       "ctc_annual_inr", "confirmation_status", "last_appraisal_rating",
       "official_email"], hr_rows)

# ------------------------------------------------------------- Fee ledger
GRADES = ["Nursery", "Jr KG", "Sr KG"] + [f"Grade {n}" for n in range(1, 13)]
CONCESSION = ["", "", "", "", "Sibling-10%", "Staff Ward-50%", "RTE",
              "Merit Scholarship-25%", "Management Concession"]
fee_rows = []
for i in range(1, 141):
    campus = random.choice(CAMPUSES)
    grade = random.choice(GRADES)
    base = {"Nursery": 78000, "Jr KG": 82000, "Sr KG": 86000}.get(grade)
    if base is None:
        n = int(grade.split()[1])
        base = 92000 + n * 4200
    term = random.choice(["Term 1", "Term 1", "Term 2", "Term 3"])
    # Due dates are staggered per student (instalment plans, late admissions,
    # campus-wise circulars) so the ageing buckets spread realistically.
    due = (date(2026, {"Term 1": 4, "Term 2": 8, "Term 3": 11}[term], 10)
           + timedelta(days=random.randint(0, 75)))
    amount = round(base / 3, -2)
    conc = random.choice(CONCESSION)
    if "10%" in conc:
        amount *= 0.9
    elif "50%" in conc:
        amount *= 0.5
    elif "25%" in conc:
        amount *= 0.75
    elif conc == "RTE":
        amount = 0
    amount = round(amount, -1)
    paid_state = random.choices(["full", "part", "none"], weights=[64, 14, 22])[0]
    paid = amount if paid_state == "full" else (
        round(amount * random.uniform(0.2, 0.7), -1) if paid_state == "part" else 0)
    bal = round(amount - paid, 2)
    today = date(2026, 9, 8)
    overdue = max(0, (today - due).days) if bal > 0 else 0
    amt_str = str(int(amount))
    if i % 12 == 0:
        amt_str = inr(amount)
    fee_rows.append([
        f"STU-{20260000 + i}", person(), campus_variant(campus), grade,
        random.choice("ABC"), term, d(due - timedelta(days=15)), d(due),
        amt_str, int(paid), int(bal), overdue,
        random.choice(["UPI", "NEFT", "Cheque", "Cash", "Card", "Payment Gateway", ""]),
        conc,
        random.choice(["WhatsApp", "SMS", "Email", "Call"]),
        random.choice(["", "", "", "Parent requested instalment",
                       "Cheque bounced - charges pending",
                       "Awaiting employer reimbursement",
                       "Disputed transport component"]),
    ])
# Traps: a duplicate invoice row, and a credit balance
fee_rows.append(list(fee_rows[3]))
credit = list(fee_rows[10])
credit[9] = int(credit[8].replace(",", "")) + 5000
credit[10] = -5000
credit[11] = 0
fee_rows.append(credit)

write("accounts_fee_ledger.csv",
      ["student_id", "student_name", "campus", "grade", "section", "term",
       "invoice_date", "due_date", "amount_due_inr", "amount_paid_inr",
       "balance_inr", "days_overdue", "payment_mode", "concession_type",
       "parent_contact_preference", "remarks"], fee_rows)

# --------------------------------------------------------- Purchase quotes
ITEMS = [
    ("LAB-DSK", "Science laboratory work table, 6ft, acid-resistant top", "No", 12),
    ("LAB-STL", "Laboratory stool, adjustable height, SS frame", "No", 72),
    ("LAB-FUM", "Fume hood, benchtop, 3ft with exhaust", "No", 2),
    ("LAB-MIC", "Compound microscope, 1000x, LED, binocular", "No", 20),
    ("LAB-GLW", "Borosilicate glassware assorted set (48 pcs)", "Set", 8),
    ("CLS-BEN", "Classroom desk-bench unit, 2-seater, powder coated", "No", 120),
    ("CLS-BRD", "Ceramic whiteboard 8ft x 4ft, magnetic", "No", 24),
    ("CLS-CHR", "Teacher chair, mid-back, revolving", "No", 24),
    ("LIB-RCK", "Library rack, double-sided, 7 shelf, MS", "No", 16),
    ("IT-PROJ", "Interactive flat panel display 75 inch, Android 13", "No", 10),
    ("IT-UPS", "Online UPS 3kVA with 30 min backup", "No", 4),
    ("SFT-EXT", "ABC fire extinguisher 6kg with wall bracket", "No", 30),
]
VENDORS = [
    ("Q-2026-101", "Sahyadri Lab Systems Pvt Ltd", 1.00, 21, 24, "50% advance, 50% on delivery"),
    ("Q-2026-102", "Nirmal Edu-Infra LLP", 0.91, 35, 12, "30% advance, 60% on delivery, 10% after 60 days"),
    ("Q-2026-103", "Crescent Scientific & Furniture Co.", 1.07, 14, 36, "100% on delivery"),
    ("Q-2026-104", "Bluewave Edutech Supplies", 0.86, 45, 12, "40% advance, balance in 3 instalments"),
]
BASE_RATE = {
    "LAB-DSK": 18500, "LAB-STL": 1450, "LAB-FUM": 62000, "LAB-MIC": 9800,
    "LAB-GLW": 7400, "CLS-BEN": 4950, "CLS-BRD": 6200, "CLS-CHR": 4300,
    "LIB-RCK": 11800, "IT-PROJ": 92000, "IT-UPS": 41000, "SFT-EXT": 2350,
}
# Vendor-specific wording for the same item, so a naive match fails.
ALT_DESC = {
    "LAB-DSK": {2: "Lab table (6 feet) with chemical resistant top",
                3: "Science Lab Work Bench 6' acid proof"},
    "IT-PROJ": {1: "Interactive Flat Panel 75\" (Android)",
                3: "75 inch smart interactive panel, Android"},
    "CLS-BEN": {2: "Desk cum bench, two seater, MS powder coated"},
}
q_rows = []
for vi, (qid, vname, mult, days, warr, terms) in enumerate(VENDORS):
    for code, desc, unit, qty in ITEMS:
        # Vendor 4 skips two items (incomplete quote - a scoring trap)
        if vi == 3 and code in ("LAB-FUM", "IT-UPS"):
            continue
        rate = round(BASE_RATE[code] * mult * random.uniform(0.96, 1.05), -1)
        gst = 18 if code.startswith(("IT-", "LAB-MIC")) else 12
        # Vendor 2 quotes GST-inclusive without saying so in a separate column
        basis = "Exclusive of GST"
        if vi == 1:
            basis = "Inclusive of GST"
            rate = round(rate * (1 + gst / 100), -1)
        q_qty = qty
        if vi == 2 and code == "CLS-BEN":
            q_qty = 100  # under-quoted quantity
        q_rows.append([
            qid, vname, d(date(2026, 8, random.randint(18, 28))), code,
            ALT_DESC.get(code, {}).get(vi, desc), unit, q_qty,
            int(rate), gst, basis, days, warr, terms,
            random.choice(["Mumbai", "Pune", "Ahmedabad", "Bengaluru"]),
        ])

write("purchase_vendor_quotations.csv",
      ["quotation_id", "vendor_name", "quotation_date", "item_code",
       "item_description", "unit", "quantity_quoted", "unit_rate_inr", "gst_pct",
       "rate_basis", "delivery_days", "warranty_months", "payment_terms",
       "vendor_location"], q_rows)

write("purchase_requisition.csv",
      ["item_code", "item_description", "unit", "quantity_required",
       "required_by_date", "indenting_campus", "budget_head"],
      [[c, desc, u, q, "2026-11-15", "Pune-Baner",
        "CAPEX-2026-27 / Science Block Phase 2"] for c, desc, u, q in ITEMS])

# ------------------------------------------------------ Marketing enquiries
# Each campus runs one of three funnel profiles. The profile is NEVER written to
# the data - it is only in the facilitator answer key. It drives ad spend, source
# mix and follow-up discipline, so the "spend more, admit fewer" finding is a real
# property of the numbers rather than something asserted in the brief.
PROFILE = {c: "average" for c in CAMPUSES}
for c in ("Hubballi", "Nagpur", "Surat"):
    PROFILE[c] = "paid-heavy"       # big budgets, weak follow-up
for c in ("Kalyan", "Vadodara", "Thane"):
    PROFILE[c] = "referral-led"     # small budgets, strong follow-up

SOURCE_MIX = {
    "referral-led": [("Referral", 20), ("Alumni", 12), ("Walk-in", 12),
                     ("School Website", 10), ("Google Ads", 18), ("Meta Ads", 16),
                     ("Hoarding", 6), ("Education Fair", 4), ("Justdial", 2)],
    "average":      [("Referral", 11), ("Alumni", 6), ("Walk-in", 8),
                     ("School Website", 8), ("Google Ads", 25), ("Meta Ads", 21),
                     ("Hoarding", 10), ("Education Fair", 6), ("Justdial", 5)],
    "paid-heavy":   [("Referral", 3), ("Alumni", 1), ("Walk-in", 4),
                     ("School Website", 6), ("Google Ads", 30), ("Meta Ads", 26),
                     ("Hoarding", 14), ("Education Fair", 8), ("Justdial", 8)],
}
FOLLOWUP_DIST = {   # weights for follow-up counts 0..6
    "referral-led": [4, 8, 16, 22, 22, 16, 12],
    "average":      [14, 20, 22, 18, 13, 8, 5],
    "paid-heavy":   [38, 28, 16, 9, 5, 3, 1],
}
VOLUME = {"referral-led": 0.85, "average": 1.0, "paid-heavy": 1.25}
SPEND_MULT = {"referral-led": 0.55, "average": 1.0, "paid-heavy": 1.9}
SOURCE_BONUS = {"Referral": 0.10, "Alumni": 0.09, "Walk-in": 0.07,
                "School Website": 0.03, "Education Fair": 0.0, "Google Ads": 0.0,
                "Meta Ads": -0.01, "Hoarding": -0.02, "Justdial": -0.03}
LOST_REASON = ["Fee too high", "Distance / transport", "Chose competitor school",
               "Relocating", "Wanted ICSE board", "No seat in required grade",
               "Parent unresponsive"]
LOCALITY = ["Baner", "Aundh", "Hinjewadi", "Powai", "Chandivali", "Ghodbunder Rd",
            "Bopal", "Whitefield", "Kalyan West", "Wakad", "Satpur", "Alkapuri",
            "Gotri", "Vesu", "Sadar", "Vijayanagar"]

counsellors = {c: [person("f") for _ in range(3)] for c in CAMPUSES}
enq_rows, eid = [], 5000
for campus in CAMPUSES:
    prof = PROFILE[campus]
    n = int(170 * VOLUME[prof] * random.uniform(0.88, 1.12))
    names, weights = zip(*SOURCE_MIX[prof])
    for _ in range(n):
        eid += 1
        src = random.choices(names, weights=weights)[0]
        followups = random.choices(range(7), weights=FOLLOWUP_DIST[prof])[0]
        p = 0.015 + 0.055 * min(followups, 4) + SOURCE_BONUS[src]
        p = max(0.01, min(0.62, p))
        dt = date(2026, 5, 1) + timedelta(days=random.randint(0, 122))
        if random.random() < p:
            st = "Admitted"
        elif followups == 0:
            st = random.choices(["New", "Not Reachable", "Contacted", "Lost"],
                                weights=[30, 34, 20, 16])[0]
        else:
            st = random.choices(
                ["Contacted", "Visit Scheduled", "Visited",
                 "Application Started", "Lost", "Not Reachable"],
                weights=[24, 14, 16, 9, 32, 5])[0]
        # Source casing is inconsistent in the CRM export - normalising it is
        # the difference between a correct and a doubled channel report.
        src_out = src.lower() if (src in ("Google Ads", "Meta Ads")
                                  and random.random() < 0.4) else src
        last = dt + timedelta(days=random.randint(1, 45))
        enq_rows.append([
            f"ENQ-{eid}", d(dt) if random.random() > 0.05 else "",
            campus_variant(campus), src_out, random.choice(GRADES[:10]),
            person(), random.choice(LOCALITY), random.choice(counsellors[campus]),
            st, followups, d(last) if st != "New" else "",
            random.choice(LOST_REASON) if st == "Lost" else "",
            random.choice(["WhatsApp", "Call", "Email"]),
        ])
random.shuffle(enq_rows)

write("marketing_admission_enquiries.csv",
      ["enquiry_id", "enquiry_date", "campus", "source", "grade_sought",
       "parent_name", "locality", "counsellor", "status", "followup_count",
       "last_contact_date", "lost_reason", "preferred_channel"], enq_rows)

spend_rows = []
for campus in CAMPUSES:
    mult = SPEND_MULT[PROFILE[campus]]
    for mn in ["May-2026", "Jun-2026", "Jul-2026", "Aug-2026"]:
        for ch, lo, hi in [("Google Ads", 8000, 20000), ("Meta Ads", 7000, 18000),
                           ("Hoarding", 0, 40000), ("Education Fair", 0, 15000),
                           ("Print", 0, 10000)]:
            amt = random.uniform(lo, hi) * mult
            spend_rows.append([campus, mn, ch, int(amt // 100 * 100)])

write("marketing_channel_spend.csv",
      ["campus", "month", "channel", "spend_inr"], spend_rows)

# ------------------------------------------------------------- Academic
ac_rows = []
teachers = {c: [person() for _ in range(4)] for c in CAMPUSES}
# Planted anomaly (facilitator key only): one Surat teacher's marks are uniformly
# high and uncorrelated with attendance - visible only if you segment by teacher.
INFLATOR = teachers["Surat"][0]
for i in range(1, 421):
    campus = random.choice(CAMPUSES)
    grade = random.choice([f"Grade {n}" for n in range(3, 11)])
    subj = random.choice(["English", "Mathematics", "Science", "Social Studies",
                          "Hindi"])
    att = round(random.uniform(58, 99), 1)
    teacher = random.choice(teachers[campus])
    if teacher == INFLATOR:
        marks = round(random.uniform(86, 98))
    else:
        # Marks loosely correlated with attendance, plus noise
        marks = max(4, min(100, round(22 + (att - 58) * 1.5 + random.gauss(0, 11))))
    ac_rows.append([
        f"STU-{20260000 + random.randint(1, 140)}", campus_variant(campus), grade,
        random.choice("ABC"), subj,
        random.choice(["Unit Test 1", "Term 1 Exam", "Unit Test 2"]),
        100, marks, att, teacher,
    ])

write("academic_assessment_results.csv",
      ["student_id", "campus", "grade", "section", "subject", "assessment",
       "max_marks", "marks_obtained", "attendance_pct", "teacher"], ac_rows)

print("done ->", OUT)
