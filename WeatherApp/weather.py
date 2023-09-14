import tkinter as tk
import requests


# Function to fetch weather data from OpenWeatherMap API
def get_weather():
    city = city_entry.get()
    api_key = 'd9004412aaec0c2e9a414627cf056b07'  # Replace with your API key
    
    # API request URL
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(url)
        data = response.json()
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        result_label.config(text=f'Temperature: {temperature}°C\nWeather: {weather_description}')
        curr_city_label.config(text=city)
    except Exception as e:
        result_label.config(text='Error fetching data')


    ##Test of if statement
    ##test_word = "sun"
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
        
    
    

    my_label_sunny.config(image= img)

    #my_label_sunny = tk.Label(app, image = img)
    #my_label_sunny.place(x=0, y=0, relwidth=1, relheight=1)

    
        



def get_starting_weather(name_of_city):
    api_key = 'd9004412aaec0c2e9a414627cf056b07'  # Replace with your API key

    # API request URL
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    # forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
    
    
    try:
        response = requests.get(url)
        data = response.json()
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        result_label.config(text=f'Temperature: {temperature}°C\nWeather: {weather_description}')
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
    my_label_sunny.config(image= img)
    

def getforecast_data(name_of_city):
    city = name_of_city
    api_key = 'd9004412aaec0c2e9a414627cf056b07'  # Replace with your API key
    

    forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
        

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

            'wind_speed' : x['wind']['speed'],
            'wind_deg' : x['wind']['deg'],
            'wind_gust' : x['wind']['gust']
        }
        weather_data.append(entry)

    # for entry in weather_data:
    #     print(entry) 

    return weather_data
    


# Create the main application window
# app = tk.Tk()
# app.geometry("920x964")

# ####

# #Define Image
# bgsunny = tk.PhotoImage(file ="C:/Users/s-nnambiar/OneDrive - Lake Washington School District/12th grade/Advanced Software Projects/Advanced-Projects-/WeatherApp/Sunny.png")
# bgrainy = tk.PhotoImage(file ="C:/Users/s-nnambiar/OneDrive - Lake Washington School District/12th grade/Advanced Software Projects/Advanced-Projects-/WeatherApp/rain.png")
# bgcloudy = tk.PhotoImage(file = "C:/Users/s-nnambiar/OneDrive - Lake Washington School District/12th grade/Advanced Software Projects/Advanced-Projects-/WeatherApp/cloudy.png")
# bgmist = tk.PhotoImage(file ="C:/Users/s-nnambiar/OneDrive - Lake Washington School District/12th grade/Advanced Software Projects/Advanced-Projects-/WeatherApp/mist.png")
# bgsnow = tk.PhotoImage(file ="C:/Users/s-nnambiar/OneDrive - Lake Washington School District/12th grade/Advanced Software Projects/Advanced-Projects-/WeatherApp/snow.png")
# bgthunderstrom = tk.PhotoImage(file ="C:/Users/s-nnambiar/OneDrive - Lake Washington School District/12th grade/Advanced Software Projects/Advanced-Projects-/WeatherApp/thunderstorm.png")


# #Create Label

# ##my_label_rainy = tk.Label(app, image = bgrainy)
# ##my_label_rainy.place(x=0, y=0, relwidth=1, relheight=1)

# my_label_sunny = tk.Label(app, image = bgsunny)
# my_label_sunny.place(x=0, y=0, relwidth=1, relheight=1)


# app.title("Weather App")

# # Create and configure GUI elements
# city_label = tk.Label(app, text="Enter City:")
# city_label.pack()

# city_entry = tk.Entry(app)
# city_entry.pack()

# get_weather_button = tk.Button(app, text="Get Weather", command=get_weather)
# get_weather_button.pack()

# result_label = tk.Label(app, text="")
# result_label.pack()
# result_label.place(x=400, y= 300)


# ##Create label for other cities called
# curr_city_label = tk.Label(app, font= ("Helvetica", 40), bd=1, relief = "sunken")
# curr_city_label.pack()
# curr_city_label.place(x=400, y= 220)



# ####
# city = "Seattle"
# get_starting_weather(city)

# app.mainloop()




# temperature = data['main']['temp']
# weather_description = data['weather'][0]['description']

data = getforecast_data("seattle")
data

#convert dt to datetime