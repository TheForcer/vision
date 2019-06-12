import requests
import configparser
import json

# Import config file and create config sections
config = configparser.ConfigParser()
config.read("/opt/config/vision.cfg")
cfg_pihole = config["pihole"]

# Return a specific stat from the PiHole API
def getPiholeStat(stat):
    url = cfg_pihole["url"] + "/admin/api.php"
    json_data = json.loads(requests.request("GET", url, data="", headers="").text)
    return json_data[stat]

print(
    "Von den heutigen "
    + str(getPiholeStat("dns_queries_today"))
    + " DNS Anfragen wurden "
    + str(getPiholeStat("ads_blocked_today"))
    + " geblockt!"
)
