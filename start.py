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
os.system("/root/ngrok http 8006 &")
time.sleep(5)

# Get the ngrok URL
ngrok_url = requests.get("http://localhost:4040/api/tunnels").json()["tunnels"][0]["public_url"]

# Send the ngrok URL as a Direct Message to the specified user




@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    await message.USER_ID.send(ngrok_url)
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

client.run(str(BOT_TOKEN))