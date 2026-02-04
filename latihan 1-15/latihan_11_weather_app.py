import requests

def get_weather(city_name, lat, lon):
    print(f"\n--- Mengambil Data Cuaca untuk {city_name} ---")

    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": "true",
        "timezone": "auto"
    }

    try:
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()

            current = data["current_weather"]
            suhu = current["temperature"]
            angin = current["windspeed"]

            print(f"🌡️ Suhu Saat Ini : {suhu} °C")
            print(f"💨 Kecepatan Angin : {angin} km/h")
            print(f"📍 Koordinat : {lat}, {lon}")
        else:
            print(f"[ERROR] Status Code: {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("[ERROR] Tidak ada koneksi internet!")
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    get_weather("Jakarta", -6.2088, 106.8456)
    get_weather("Makassar", -5.1477, 119.4327)