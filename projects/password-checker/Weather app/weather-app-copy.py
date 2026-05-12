import requests

api_key = "5513f27212cb3c3c25dc1e7faaf86033"

while True:
    city=input("Enter the city name or E for exit: ")
    if city.upper()=="E":
        print("Exiting")
        break

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    data = response.json()

    temperature=data["main"]["temp"]
    feels_like=data["main"]["feels_like"]
    time_zone=data["timezone"]
    weather = data["weather"][0]["description"]

    print(f"""
Weather Report
----------------
City        : {city}
Temperature : {temperature}°C
feels like    : {feels_like}
timezone: {time_zone}
Condition   : {weather}
""")

