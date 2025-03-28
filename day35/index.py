# day35.py
import os
import requests
from twilio.rest import Client

# Load environment variables
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
api_key = os.getenv("OPEN_WEATHER_API_KEY")

# OpenWeather API Endpoint
OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

# Weather API request parameters
weather_params = {
    "q": "Lagos",
    "appid": api_key,
    "cnt": 12
}

# Fetch weather data
response = requests.get(OWN_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data.get("list", [])[:12]

# Check for rain
it_will_rain = any(int(hour_data["weather"][0]["id"]) < 700 for hour_data in weather_slice)

if it_will_rain:
    print("Bring an umbrella")
    
    # Initialize Twilio Client
    if account_sid and auth_token:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="It's going to rain today. Remember to bring an umbrella ☔",
            from_="+12056284033",  # Replace with your Twilio number
            to="+2347081104745"    # Replace with your actual phone number
        )
        print(f"SMS sent: {message.sid}")
    else:
        print("Twilio credentials are missing. SMS not sent.")





# city = "Lagos"
# url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
# response_one = requests.get(url)
# response_one.raise_for_status()
# weather_data = response_one.json()
# print(weather_data["list"][0]["weather"][0]["description"])




