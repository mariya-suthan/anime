def apply_friendly_tone(answer, tone="calm"):
    prefix = {
        "calm": "Hey — I’m right here with you. ",
        "reassuring": "It’s okay, I’ve got you. ",
        "alert": "Listen carefully — ",
    }

    emoji = {
        "calm": "🙂",
        "reassuring": "🤝",
        "alert": "⚠️",
    }

    return f"{emoji.get(tone, '')} {prefix.get(tone, '')}{answer}"
