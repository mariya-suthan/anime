def get_guidance(intent: str):
    guidance_map = {
        "danger": {
            "tone": "calm",
            "follow_up": "Are people pushing around you right now?"
        },
        "panic": {
            "tone": "reassuring",
            "follow_up": "Can you see any open space nearby?"
        },
        "general": {
            "tone": "friendly",
            "follow_up": "Tell me a bit more about the situation."
        },
        "unknown": {
            "tone": "curious",
            "follow_up": "What’s happening around you?"
        }
    }

    return guidance_map.get(intent, guidance_map["general"])
