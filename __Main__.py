import os
import time

import discord
from dotenv import load_dotenv

# Loads the .env file
load_dotenv()

# Token from discord for bot API access
TOKEN = os.getenv('DISCORD_TOKEN')

# Path to the poi.txt file
COMMAND_FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + '\poi.txt'

# The number of seconds between sending commands
SEND_DELAY = 3

client = discord.Client()

# Executed when the bot successfully connects to discord
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

# Executed when a message is posted in any channel that the bot is in
@client.event
async def on_message(message):
    # Make sure we're not being triggered by our own message
    if message.author == client.user:
        return

    # If the message sent is "$start", begin sending commands
    if message.content == '$start':
        print('Starting')
        channel = message.channel
        await postCommands(channel)

# Opens the command file and reads line by line
async def postCommands(channel):
    poi_file = open(COMMAND_FILE_PATH, 'r')
    pois = poi_file.readlines()
    for poi in pois:
        await sendCommand(poi, channel)

# Pauses for a configured number of seconds, and then sends the command
async def sendCommand(poi, channel):
    time.sleep(SEND_DELAY)
    await channel.send(poi)

client.run(TOKEN)
