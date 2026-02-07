# Level 1C: Symptom Correlation Agent
# evidence/symptom_agent.py

SYMPTOM_MAP = {
    "chest pain": "cardiac-related symptom",
    "shortness of breath": "respiratory-related symptom",
    "dizziness": "neurological-related symptom",
    "vomiting": "gastrointestinal-related symptom"
}

def analyze_symptoms(symptom_text):
    flags = []
    text = symptom_text.lower()

    for symptom, note in SYMPTOM_MAP.items():
        if symptom in text:
            flags.append(f"{symptom} detected ({note})")

    if len(flags) == 0:
        severity = "low"
    elif len(flags) == 1:
        severity = "moderate"
    else:
        severity = "high"

    return {
        "flags": flags,
        "severity": severity
    }
