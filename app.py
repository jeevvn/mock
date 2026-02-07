import streamlit as st
from evidence.lab_agent import analyze_labs
from evidence.med_agent import analyze_medications
from evidence.symptom_agent import analyze_symptoms

st.title("Medical Escalation Support System")

# --- UI inputs ---
age = st.number_input("Age", 0, 120)
sex = st.selectbox("Sex", ["male", "female"])

meds = st.text_input("Medications (comma-separated)")
labs = st.text_input("Labs (e.g. hb:9,wbc:8000)")
symptoms = st.text_area("Symptoms")

if st.button("Analyze"):
    meds_list = [m.strip() for m in meds.split(",") if m.strip()]
    labs_dict = {
        k: float(v) for k, v in
        (item.split(":") for item in labs.split(","))
    }

    # 🔥 MEMBER 2 CALLED HERE
    lab_result = analyze_labs(labs_dict)
    med_result = analyze_medications(meds_list)
    symptom_result = analyze_symptoms(symptoms)

    st.subheader("Evidence Results")
    st.json({
        "labs": lab_result,
        "medications": med_result,
        "symptoms": symptom_result
    })
