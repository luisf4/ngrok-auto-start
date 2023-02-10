import os
import requests
import subprocess
import time
from dotenv import load_dotenv
import discord


load_dotenv()

# Read the Discord bot token from the .env file
BOT_TOKEN = os.getenv("BOT_TOKEN")
# Read the ID of the user who will receive the Direct Message from the .env file
USER_ID = os.getenv("USER_ID")

# Start ngrok on port 8006
os.system("./ngrok-folder/ngrok http 8006 &")
time.sleep(5)

# Get the ngrok URL
ngrok_url = requests.get("http://localhost:4040/api/tunnels").json()["tunnels"][0]["public_url"]


# Initiates discord api
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
 
@client.event
async def on_ready():
    #Ready message
    print('On as {0.user}'.format(client))



@client.event
async def on_message(message):
    await message.author.send(ngrok_url)

    #sends the link every time somo one sends !link on the chat
    if message.content.startswith('link'):
        await message.channel.send(ngrok_url)


client.run(str(BOT_TOKEN))