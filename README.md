# vision
A helpful bot for the matrix ecosystem, currently used for some smaller tasks.

## Usage
Clone the repo to your preferred location:
```sh
git clone https://github.com/theforcer/vision
```

Set the execution bit on the trigger scripts that you want to run on startup:
```sh
chmod +x trigger-scripts/pihole
```

Copy and rename the config file and fill in the required keys etc:
```sh
cp vision.example.cfg vision.cfg
nano/vim/pico vision.cfg
```

Start up the container with docker-compose (add -d if you want the process to run in the background):
```sh
docker-compose up
```

## Update tiny-matrix-bot
To update to a current version of the bot script, run the following command in the repo.
This will replace the vision-bot.py file.
```sh
curl https://raw.githubusercontent.com/4nd3r/tiny-matrix-bot/master/tiny-matrix-bot.py | sed 's/"tiny-matrix-bot.cfg"/"vision.cfg"/g' > vision-bot.py
```