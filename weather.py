import os
from collections import defaultdict

import requests

WEATHER_API_KEY = os.getenv("API_KEY")
API_URL = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name},fr&appid={WEATHER_API_KEY}&units=metric"

def get_weather_forecast(city_name: str) -> dict | None:

    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError as err:
        print(f"City {city_name} not found {err}")
        return None

def daily_min_max(forecast_data: dict) -> dict:
    daily_temps= defaultdict(list)

    for item in forecast_data.get("list", []):
        date_str = item["dt_txt"].split(" ")[0]

        temp = item["main"]["temp"]
        daily_temps[date_str].append(temp)

    daily_summary = {}
    for date, temps in daily_temps.items():
        daily_summary[date] = {"min": min(temps), "max": max(temps)}

    return daily_summary

def main():
    get_weather_forecast()

if __name__ == '__main__':
    main()

