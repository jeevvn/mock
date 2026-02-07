# 🚑 **TRIAGE-AI**

### *Trust-Weighted Risk Interpretation & Escalation*

---

### ❓ What problem does TRIAGE-AI solve?

**TRIAGE-AI** is a **safety-first medical decision-support system** built to answer one focused question:

> **“How urgently should this medical situation be reviewed?”**

Instead of diagnosing diseases or prescribing treatments, TRIAGE-AI focuses purely on **triage and escalation** — deciding **when** attention is needed, not **what** the condition is.

---

## 🧠 Why TRIAGE-AI?

Medical data is often **fragmented and confusing**:

* 📊 Lab values without context
* 💊 Medications with hidden interactions
* 🗣️ Vague or overlapping symptoms

This commonly results in:

* 🚨 **Unnecessary panic** and alert fatigue
* 😴 **Dangerous delays** in identifying early risk

---

## 🎯 Our Solution

TRIAGE-AI transforms scattered medical inputs into **one clear, explainable escalation decision**:

| Escalation Level | Meaning                       |
| ---------------- | ----------------------------- |
| 🟢 **LOW**       | Monitor                       |
| 🟡 **MEDIUM**    | Medical review advised        |
| 🔴 **HIGH**      | Seek urgent medical attention |

This keeps decisions **clear, calm, and actionable**.

---

## ✨ What Makes TRIAGE-AI Special

✅ **Multi-agent reasoning** — multiple risk perspectives
✅ **Adaptive trust weighting** — context-aware, not static
✅ **Deterministic & explainable** — no black-box decisions
✅ **Safety-first design** — no diagnosis, no treatment advice

> ⚠️ This is **decision support**, not decision replacement.

---

## 🔄 System Flow (High Level)

```
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
Explainability (plain-English output)
```

Each stage has **one responsibility**, making the system easy to:

* explain
* debug
* trust

---

## 🧩 Architecture Overview

### 🔹 Level 0 — Input

Collected information:

* Age, sex
* Current medications
* Selected lab values
* Patient-reported symptoms

➡️ Normalized into structured JSON
➡️ **No reasoning happens here**

---

### 🔹 Level 1 — Medical Evidence Agents

Objective signal extraction only:

* 🧪 **Lab Analysis Agent**
* 💊 **Medication Interaction Agent**
* 🩺 **Symptom Correlation Agent**

❗ These agents **do not communicate**
❗ They **do not interpret or judge**

---

### 🔹 Level 2 — Perspective Agents

Independent risk viewpoints:

* 😊 **Optimistic** — assumes best reasonable case
* ⚖️ **Analytical** — balances evidence & uncertainty
* 🚨 **Pessimistic** — prioritizes early risk detection

Each outputs:

* concern level *(low / medium / high)*
* confidence score
* rationale

---

### 🔹 Level 3 — Meta Agent

Acts as a **moderator**, not a doctor.

* Observes evidence severity
* Detects agreement vs disagreement
* Adjusts how much each perspective is trusted

➡️ Output: **adaptive trust weights**

---

### 🔹 Level 4 — Arbitration

The **only decision-maker**.

* Converts concern → numeric scores
* Scales by confidence & trust
* Aggregates into one risk score
* Maps score → **LOW / MEDIUM / HIGH**

⚠️ Includes **hard safety overrides** for critical lab values

---

### 🔹 Level 5 — Explainability

Produces:

* 🗣️ Clear, human-readable reasoning
* 🎯 Action-oriented recommendation
* 🛡️ Mandatory safety disclaimer

---

## 🛡️ Safety by Design

* No diagnosis or treatment advice
* Deterministic decision logic
* Critical-value overrides (e.g., extreme labs)
* Input sanity checks
* LLMs (if used) restricted to interpretation layers only

---

## 🗂️ Project Structure

```
TRIAGE-AI/
│
├── app.py                  # Streamlit orchestration layer
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
```

---

## ▶️ How to Run (Demo-Ready)

### 1️⃣ Install dependencies

```bash
pip install streamlit
```

### 2️⃣ Validate core logic (Levels 3–5)

```bash
python tests/run_meta_pipeline.py
```

### 3️⃣ Launch the application

```bash
streamlit run app.py
```

---

## 🧪 Sample Output

```
Escalation Level: MEDIUM
Explanation: Some information is outside the normal range, but does not suggest an emergency.
Recommended Action: Medical review advised.
```

---

## 🚀 Use Cases

* 🧑‍⚕️ Patient-facing triage assistance
* 🏥 Clinical prioritization support
* 💊 Medication interaction awareness
* 📡 Remote health monitoring
* 🧪 Safe medical AI demonstrations

---

## 🏁 One-Line Pitch (Hackathon Ready)

> **TRIAGE-AI is a trust-weighted, multi-agent medical escalation system that safely determines urgency without diagnosing or treating.**

---

## ⚠️ Disclaimer

TRIAGE-AI does **not** provide medical advice, diagnosis, or treatment recommendations.
It is intended solely to support **escalation and prioritization decisions**.

