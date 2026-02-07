def build_patient_input(age, sex, medications_text, labs_text, symptoms):
    medications = [m.strip().lower() for m in medications_text.split(",") if m.strip()]

    labs = {}
    for line in labs_text.split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            try:
                labs[key.strip().lower()] = float(value.strip())
            except ValueError:
                pass

    return {
        "age": age,
        "sex": sex,
        "medications": medications,
        "labs": labs,
        "symptoms": symptoms.strip()
    }

