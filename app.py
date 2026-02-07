from input_layer import build_patient_input
import streamlit as st
from input_layer import build_patient_input

st.set_page_config(page_title="Medical Escalation System")

st.title(" Medical Risk Escalation Support")
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

if st.button("Submit"):
    patient_input = build_patient_input(
        age, sex, medications_text, labs_text, symptoms
    )

    st.subheader("📦 Structured Input")
    st.json(patient_input)

    st.subheader("🚨 Final Escalation")
    st.info("Waiting for arbitration output")

    st.subheader("🧠 Explanation")
    st.write("Waiting for explainability module")



