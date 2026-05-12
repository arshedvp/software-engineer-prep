import requests

api_key="5513f27212cb3c3c25dc1e7faaf86033"

while True:
    city = input("\nEnter the city name (or E for exit): ")

    if city.upper() == "E":
        print("Exiting app")
        break

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    data = response.json()

    if data["cod"] != 200:
        print("City not found")
    else:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather=data["weather"][0]["description"]

        print(f"""
Weather Report
----------------
City        : {city}
Temperature : {temperature}°C
Humidity    : {humidity}%
Condition   : {weather}
""")