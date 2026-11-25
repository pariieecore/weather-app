import requests
import os
import time
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5"

# Store recent weather results
cache = {}
CACHE_TIME = 600


# Fetch data from API
def fetch_weather(endpoint, city):
    cache_key = endpoint + city.lower()

    # Check cache
    if cache_key in cache:
        data, saved_time = cache[cache_key]

        if time.time() - saved_time < CACHE_TIME:
            return data

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(
            BASE_URL + endpoint,
            params=params,
            timeout=10
        )

        if response.status_code == 404:
            print("City not found! Please check the city name.")

        elif response.status_code == 401:
            print("Invalid API key or key not activated.")

        response.raise_for_status()

        data = response.json()

        cache[cache_key] = (data, time.time())

        return data

    except requests.exceptions.RequestException as e:
        print("Network or API error:", e)
        return None


# Display current weather
def show_current_weather(city):
    data = fetch_weather("/weather", city)

    if data is None:
        return

    main = data.get("main", {})
    weather = data.get("weather", [{}])[0]
    wind = data.get("wind", {})

    print("\n===== CURRENT WEATHER =====")
    print("City:", data.get("name", city))
    print("Temperature:", main.get("temp", "N/A"), "°C")
    print("Humidity:", main.get("humidity", "N/A"), "%")
    print("Condition:", weather.get("description", "N/A"))
    print("Wind Speed:", wind.get("speed", "N/A"), "m/s")


# Display 5-day forecast
def show_forecast(city):
    data = fetch_weather("/forecast", city)

    if data is None:
        return

    print("\n===== 5-DAY FORECAST =====")

    daily_forecast = {}

    for item in data.get("list", []):
        date = item.get("dt_txt", "").split(" ")[0]

        # Store one forecast entry per day
        if date and date not in daily_forecast:
            daily_forecast[date] = item

    for date, item in list(daily_forecast.items())[:5]:
        temp = item.get("main", {}).get("temp", "N/A")
        description = item.get("weather", [{}])[0].get(
            "description", "N/A"
        )

        formatted_date = datetime.strptime(
            date, "%Y-%m-%d"
        ).strftime("%d-%m-%Y")

        print(
            f"{formatted_date} | "
            f"{temp}°C | "
            f"{description.title()}"
        )


# Main program
def main():
    if not API_KEY:
        print("API key missing! Please add it to your .env file.")
        return

    while True:
        city = input("\nEnter city name (or press Enter to quit): ")

        if city.strip() == "":
            print("Thank you for using Weather App!")
            break

        show_current_weather(city)
        show_forecast(city)


if __name__ == "__main__":
    main()
