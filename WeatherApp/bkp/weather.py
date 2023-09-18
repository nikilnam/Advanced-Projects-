import tkinter as tk
import requests
import datetime
from tkinter import ttk
from io import BytesIO
from PIL import Image, ImageTk

api_key = "665f7d572ee197a49725be374ad11654" #d9004412aaec0c2e9a414627cf056b07



# Function to fetch weather data from OpenWeatherMap API
def get_weather():
    city = city_entry.get()
    get_starting_weather(city)
    # api_key = 'd9004412aaec0c2e9a414627cf056b07' 
    
    # # API request URL
    # url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial'
    # forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=imperial'
    
    # try:
    #     response = requests.get(url)
    #     data = response.json()
    #     temperature = data['main']['temp']
    #     weather_description = data['weather'][0]['description']
    #     result_label.config(text=f'Temperature: {temperature}°C\nWeather: {weather_description}')
    #     curr_city_label.config(text=city)
    # except Exception as e:
    #     result_label.config(text='Error fetching data')


    # ##Test of if statement
    # ##test_word = "sun"
    # img = ""
    # if "sky" in weather_description:
    #     img = bgsunny
    # elif "rain" in weather_description:
    #     img = bgrainy
    # elif "cloud" in weather_description:
    #     img = bgcloudy
    # elif "mist" in weather_description:
    #     img = bgmist
    # elif "snow" in weather_description:
    #     img = bgsnow
    # elif "thunderstorm" in weather_description:
    #     img = bgthunderstrom
    # else:
    #     img = bgcloudy

    # my_label_sunny.config(image= img)

    # my_label_sunny = tk.Label(app, image = img)
    # my_label_sunny.place(x=0, y=0, relwidth=1, relheight=1)
    

def get_starting_weather(name_of_city):
    # api_key = 'd9004412aaec0c2e9a414627cf056b07'  

    # API request URL
    url = f'http://api.openweathermap.org/data/2.5/weather?q={name_of_city}&appid={api_key}&units=imperial'
    # forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=imperial'
    
    try:
        response = requests.get(url)
        data = response.json()
        longitude = data['coord']['lon']
        latitude = data['coord']['lat']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        weather_icon = data['weather'][0]['icon']
        result_label.config(text=f'Temperature: {temperature}°F\nWeather: {weather_description}')
        curr_city_label.config(text=name_of_city)
        # result_label.set('Temp')
        # curr_city_label.set(name_of_city)
    except Exception as e:
        result_label.config(text='Error fetching data')

    img = ""
    if "sky" in weather_description:
        img = bgsunny
    elif "rain" in weather_description:
        img = bgrainy
    elif "cloud" in weather_description:
        img = bgcloudy
    elif "mist" in weather_description:
        img = bgmist
    elif "snow" in weather_description:
        img = bgsnow
    elif "thunderstorm" in weather_description:
        img = bgthunderstrom
    else:
        img = bgcloudy

    # my_label_sunny.config(image= img)

    # my_label_sunny = tk.Label(app, image = img)
    # my_label_sunny.place(x=70, y=300)
    
    # Fetch the weather icon
    icon_url = f'https://openweathermap.org/img/wn/{weather_icon}@4x.png'     
    response = requests.get(icon_url)
    icon_data = response.content
    icon_image = Image.open(BytesIO(icon_data))
    icon_photo = ImageTk.PhotoImage(icon_image)    
    weather_icon_label.config(image= icon_photo)

    return longitude, latitude    


def getforecast_data(name_of_city):
    city = name_of_city
    # api_key = 'd9004412aaec0c2e9a414627cf056b07'  

    forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=imperial'

    response = requests.get(forecast_url)
    data = response.json()
    temperatures = data['list']
    city = data['city']
    

    weather_data = []

    for x in temperatures:
        entry = {
            'date' : x['dt'],
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

    # for entry in weather_data:
    #     print(entry)

    return weather_data

def getforecast_air_pollution(lat, lon):
    ##### Forecasted Air Pollution    
    # api_key = 'd9004412aaec0c2e9a414627cf056b07' 

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
            'date' : x['dt'],
        }
        pollution_data.append(entry)

    return pollution_data

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
    tree2.column("#1", width=75)
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
    tree2.place(x=325, y= 325)

    ######

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
    tree.column("#1", width=75)
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

    s = ttk.Style()
    s.theme_use('default')
    s.configure('Treeview.Item', indicatorsize=0)

    tree.pack()
    tree.place(x=325, y= 100)

    ######
    

