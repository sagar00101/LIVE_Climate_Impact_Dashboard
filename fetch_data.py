import os
from datetime import datetime
import pandas as pd
import requests

cities = [
    {"city": "Mumbai", "lat": 19.0760, "lon": 72.8777, "zone": "Coastal"},
    {"city": "Pune", "lat": 18.5204, "lon": 73.8567, "zone": "Western Plateau"},
    {"city": "Nagpur", "lat": 21.1458, "lon": 79.0882, "zone": "Vidarbha"},
    {"city": "Nashik", "lat": 19.9975, "lon": 73.7898, "zone": "North Maharashtra"},
    {"city": "Chhatrapati Sambhajinagar", "lat": 19.8762, "lon": 75.3433, "zone": "Marathwada"},
]

records = []
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for item in cities:
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={item['lat']}&longitude={item['lon']}&current=temperature_2m,relative_humidity_2m,surface_pressure,wind_speed_10m"
    aqi_url = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={item['lat']}&longitude={item['lon']}&current=pm10,pm2_5,european_aqi"

    weather_res = requests.get(weather_url).json().get("current", {})
    aqi_res = requests.get(aqi_url).json().get("current", {})

    records.append({
        "timestamp": current_time,
        "state": "Maharashtra",
        "city": item["city"],
        "zone": item["zone"],
        "temperature_celsius": weather_res.get("temperature_2m"),
        "humidity_percent": weather_res.get("relative_humidity_2m"),
        "wind_speed_kmh": weather_res.get("wind_speed_10m"),
        "pm2_5": aqi_res.get("pm2_5"),
        "pm10": aqi_res.get("pm10"),
        "aqi_index": aqi_res.get("european_aqi")
    })

df = pd.DataFrame(records)
csv_name = "maharashtra_climate_live_data.csv"

if not os.path.exists(csv_name):
    df.to_csv(csv_name, index=False)
else:
    df.to_csv(csv_name, mode="a", header=False, index=False)

print("Data save ho gaya! Total rows:", len(pd.read_csv(csv_name)))