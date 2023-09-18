import tkinter as tk
import requests
import datetime
from tkinter import ttk
# from io import BytesIO
# from PIL import Image, ImageTk
import datetime

api_key = "665f7d572ee197a49725be374ad11654" 



# Function to fetch weather data from OpenWeatherMap API
def get_weather():
    city = city_entry.get()
    get_starting_weather(city)
    

# Function to fetch weather data from OpenWeatherMap API given a city
def get_starting_weather(name_of_city):

    url = f'http://api.openweathermap.org/data/2.5/weather?q={name_of_city}&appid={api_key}&units=imperial'
    
    try:
        response = requests.get(url)
        data = response.json()
        longitude = data['coord']['lon']
        latitude = data['coord']['lat']
        temperature = data['main']['temp']
        temperature_min = data['main']['temp_min']
        temperature_max = data['main']['temp_max']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']
        weather_icon = data['weather'][0]['icon']
        
        # If weather_icon contains d it is day and if n it is night
        if 'd' in weather_icon: 
            my_label_sunny.config( image = bgsunny)
        else:
            my_label_sunny.config( image = bgnight)
        
        # Set all the labels with weather data
        curr_weather_label.config(text=f'{temperature}°F')
        temperature_min_label.config(text=f'L: {temperature_min}°F')
        temperature_max_label.config(text=f'H: {temperature_max}°F')
        pressure_label.config(text=f'Pressure: {pressure}')
        humidity_label.config(text=f'Humidity: {humidity}')
        weather_des_label.config(text=weather_description)

        curr_city_label.config(text=str.upper(name_of_city))
        curr_weather_label.config(text=f'{temperature}°F')

    except Exception as e:
        result_label.config(text='Error fetching data')

       
    # Fetch the weather icon
    icon_photo = tk.PhotoImage(file =f"C:/Users/s-nnambiar/OneDrive - Lake Washington School District/12th grade/Advanced Software Projects/Advanced-Projects-/WeatherApp/{weather_icon}@4x.png") 
    weather_icon_label = tk.Label(app, image = icon_photo, bg="grey")
    weather_icon_label.pack()    
    weather_icon_label.place(x=80, y=355)
    weather_icon_label.img_ref = icon_photo    

    return longitude, latitude    


# Function to get 5 days weather forecast for every 3 hours
def getforecast_data(name_of_city):
    city = name_of_city
    
    forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=imperial'

    response = requests.get(forecast_url)
    data = response.json()
    temperatures = data['list']
    city = data['city']    

    weather_data = []

    for x in temperatures:
        entry = {
             'date' : datetime.datetime.utcfromtimestamp(x['dt']).strftime('%Y-%m-%d %H'),
            # 'date' : x['dt'],
            'temp' : x['main']['temp'],
            'min_temp' : x['main']['temp_min'],
            'max_temp' : x['main']['temp_max'] ,   
            'pressure' : x['main']['pressure'],
            'humidity' : x['main']['humidity'],

            'weather' : x['weather'][0]['description'],
            'weather_icon' : x['weather'][0]['icon'],

            'wind_speed' : x['wind']['speed'],
            'wind_deg' : x['wind']['deg'],
            'wind_gust' : x['wind']['gust']
        }
        weather_data.append(entry)

    return weather_data

# Function to get 5 days air pollution forecast for every 3 hours
def getforecast_air_pollution(lat, lon):
   
    air_pollution_url = f'http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={lat}&lon={lon}&appid={api_key}'
    response = requests.get(air_pollution_url)
    data = response.json()

    pollution_data = []

    for x in data['list']:
        entry = {
            'CO' : x['components']['co'],
            'NO' : x['components']['no'],
            'NO2' : x['components']['no2'],
            'O3' : x['components']['o3'],
            'SO2' : x['components']['so2'],
            'PM2_5' : x['components']['pm2_5'],
            'PM10' : x['components']['pm10'],
            'NH3' : x['components']['nh3'],
            # 'date' : x['dt'],
            'date' : datetime.datetime.utcfromtimestamp(x['dt']).strftime('%Y-%m-%d %H'),
        }
        pollution_data.append(entry)

    return pollution_data

# Fill the air pollution forecast table
def create_air_pollution_forecast_table():
    #####
    # Create a Treeview widget
    tree2 = ttk.Treeview(app, show="headings", columns=("Date", "CO", "NO", "NO2", "O3", "SO2", "PM2_5", "PM10", "NH3"))
    # Add the header to the Treeview
    tree2.heading("#1", text="Date")
    tree2.heading("#2", text="CO")
    tree2.heading("#3", text="NO")
    tree2.heading("#4", text="NO2")
    tree2.heading("#5", text="O3")
    tree2.heading("#6", text="SO2")
    tree2.heading("#7", text="PM2_5")
    tree2.heading("#8", text="PM10")
    tree2.heading("#9", text="NH3")
    # Set the width of each column in the Treeview 
    tree2.column("#1", width=90)
    tree2.column("#2", width=55)
    tree2.column("#3", width=55)
    tree2.column("#4", width=55)
    tree2.column("#5", width=55)
    tree2.column("#6", width=55)
    tree2.column("#7", width=55)
    tree2.column("#8", width=55)
    tree2.column("#9", width=55)

    air_pollution_data_list = []
    for item in pollution_data:    
        data = (item['date'], item['CO'], item['NO'], item['NO2'], item['O3'], item['SO2'], item['PM2_5'], item['PM10'], item['NH3'] )    
        air_pollution_data_list.append(data)

    # Inserting air pollution  data into the forecast table
    for item in air_pollution_data_list:
        tree2.insert("", "end", values=item)

    tree2.pack()
    tree2.place(x=325, y= 355)

    ######

