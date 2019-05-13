import requests
import configparser
import json
import sys

# Import config file and create config sections
config = configparser.ConfigParser()
config.read('/opt/vision.cfg')
cfg_weather = config['weather']

# Return a specific stat from the PiHole API
def getForecast(location):
    if location == "default":
        url = "https://api.openweathermap.org/data/2.5/forecast?q="+cfg_weather['location']+"&mode=json&units=metric&APPID="+cfg_weather['apikey']
    else:
        url = "https://api.openweathermap.org/data/2.5/forecast?q="+location+"&mode=json&units=metric&APPID="+cfg_weather['apikey']

    json_data = json.loads(requests.request("GET", url, data="", headers="").text)
    return json_data

def createString(json_data):
    forecast_list = json_data["list"]
    string = "Wetter: "
    i = 0
    while i < 3:
        string = string+forecast_list[i]["dt_txt"]+" / "+str(forecast_list[i]["main"]["temp"])+"°C / "+forecast_list[i]["weather"][0]["main"]+" | "
        i+=1
    return string


print(createString(getForecast(sys.argv[1])))