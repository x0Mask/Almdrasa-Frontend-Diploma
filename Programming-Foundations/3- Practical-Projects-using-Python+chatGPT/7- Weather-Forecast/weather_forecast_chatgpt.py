import tkinter as tk
import requests

def get_weather():
    api_key = "Your API key"
    city = entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        weather_data = response.json()
        display_weather_info(weather_data)

    except requests.exceptions.RequestException as e:
        label.config(text="Error fetching data. Please check your city name or API key.")

def display_weather_info(weather_data):
    Temperature.config(text=f"Temperature: {weather_data['main']['temp']}°C")
    Humidity.config(text=f"Humidity: {weather_data['main']['humidity']}%")
    Wind_Speed.config(text=f"Wind Speed: {weather_data['wind']['speed']} km/h")
    Pressure.config(text=f"Pressure: {weather_data['main']['pressure']} hPa")

root = tk.Tk()
root.title("Weather Forecast")
root.geometry('400x300')

# Input Field and Button Frame
input_frame = tk.Frame(root)
input_frame.pack(pady=20)

entry = tk.Entry(input_frame)
entry.pack(side=tk.LEFT, padx=10)

button = tk.Button(input_frame, text="Search", command=get_weather)
button.pack(side=tk.LEFT, padx=10)

# Weather Information Labels
Weather_Info = tk.Label(root, text="Weather Information", font=("Arial", 14, "bold"))
Weather_Info.pack()

Temperature = tk.Label(root, text="Temperature", font=("Arial", 12))
Temperature.pack(pady=5)

Humidity = tk.Label(root, text="Humidity", font=("Arial", 12))
Humidity.pack(pady=5)

Wind_Speed = tk.Label(root, text="Wind Speed", font=("Arial", 12))
Wind_Speed.pack(pady=5)

Pressure = tk.Label(root, text="Pressure", font=("Arial", 12))
Pressure.pack(pady=5)

label = tk.Label(root, text="")
label.pack()

root.mainloop()
