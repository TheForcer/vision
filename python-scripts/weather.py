import requests
import configparser
import json
import sys
import pytz
from pytz import timezone
from datetime import datetime, timedelta

# Import config file and create config section
config = configparser.ConfigParser()
config.read('/opt/vision.cfg')
cfg_weather = config['weather']

# Default timezone and date format
utc = pytz.utc
fmt = '%d.%m %H:%M'

# Return the json response data for a specific forecast location
def getForecast(location):
    if location == "default":
        url = "https://api.openweathermap.org/data/2.5/forecast?q="+cfg_weather['location']+"&mode=json&units=metric&lang=de&APPID="+cfg_weather['apikey']
    else:
        url = "https://api.openweathermap.org/data/2.5/forecast?q="+location+"&mode=json&units=metric&lang=de&APPID="+cfg_weather['apikey']

    json_data = json.loads(requests.request("GET", url, data="", headers="").text)
    return json_data

# Create the string to return if request was either 200 or 400
def createString(json_data, location):
    if json_data["cod"] == "404":
        return "Die gesuchte Stadt wurde nicht gefunden."
    forecast_list = json_data["list"]
    if location == "default":
        string = "Wetter in: "+cfg_weather['location']+"""\n"""
    else:
        string = "Wetter in: "+location+"""\n"""
    i = 0
    while i < 3:
        utc_dt = utc.localize(datetime.utcfromtimestamp(forecast_list[i]["dt"]))
        de_tz = timezone('Europe/Berlin')
        de_dt = utc_dt.astimezone(de_tz)
        string = string+str(de_dt.strftime(fmt))+" / "+str(forecast_list[i]["main"]["temp"])+"°C / "+forecast_list[i]["weather"][0]["description"]+"""\n"""
        i+=1
    return string

print(createString(getForecast(sys.argv[1]), sys.argv[1]))