# Create the main application window
app = tk.Tk()
app.geometry("920x600")

# #Define Image
bgsunny = tk.PhotoImage(file ="C:/Users/s-nnambiar/OneDrive - Lake Washington School District/12th grade/Advanced Software Projects/Advanced-Projects-/WeatherApp/Sunny.png")
bgrainy = tk.PhotoImage(file ="C:/Users/s-nnambiar/OneDrive - Lake Washington School District/12th grade/Advanced Software Projects/Advanced-Projects-/WeatherApp/rain.png")
bgcloudy = tk.PhotoImage(file = "C:/Users/s-nnambiar/OneDrive - Lake Washington School District/12th grade/Advanced Software Projects/Advanced-Projects-/WeatherApp/cloudy.png")
bgmist = tk.PhotoImage(file ="C:/Users/s-nnambiar/OneDrive - Lake Washington School District/12th grade/Advanced Software Projects/Advanced-Projects-/WeatherApp/mist.png")
bgsnow = tk.PhotoImage(file ="C:/Users/s-nnambiar/OneDrive - Lake Washington School District/12th grade/Advanced Software Projects/Advanced-Projects-/WeatherApp/snow.png")
bgthunderstrom = tk.PhotoImage(file ="C:/Users/s-nnambiar/OneDrive - Lake Washington School District/12th grade/Advanced Software Projects/Advanced-Projects-/WeatherApp/thunderstorm.png")

# #Create Label
# my_label_rainy = tk.Label(app, image = bgrainy)
# my_label_rainy.place(x=0, y=0, relwidth=1, relheight=1)

weather_icon_label = tk.Label(app)
weather_icon_label.place(x=70, y=300)

my_label_sunny = tk.Label(app, image = bgsunny)
my_label_sunny.place(x=0, y=0, relwidth=1, relheight=1)

app.title("Weather App")

# # Create and configure GUI elements
city_label = tk.Label(app, text="Enter City:")
city_label.pack()

city_entry = tk.Entry(app)
city_entry.pack()

get_weather_button = tk.Button(app, text="Get Weather", command=get_weather)
get_weather_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()
result_label.place(x=100, y= 200)

# ##Create label for other cities called
curr_city_label = tk.Label(app, font= ("Helvetica", 50), bd=1, relief = "sunken")
curr_city_label.pack()
curr_city_label.place(x=100, y= 120)

##Test Labels

# ####
city = "Boston"
lon,lat = get_starting_weather(city)

forecast_data = getforecast_data("seattle")
create_weather_forecast_table()

pollution_data = getforecast_air_pollution(lat, lon)
create_air_pollution_forecast_table()

#####

# layer_label = tk.Label(app)
# api_key = 'd9004412aaec0c2e9a414627cf056b07' 
# layer_url = f'https://tile.openweathermap.org/map/precipitation_new/0/0/0.png?appid={api_key}'
# response = requests.get(layer_url)
# layer_data = response.content
# layer_image = Image.open(BytesIO(layer_data))
# photo = ImageTk.PhotoImage(layer_image)

# layer_label.config(image= photo)
# layer_label.pack()
# layer_label.place(x=100, y=300)

# data = response.json()



app.mainloop()

# temperature = data['main']['temp']
# weather_description = data['weather'][0]['description']



#This should change sunset time of this 152409 to 03:24:09
#[datetime.datetime.strptime(time, "%H:%M").strftime("%I:%M %p") for time in times]


## This code will give you 12 hr time if the time is in this format (12:45:08)
##def convert12(str):
   ## h1 = ord(str[0]) - ord('0');
   ## h2 = ord(str[1]) - ord('0');
 
  ##  hh = h1 * 10 + h2;
  ##  Meridien="";
  ##  if (hh < 12):
   ##     Meridien = "AM";
  ##  else:
    ## Meridien = "PM";
 
   ## hh %= 12;
    #if (hh == 0):
     #   print("12", end = "");
      #  for i in range(2, 8):
       #     print(str[i], end = "");
 
   # else:
    #    print(hh,end="");
     #   for i in range(2, 8):
      #      print(str[i], end = "");
 
    #print(" " + Meridien);
#if __name__ == '__main__':
 #   str = "17:35:20";
 #   convert12(str);
 

#convert dt to datetime