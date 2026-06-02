import os
import requests
from datetime import datetime

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

# --------------------------------------------------
# Load environment variables
# --------------------------------------------------

load_dotenv()


# --------------------------------------------------
# Weather Tool
# --------------------------------------------------

def get_weather(city: str):
    """
    Get current weather information for a city.
    """

    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        return {
            "error": "OPENWEATHER_API_KEY is missing."
        }

    try:
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={
                "q": city,
                "appid": api_key,
                "units": "metric"
            },
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        temp_c = round(data["main"]["temp"], 1)
        temp_f = round((temp_c * 9 / 5) + 32, 1)

        return {
            "city": data["name"],
            "country_code": data["sys"]["country"],
            "temperature_celsius": temp_c,
            "temperature_fahrenheit": temp_f,
            "condition": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed_mps": data["wind"]["speed"],
            "pressure": data["main"]["pressure"]
        }

    except requests.exceptions.HTTPError:
        return {
            "error": f"Could not find weather data for '{city}'."
        }

    except Exception as e:
        return {
            "error": str(e)
        }


# --------------------------------------------------
# Location Tool
# --------------------------------------------------

def get_location():
    """
    Get the user's current location from IP address.
    Use when the user asks about weather but doesn't
    provide a city.
    """

    try:
        response = requests.get(
            "https://ipapi.co/json/",
            headers={"User-Agent": "weather-agent"},
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return {
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country_name")
        }

    except Exception as e:
        return {
            "error": str(e)
        }


# --------------------------------------------------
# LLM
# --------------------------------------------------

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2
)


# --------------------------------------------------
# System Prompt
# --------------------------------------------------

today = datetime.now().strftime("%Y-%m-%d")

system_prompt = f"""
You are a professional weather assistant.

Today's date is {today}.

Rules:

1. If the user asks about weather without specifying a location:
   - Call get_location()
   - Then call get_weather() using the detected city

2. If the user provides a city:
   - Call get_weather(city)

3. Use Fahrenheit for:
   - United States
   - Liberia
   - Myanmar

4. Use Celsius for all other countries.

5. Present weather in a friendly format.

Include:
- Location
- Temperature
- Condition
- Humidity
- Wind speed
- Pressure

6. Never display raw JSON.

7. If a tool returns an error,
   explain it clearly to the user.

Example format:

Current Weather

📍 Location: Rome, Italy
🌡 Temperature: 24°C
☁️ Condition: Clear Sky
💧 Humidity: 55%
💨 Wind Speed: 3.2 m/s
🔵 Pressure: 1015 hPa

Briefly summarize the weather conditions.
"""


# --------------------------------------------------
# Agent
# --------------------------------------------------

agent = create_agent(
    model=llm,
    tools=[
        get_weather,
        get_location
    ],
    system_prompt=system_prompt
)


# --------------------------------------------------
# Main Loop
# --------------------------------------------------

if __name__ == "__main__":

    print("Weather Assistant")
    print("Type 'exit' to quit.\n")

    while True:

        user_query = input("You: ")

        if user_query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        try:
            response = agent.invoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": user_query
                        }
                    ]
                }
            )

            print("\nAssistant:")
            #print(response["messages"][-1].content)
            print(type(response["messages"][-1].content))
            print()

        except Exception as e:
            print(f"\nError: {e}\n")