import retrofit2.Call
import retrofit2.http.Body
import retrofit2.http.POST

interface ApiService {

    @POST("/chat")
    fun sendMessage(
        @Body request: ChatRequest
    ): Call<ChatResponse>
    @POST("/api/sos")
    fun sendSOS(
        @Body request: SosRequest
    ): Call<SosResponse>

}