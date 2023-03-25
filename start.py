import os
import requests
import time
import discord

# Read the Discord bot token
BOT_TOKEN = 'YOUR BOT TOKEN GOES HERE'

# Start ngrok on port 8006
os.system("./ngrok start --all --config='/PATH/TO/YOUR/config.yml'&")
time.sleep(5)

# Get the ngrok URL
ngrok_url = requests.get("http://localhost:4040/api/tunnels").json()["tunnels"][0]["public_url"]


# Initiates discord api
intents = discord.Intents.all()

# Set the prefix
client = discord.Client(command_prefix='!', intents=intents)
 
# On event
@client.event
async def on_ready():
    #Ready message
    print('On as {0.user}'.format(client))

@client.event
async def on_message(message):
    #sends the link every time somo one sends !link on the chat
    if message.content.startswith('link'):
        await message.channel.send(ngrok_url)

# Auth bot
client.run(str(BOT_TOKEN))
