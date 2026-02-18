import android.Manifest
import android.content.pm.PackageManager
import androidx.core.app.ActivityCompat
import com.google.android.gms.location.FusedLocationProviderClient
import com.google.android.gms.location.LocationServices

class ChatActivity : AppCompatActivity() {
    private lateinit var fusedLocationClient: FusedLocationProviderClient
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_chat)
        fusedLocationClient = LocationServices.getFusedLocationProviderClient(this)

        sosButton.setOnClickListener {

            val location = getCurrentLocation()

            val request = SosRequest(
                location = location,
                source = "chat",
                riskLevel = currentRiskLevel
            )

            RetrofitClient.api.sendSOS(request)
                .enqueue(object : Callback<SosResponse> {

                    override fun onResponse(
                        call: Call<SosResponse>,
                        response: Response<SosResponse>
                    ) {
                        Toast.makeText(
                            this@ChatActivity,
                            "🚨 SOS sent successfully",
                            Toast.LENGTH_LONG
                        ).show()
                    }

                    override fun onFailure(call: Call<SosResponse>, t: Throwable) {
                        Toast.makeText(
                            this@ChatActivity,
                            "❌ SOS failed",
                            Toast.LENGTH_LONG
                        ).show()
                    }
                })
        }
    }
    private fun getCurrentLocation(callback: (String) -> Unit) {

    if (ActivityCompat.checkSelfPermission(
            this,
            Manifest.permission.ACCESS_FINE_LOCATION
        ) != PackageManager.PERMISSION_GRANTED
    ) {
        ActivityCompat.requestPermissions(
            this,
            arrayOf(Manifest.permission.ACCESS_FINE_LOCATION),
            101
        )
        callback("permission_denied")
        return
    }

    fusedLocationClient.lastLocation
        .addOnSuccessListener { location ->
            if (location != null) {
                val loc = "${location.latitude},${location.longitude}"
                callback(loc)
            } else {
                callback("location_unavailable")
            }
        }
}


    // ✅ MUST BE HERE
    private fun getCurrentLocation(): String {
        return "8.1823,77.4119"
    }
}
