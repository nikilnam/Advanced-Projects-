# Advanced-Projects-
Nikil Nambiar 
09/10/23
Design Doc: 
Weather App
What the project is about:
The project I am creating is a weather app. The weather app will have a User Interface that when you select a city it will give you the current weather and THE NEXT BLANK. The background of the app will display either sun, rain, fog, cloudy, etc based on the weather in different cities. 
How we plan on creating it: 
We will be coding in python on VS code and will use Open Weather map API to get the current weather conditions and 5 days forecast. It will kind of look like the apple weather app on our phones. If the user enters a city name that is invalid, we will show an error, so they know the name is invalid. 
Downside or tradeoffs: 
The Open Weather map API (Application Programing Interface) will only allow us to make a maximum of 60 calls a minute with the free subscriptions. 
Major components of code: 
1)	One of them would make an API request and parse the response for the weather data and then extra the weather data related to our project: temperature. 
2)	User interface in which we need to list the cities and show the temperature and have the correct background for the given weather for the city. It should be smooth running so the user can get his information quickly and easily. 
What design (UI) decisions we are making: 
So, we will have different colors and backgrounds for each city that is displayed due to the weather. We will also have weather icons to show the weather conditions and there will be a bar with a drop-down list in which we can import the cities in which the user can choose from. 
What API integration we are choosing: 
We need to choose a weather data provider which would be the Open Weather Map API. 
