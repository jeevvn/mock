# arbitration/decision_engine.py

SCORE_MAP = {
    "low": 0.2,
    "medium": 0.5,
    "high": 0.8
}

def arbitrate(perspectives, weights):
    """
    Produces ONE escalation decision.
    """

    weighted_score = 0.0

    for p in perspectives:
        agent = p["agent"]
        concern = SCORE_MAP[p["concern_level"]]
        confidence = p.get("confidence", 0.5)

        weighted_score += concern * confidence * weights.get(agent, 0)

    # escalation thresholds
    if weighted_score >= 0.65:
        level = "HIGH"
    elif weighted_score >= 0.35:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "escalation_level": level,
        "score": round(weighted_score, 2)
    }

