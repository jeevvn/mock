# Level 1A: Lab Analysis Agent
# evidence/lab_agent.py

# Hardcoded normal ranges
LAB_RANGES = {
    "hb": (12, 16),
    "wbc": (4000, 11000),
    "platelets": (150000, 450000),
    "glucose": (70, 140)
}

def analyze_labs(labs):
    flags = []
    severity = "low"

    for lab, value in labs.items():
        if lab not in LAB_RANGES:
            continue

        low, high = LAB_RANGES[lab]

        if value < low or value > high:
            flags.append(f"{lab} abnormal: {value}")
            severity = "moderate"

            if value < low * 0.7 or value > high * 1.3:
                severity = "high"

    return {
        "flags": flags,
        "severity": severity
    }