# Fill the weather forecast table
def create_weather_forecast_table():
    #####
    # Create a Treeview widget
    tree = ttk.Treeview(app, show="headings", columns=("Date", "Weather", "Temp", "Min Temp", "Max Temp", "Pressure", "Humidity"), padding=[0,0,0,0])
    # Add the header to the Treeview
    tree.heading("#1", text="Date")
    tree.heading("#2", text="Weather")    
    tree.heading("#3", text="Temp (°F)")
    tree.heading("#4", text="Min Temp (°F)")
    tree.heading("#5", text="Max Temp (°F)")
    tree.heading("#6", text="Pressure")
    tree.heading("#7", text="Humidity")
    # Set the width of each column in the Treeview 
    tree.column("#1", width=90)
    tree.column("#2", width=100)    
    tree.column("#3", width=75)
    tree.column("#4", width=85)
    tree.column("#5", width=85)
    tree.column("#6", width=75)
    tree.column("#7", width=55)

    weather_data = []
    for item in forecast_data:    
        data = (item['date'], item['weather'], item['temp'], item['min_temp'], item['max_temp'], item['pressure'], item['humidity'] )    
        weather_data.append(data)

    # Inserting weather data into the forecast table
    for item in weather_data:
        tree.insert("", "end", values=item)

    tree.pack()
    tree.place(x=325, y= 100)

    

# Create the main application window
app = tk.Tk()
app.geometry("920x600")

# Define Image variables
bgsunny = tk.PhotoImage(file ="C:/Users/s-nnambiar/OneDrive - Lake Washington School District/12th grade/Advanced Software Projects/Advanced-Projects-/WeatherApp/Sunny.png")
bgnight = tk.PhotoImage(file ="C:/Users/s-nnambiar/OneDrive - Lake Washington School District/12th grade/Advanced Software Projects/Advanced-Projects-/WeatherApp/night.png")

my_label_sunny = tk.Label(app, image = bgsunny)
my_label_sunny.pack()
my_label_sunny.place(x=0, y=0, relwidth=1, relheight=1)

app.title("Weather App")

# # Create and configure GUI elements
city_label = tk.Label(app, text="Enter City:")
city_label.pack()

city_entry = tk.Entry(app)
city_entry.pack()

get_weather_button = tk.Button(app, text="Get Weather", command=get_weather)
get_weather_button.pack()

# ##Create label for other cities called
curr_city_label = tk.Label(app, font= ("Helvetica", 30), bd=1, relief = "sunken")
curr_city_label.pack()
curr_city_label.place(x=50, y= 50)

curr_weather_label = tk.Label(app, font= ("Helvetica", 45), bd=1, relief = "sunken")
curr_weather_label.pack()
curr_weather_label.place(x=50, y= 100)

weather_des_label = tk.Label(app, font= ("Helvetica", 20), bd=1)
weather_des_label.pack()
weather_des_label.place(x=50, y= 172)

temperature_min_label = tk.Label(app, font= ("Helvetica", 15), bd=1)
temperature_min_label.pack()
temperature_min_label.place(x=50, y= 209)

temperature_max_label = tk.Label(app, font= ("Helvetica", 15), bd=1)
temperature_max_label.pack()
temperature_max_label.place(x=200, y= 209)

pressure_label = tk.Label(app, font= ("Helvetica", 15), bd=1)
pressure_label.pack()
pressure_label.place(x=50, y= 237)

humidity_label = tk.Label(app, font= ("Helvetica", 15), bd=1)
humidity_label.pack()
humidity_label.place(x=50, y= 265)

weather_forecast_label = tk.Label(app, font= ("Helvetica", 10), bd=1)
weather_forecast_label.pack()
weather_forecast_label.place(x=325, y= 80)
weather_forecast_label.config(text=f'5-Day Weather Forecast every 3 hours')

airpollution_forecast_label = tk.Label(app, font= ("Helvetica", 10), bd=1)
airpollution_forecast_label.pack()
airpollution_forecast_label.place(x=325, y= 335)
airpollution_forecast_label.config(text=f'5-Day Air Pollution Forecast every hour')

# ####
# Default city
city = "Sammamish"
lon,lat = get_starting_weather(city)

forecast_data = getforecast_data(city)
create_weather_forecast_table()

pollution_data = getforecast_air_pollution(lat, lon)
create_air_pollution_forecast_table()

app.mainloop()