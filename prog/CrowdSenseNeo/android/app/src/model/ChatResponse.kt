data class ChatResponse(
    val answer: String,
    val intent: String,
    val risk_level: String,
    val actions: Actions
)