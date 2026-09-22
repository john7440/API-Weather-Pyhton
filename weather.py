import os
from collections import defaultdict

import requests

WEATHER_API_KEY = os.getenv("API_KEY")

def get_weather_forecast(city_name: str, api_key:str) -> dict | None:

    api_url= f"https://api.openweathermap.org/data/2.5/forecast?q={city_name},fr&appid={api_key}&units=metric"

    try:
        response = requests.get(api_url, timeout=10)
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

def display_weather():
    cities = ["Saint-Geours-de-Maremne","Mérignac","Toulouse"]

    for city in cities:
        print(f"{city.capitalize()}'s weather\n")
        forcast_data = get_weather_forecast(city, WEATHER_API_KEY)

        if forcast_data:
            daily_summary = daily_min_max(forcast_data)

            for date, temps in daily_summary.items():
                print(f"Date: {date} | Min: {temps['min']:.1f}°C | Max: {temps['max']:.1f}°C")
        else:
             print(f"Forecast currently unavailable for {city}")

def main():
    display_weather()

if __name__ == '__main__':
    main()

