from meta.meta_agent import compute_agent_weights
from arbitration.decision_engine import arbitrate
from explainability import generate_explanation

weights = compute_agent_weights(evidence_summary, perspectives)
decision = arbitrate(perspectives, weights)
explanation = generate_explanation(decision, perspectives)

