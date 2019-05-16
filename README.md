# vision
A helpful bot for the matrix ecosystem, currently used for some smaller tasks.

## Setup & Start
Clone the repo to your preferred location:
```sh
git clone https://github.com/theforcer/vision
```

Set the execution bit on the trigger scripts that you want to run on startup:
```sh
chmod +x scripts/pihole
```

Copy and rename the config file and fill in the required keys etc:
```sh
cp vision.example.cfg vision.cfg
nano/vim/pico vision.cfg
```

Start up the bot/container with docker-compose (add -d if you want the process to run in the background):
```sh
docker-compose up
```

## Script Usage

### PiHole
The PiHole script is used to get a quick overlook of the total amount of (blocked) DNS queries. Configure the respective section in the config file with your PiHole's IP, and with a quick ```!pihole``` you'll get the information you need.

### Weather
This handy little script gives you a quick weather forecast for the next 3 three-hour intervals. Just call ```!weather city``` to get the latest information from the openweathermap API.
You'll need to [create an account](https://home.openweathermap.org/users/sign_up) over at OWM to get your API key, which you then have to put in the bot's config file, as well as a default location, which will be used when no city parameter is provided in the call.

## Update tiny-matrix-bot
To update to a current version of the bot script, run the following command in the repo.
This will replace the vision-bot.py file.
```sh
curl https://raw.githubusercontent.com/4nd3r/tiny-matrix-bot/master/tiny-matrix-bot.py | sed 's/"tiny-matrix-bot.cfg"/"vision.cfg"/g' > vision-bot.py
```