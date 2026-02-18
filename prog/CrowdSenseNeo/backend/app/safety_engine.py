def decide_actions(intent, risk_level):
    actions = {
        "show_sos": False,
        "suggest_call": False,
        "suggest_escape": False,
        "notify_trusted_contact": False
    }

    if intent == "danger":
        actions["suggest_escape"] = True

        if risk_level in ["medium", "high"]:
            actions["show_sos"] = True
            actions["notify_trusted_contact"] = True

        if risk_level == "high":
            actions["suggest_call"] = True

    return actions
