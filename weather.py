import os
import logging
from collections import defaultdict

import requests

WEATHER_API_KEY = os.getenv("API_KEY")

logger = logging.getLogger(__name__)

def get_weather_forecast(city_name: str, api_key:str) -> dict | None:
    """Fetches the 5-day weather forecast for a given city from open weather map"""
    api_url= f"https://api.openweathermap.org/data/2.5/forecast?q={city_name},fr&appid={api_key}&units=metric"

    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException:
        logger.exception(f"Failed to fetch forecast for {city_name}")
        return None

def extract_daily_min_max(forecast_data: dict) -> dict:
    """Extracts the daily minimum and maximum temperatures from the interval data"""
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
    """Displays weather data for given cities"""
    cities = ["Saint-Geours-de-Maremne","Mérignac","Toulouse"]

    for city in cities:
        print(f"{city}'s weather\n")
        forecast_data = get_weather_forecast(city, WEATHER_API_KEY)

        if forecast_data:
            daily_summary = extract_daily_min_max(forecast_data)

            for date, temps in daily_summary.items():
                print(f"Date: {date} | Min: {temps['min']:.1f}°C | Max: {temps['max']:.1f}°C")
        else:
             print(f"Forecast currently unavailable for {city}")
        print("")

def main():
    """Main function"""
    logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S")

    if not WEATHER_API_KEY:
        logger.error("API_KEY environment variable not set")
        return

    display_weather()

if __name__ == '__main__':
    main()

