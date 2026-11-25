# Python Weather App

## About the Project

This is a simple Python command-line Weather App that fetches real-time weather information using the OpenWeather API.

Users can enter a city name to view the current temperature, humidity, weather condition, wind speed, and a short 5-day forecast.

## Features

- Fetches weather data using a REST API
- Displays current temperature in Celsius
- Shows humidity and weather conditions
- Displays wind speed
- Provides a 5-day weather forecast
- Handles invalid city names
- Handles API and network errors
- Uses caching to reduce repeated API requests
- Protects the API key using environment variables

## Technologies Used

- Python 3
- Requests
- JSON
- Python-dotenv
- OpenWeather API

## API Used

OpenWeather Current Weather API and 5-Day Forecast API.

Website: https://openweathermap.org/api

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

## API Key Setup

1. Create an account on OpenWeather.
2. Generate an API key.
3. Create a `.env` file in the project folder.
4. Add the following line:

```text
OPENWEATHER_API_KEY=your_actual_api_key
```

Replace the placeholder with your API key.

## How to Run

Run the following command:

```bash
python weather.py
```

Enter a city name to view its weather information.

Press Enter without entering a city name to quit.

## API Key Protection

The API key is stored in a `.env` file and loaded using the python-dotenv library.

The `.env` file is included in `.gitignore` so that the secret key is not uploaded to GitHub.

The repository contains only `.env.example`, which provides a placeholder for users to add their own API key.

## Learning Outcomes

Through this project, I learned how to make REST API requests, parse JSON responses, handle API errors, use environment variables, and display weather information in a command-line application.

## Author

Pari Bansal
