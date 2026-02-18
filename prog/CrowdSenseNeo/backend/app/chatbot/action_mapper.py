def map_actions(risk_level):
    return {
        "show_sos": risk_level in ["medium", "high"],
        "notify_trusted_contact": risk_level == "high"
    }