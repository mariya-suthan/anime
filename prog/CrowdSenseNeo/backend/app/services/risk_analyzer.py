def analyze_risk(intent: str, query: str) -> str:
    q = query.lower()

    if intent == "emergency":
        if any(word in q for word in ["stampede", "trapped", "falling"]):
            return "critical"
        return "high"

    if intent == "law":
        return "medium"

    return "low"
