# explainability.py

def generate_explanation(decision, perspectives):
    level = decision["escalation_level"]

    if level == "LOW":
        message = (
            "The available information does not show signs that need immediate attention. "
            "Monitoring the situation for now is reasonable."
        )

    elif level == "MEDIUM":
        message = (
            "Some of the information is outside the normal range, but it does not clearly "
            "suggest an urgent problem. Because of this uncertainty, a medical review is advised."
        )

    else:  # HIGH
        message = (
            "Several findings raise concern and may indicate a developing issue. "
            "Seeking medical attention promptly is recommended."
        )

    explanation = {
        "summary": message,
        "details": [
            p["rationale"] for p in perspectives
        ],
        "disclaimer": (
            "This system does not provide diagnosis or treatment advice. "
            "It is intended only to support decisions about medical escalation."
        )
    }

    return explanation
