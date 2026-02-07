import streamlit as st

# Member 1
from input_layer import build_patient_input

# Member 2
from lab_agent import analyze_labs
from med_agent import analyze_medications
from symptom_agent import analyze_symptoms

# ---------------- UI ----------------

st.set_page_config(page_title="Medical Escalation System")

st.title("🩺 Medical Risk Escalation Support")
st.warning("This is NOT a diagnostic system")

st.header("Patient Input")

age = st.number_input("Age", min_value=0, max_value=120, step=1)
sex = st.selectbox("Sex", ["male", "female", "other"])

medications_text = st.text_input(
    "Medications (comma-separated)",
    placeholder="e.g. metformin, atorvastatin"
)

labs_text = st.text_area(
    "Labs (one per line: key:value)",
    placeholder="hemoglobin: 11.2\nglucose: 180"
)

symptoms = st.text_area(
    "Symptoms",
    placeholder="Describe symptoms here"
)

# ---------------- ACTION ----------------

if st.button("Analyze"):

    # ✅ MEMBER 1: Structured input
    patient_input = build_patient_input(
        age, sex, medications_text, labs_text, symptoms
    )

    st.subheader("📦 Structured Input")
    st.json(patient_input)

    # ✅ MEMBER 2: Evidence agents
    lab_result = analyze_labs(patient_input["labs"])
    med_result = analyze_medications(patient_input["medications"])
    symptom_result = analyze_symptoms(patient_input["symptoms"])

    st.subheader("🔬 Evidence Results")
    st.json({
        "labs": lab_result,
        "medications": med_result,
        "symptoms": symptom_result
    })

    # Placeholder for later stages
    st.subheader("🚨 Final Escalation")
    st.info("Waiting for arbitration module")

    st.subheader("🧠 Explanation")
    st.write("Waiting for explainability module")
