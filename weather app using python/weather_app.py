from tkinter import *
import requests
import json
from datetime import datetime

root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Weather App By Vivek Kulkarni')

city_value = StringVar()

def currentTime(utc):
    local_time = datetime.utcfromtimestamp(utc)
    return local_time

def showWeather():
    api = '810ffed7d29bdf1e1ef784394c3d6584'
    city_name = city_value.get()
    weatherURL = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api}'
    responce = requests.get(weatherURL)
    weather_info = responce.json()
    tfield.delete('1.0',END)
    if weather_info['cod'] == 200:
        kelvin = 273
        temp = int(weather_info['main']['temp']-kelvin)
        temp_feels_like = int(weather_info['main']['feels_like']-kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed']*3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
        sunrise_time = currentTime(sunrise+timezone)
        sunset_time = currentTime(sunset+timezone)

        weather = f'\nWeather of: {city_name}\nTemperature (Celsius): {temp}\nFeels Like (Celsius): {temp_feels_like}\nPressure: {pressure} hPa\nHumidity: {humidity}\nWind Speed: {wind_speed}\nSunrise At: {sunrise_time}\nSubset At: {sunset_time}\nCloud: {cloudy}%\nInfo: {description}'
    else:
        weather = f'\n\tWeather for "{city_name}" not found!!\n\tPlease Enter Valid City name'
    
    tfield.insert(INSERT, weather)

city = Label(root, text='Enter City Name',font=('Times new roman',12,'bold')).pack(pady=10)
city_input = Entry(root, width=30,textvariable=city_value,font=('Times new roman',14,'bold'),justify=CENTER).pack()
btn = Button(root, text='Check Weather', font=('Times new roman',10),fg='black',bg='lightblue',padx=5,pady=5,cursor='hand2',command=showWeather).pack(pady=20)
weather_now = Label(root,text='The Weather is: ',font=('Times new roman',12,'bold')).pack(pady=10)
tfield = Text(root,width=46,height=10)
tfield.pack()


root.mainloop()