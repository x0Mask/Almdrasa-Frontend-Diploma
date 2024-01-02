import tkinter as tk
import requests

class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather Forecast")
        self.geometry('400x300')

        self.create_input_widgets()
        self.create_weather_info_widgets()

    def create_input_widgets(self):
        input_frame = tk.Frame(self)
        input_frame.pack(pady=20)

        self.entry = tk.Entry(input_frame)
        self.entry.pack(side=tk.LEFT, padx=10)

        self.button = tk.Button(input_frame, text="Search", command=self.get_weather)
        self.button.pack(side=tk.LEFT, padx=10)

    def create_weather_info_widgets(self):
        Weather_Info = tk.Label(self, text="Weather Information", font=("Arial", 14, "bold"))
        Weather_Info.pack()

        self.Temperature = tk.Label(self, text="Temperature", font=("Arial", 12))
        self.Temperature.pack(pady=5)

        self.Humidity = tk.Label(self, text="Humidity", font=("Arial", 12))
        self.Humidity.pack(pady=5)

        self.Wind_Speed = tk.Label(self, text="Wind Speed", font=("Arial", 12))
        self.Wind_Speed.pack(pady=5)

        self.Pressure = tk.Label(self, text="Pressure", font=("Arial", 12))
        self.Pressure.pack(pady=5)

        self.label = tk.Label(self, text="")
        self.label.pack()

    def get_weather(self):
        api_key = "Your API key"
        city = self.entry.get()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            weather_data = response.json()
            self.display_weather_info(weather_data)

        except requests.exceptions.RequestException as e:
            self.label.config(text="Error fetching data. Please check your city name or API key.")

    def display_weather_info(self, weather_data):
        self.Temperature.config(text=f"Temperature: {weather_data['main']['temp']}°C")
        self.Humidity.config(text=f"Humidity: {weather_data['main']['humidity']}%")
        self.Wind_Speed.config(text=f"Wind Speed: {weather_data['wind']['speed']} km/h")
        self.Pressure.config(text=f"Pressure: {weather_data['main']['pressure']} hPa")

if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
