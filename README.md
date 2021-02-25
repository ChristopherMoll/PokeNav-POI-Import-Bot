# PokeNav-POI-Import-Bot
A simple discord bot for posting messages at a given interval.  Can be used to bulk import POIs into PokeNav.

## Setup
To run the bot, you'll need [Python](https://www.python.org/downloads/) installed on your system, as well as a bot token from Discord, which requires creating and registering a bot in the [Discord Developer Portal](http://discordapp.com/developers/applications).  

Once Python is installed, you'll need to install 2 Python packages.  From the command line, execute:
`pip install -U discord.py`
then
`pip install -U python-dotenv`

Now, edit the included .env file to contain your token.  Then, edit the included poi.txt file to contain the list of commands the bot should send, one command per line.  The commands should follow [PokeNav's syntax](https://docs.pokenavbot.com/moderation.html#adding-a-new-gym-pokestop) in order for it to be executed properly.  

Finally, add the bot to your server using the invite URL generated in the Discord Developer Portal.  The only permission this bot requires is Send Messages.

## Execution
Once the bot has successfully joined your server, use the `$start` command in whichever channel you want the bot to be running in.  It will begin executing the commands contained in poi.txt, sending one message every 3 seconds.  

## Stopping
Currently the only way to stop the bot from sending messages is to kill the bot via your command line (Control+C for Windows).
