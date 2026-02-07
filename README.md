🚑 TRIAGE-AI
Trust-Weighted Risk Interpretation & Escalation

TRIAGE-AI is a safety-first medical decision-support system that helps answer one critical question:

“How urgently should this medical situation be reviewed?”

Instead of diagnosing or prescribing, TRIAGE-AI focuses on triage and escalation — deciding when attention is needed, not what the condition is.

🧠 Why TRIAGE-AI?

Medical data is messy:

lab values without context

medications with hidden interactions

vague or overlapping symptoms

This often leads to:

🚨 unnecessary panic

😴 dangerous delays

TRIAGE-AI solves this by producing one clear, explainable escalation decision:

LOW → Monitor

MEDIUM → Medical review advised

HIGH → Seek urgent medical attention

✨ What Makes This Project Special

✅ Multi-agent reasoning (different risk perspectives)
✅ Adaptive trust weighting (context-aware, not static)
✅ Deterministic & explainable (no black box decisions)
✅ Safety-first design (no diagnosis, no treatment advice)

This is decision support, not decision replacement.

🔄 System Flow (High Level)
User Input
   ↓
Medical Evidence Agents (facts only)
   ↓
Perspective Agents (opinions)
   ↓
Meta Agent (who to trust more?)
   ↓
Arbitration (one escalation decision)
   ↓
Explainability (plain English output)


Each stage has one responsibility, making the system easy to explain, debug, and trust.

🧩 Architecture Overview
Level 0 – Input

Age, sex

Current medications

Selected lab values

Patient-reported symptoms
➡️ Normalized into JSON (no reasoning yet)

Level 1 – Medical Evidence Agents

Objective signal extraction:

Lab Analysis Agent

Medication Interaction Agent

Symptom Correlation Agent

❗ These agents do not communicate and do not interpret.

Level 2 – Perspective Agents

Three independent viewpoints:

Optimistic – assumes best reasonable case

Analytical – balances evidence & uncertainty

Pessimistic – prioritizes early risk detection

Each outputs:

concern level (low / medium / high)

confidence score

rationale

Level 3 – Meta Agent

Acts as a moderator, not a doctor.

Observes evidence severity

Detects agreement vs disagreement

Adjusts how much each perspective is trusted

Output: adaptive trust weights

Level 4 – Arbitration

The only decision-maker.

Converts concern → numeric score

Scales by confidence & trust

Aggregates into one risk score

Maps score → LOW / MEDIUM / HIGH

Also includes hard safety overrides for critical lab values.

Level 5 – Explainability

Outputs:

clear, human-readable reasoning

action-oriented recommendation

safety disclaimer

🛡️ Safety by Design

No diagnosis or treatment advice

Deterministic decision logic

Critical-value overrides (e.g., extreme labs)

Input sanity checks

LLMs (if used) restricted to interpretation only

🗂️ Project Structure
TRIAGE-AI/
│
├── app.py                  # Streamlit app (orchestration only)
├── explainability.py
│
├── evidence/               # Level 1
├── perspectives/           # Level 2
├── meta/                   # Level 3
├── arbitration/            # Level 4
│
├── tests/
│   └── run_meta_pipeline.py
│
└── README.md

▶️ How to Run (Demo-Ready)
1️⃣ Install dependencies
pip install streamlit

2️⃣ Run logic validation (Levels 3–5)
python tests/run_meta_pipeline.py

3️⃣ Launch the app
streamlit run app.py

🧪 Sample Output
Escalation Level: MEDIUM
Explanation: Some information is outside the normal range, but does not suggest an emergency.
Recommended Action: Medical review advised.

🚀 Use Cases

Patient-facing triage assistance

Clinical prioritization support

Medication interaction awareness

Remote health monitoring

Safe medical AI demos

🏁 One-Line Pitch (Hackathon Ready)

TRIAGE-AI is a trust-weighted, multi-agent medical escalation system that safely determines urgency without diagnosing or treating.

⚠️ Disclaimer

TRIAGE-AI does not provide medical advice, diagnosis, or treatment recommendations.
It is intended solely to support escalation and prioritization decisions.
