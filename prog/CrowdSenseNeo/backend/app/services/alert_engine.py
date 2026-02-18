def handle_sos(data):
    if data.riskLevel in ["high", "critical"]:
        escalate(data)

    return {
        "status": "success",
        "message": "SOS alert triggered"
    }

def escalate(data):
    print("🚨 ESCALATING SOS")
    print("Location:", data.location)
    print("Source:", data.source)