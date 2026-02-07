# meta/meta_agent.py

def compute_agent_weights(evidence_summary, perspectives):
    """
    Decides how much to trust each perspective agent.
    This function does NOT do medical reasoning.
    """

    # base trust (must sum ~1 later)
    weights = {
        "optimistic": 0.3,
        "analytical": 0.4,
        "pessimistic": 0.3
    }

    # --- Adaptive adjustments ---
    if evidence_summary.get("lab_severity") == "significant":
        weights["pessimistic"] += 0.2
        weights["optimistic"] -= 0.1

    if all(p["concern_level"] == perspectives[0]["concern_level"]
           for p in perspectives):
        # consensus → trust analytical more
        weights["analytical"] += 0.2

    # normalize weights
    total = sum(max(w, 0) for w in weights.values())
    for k in weights:
        weights[k] = max(weights[k], 0) / total

    return weights
