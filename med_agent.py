# Level 1B: Medication Interaction Agent
# evidence/med_agent.py

MED_SIDE_EFFECTS = {
    "statin": ["muscle pain", "fatigue"],
    "metformin": ["nausea", "diarrhea"],
    "amlodipine": ["ankle swelling", "headache"]
}

def analyze_medications(medications):
    flags = []

    for med in medications:
        med_lower = med.lower()
        for known_med, effects in MED_SIDE_EFFECTS.items():
            if known_med in med_lower:
                flags.append(f"{med} may cause {', '.join(effects)}")

    severity = "low" if not flags else "moderate"

    return {
        "flags": flags,
        "severity": severity
    }
