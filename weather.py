import os
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



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
