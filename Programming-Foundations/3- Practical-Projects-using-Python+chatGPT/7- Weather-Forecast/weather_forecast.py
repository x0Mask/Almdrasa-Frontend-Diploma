import tkinter as tk
import requests

def get_weather():
    api_key = "Your API key"
    city = entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        result = response.json()
        Temperature.config(text=f"Temperature: {result['main']['temp']}°C")
        Humidity.config(text=f"Humidity: {result['main']['humidity']}%")
        Wind_Speed.config(text=f"Wind Speed: {result['wind']['speed']}km/h")
        Pressure.config(text=f"Pressure : {result['main']['pressure']}hPa")
    else:
        label.config(text="Error fetching data. Please check your city name or API key.")

root = tk.Tk()
root.title("Weather Forecast")
root.geometry('600x400')

entry = tk.Entry(root)
entry.pack(side=tk.TOP, fill=tk.NONE ,padx=40)

button = tk.Button(root, text="Search", command=get_weather)
button.pack(side=tk.TOP, fill=tk.NONE ,padx=40)

Temperature = tk.Label(root, text="Temperature")
Temperature.pack(side=tk.TOP, fill=tk.X ,padx=40, pady=10)

Humidity = tk.Label(root, text="Humidity")
Humidity.pack(side=tk.TOP, fill=tk.X ,padx=40, pady=10)

Wind_Speed = tk.Label(root, text="Wind Speed")
Wind_Speed.pack(side=tk.TOP, fill=tk.X ,padx=40, pady=10)

Pressure = tk.Label(root, text="Pressure")
Pressure.pack(side=tk.TOP, fill=tk.X ,padx=40, pady=10)

label = tk.Label(root, text="")
label.pack()

root.mainloop()
