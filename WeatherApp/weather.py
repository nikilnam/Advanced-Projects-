import tkinter as tk
import requests

# Function to fetch weather data from OpenWeatherMap API
def get_weather():
    city = city_entry.get()
    api_key = 'd9004412aaec0c2e9a414627cf056b07'  # Replace with your API key
    
    # API request URL
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    # url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(url)
        data = response.json()
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        result_label.config(text=f'Temperature: {temperature}°C\nWeather: {weather_description}')
    except Exception as e:
        result_label.config(text='Error fetching data')

# Create the main application window
app = tk.Tk()
app.geometry("920x964")

#Define Image
bgsunny = tk.PhotoImage(file ="Pictures\Sunny.png")

#Create Label
my_label = tk.Label(app, image = bgsunny)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

app.title("Weather App")

# Create and configure GUI elements
city_label = tk.Label(app, text="Enter City:")
city_label.pack()

city_entry = tk.Entry(app)
city_entry.pack()

get_weather_button = tk.Button(app, text="Get Weather", command=get_weather)
get_weather_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
