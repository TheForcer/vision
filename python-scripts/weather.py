import requests
import configparser
import json
import sys
from datetime import datetime, timedelta
from pytz import timezone
import pytz

# Import config file and create config sections
config = configparser.ConfigParser()
config.read('/opt/vision.cfg')
cfg_weather = config['weather']

utc = pytz.utc
fmt = '%d.%m %H:%M'

# Return a specific stat from the PiHole API
def getForecast(location):
    if location == "default":
        url = "https://api.openweathermap.org/data/2.5/forecast?q="+cfg_weather['location']+"&mode=json&units=metric&lang=de&APPID="+cfg_weather['apikey']
    else:
        url = "https://api.openweathermap.org/data/2.5/forecast?q="+location+"&mode=json&units=metric&lang=de&APPID="+cfg_weather['apikey']

    json_data = json.loads(requests.request("GET", url, data="", headers="").text)
    return json_data

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