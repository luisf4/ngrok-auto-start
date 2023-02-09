import os
import requests
import subprocess
import time
from dotenv import load_dotenv

load_dotenv()

# Read the Discord bot token from the .env file
BOT_TOKEN = os.getenv("BOT_TOKEN")
# Read the ID of the user who will receive the Direct Message from the .env file
USER_ID = os.getenv("USER_ID")

# Start ngrok on port 8006
os.system("ngrok http 8006 &")
time.sleep(5)

# Get the ngrok URL
ngrok_url = requests.get("http://localhost:4040/api/tunnels").json()["tunnels"][0]["public_url"]

# Send the ngrok URL as a Direct Message to the specified user
requests.post(
    f"https://discordapp.com/api/v6/users/{USER_ID}/channels",
    headers={
        "Authorization": f"Bot {BOT_TOKEN}",
        "User-Agent": "BotDiscord (https://github.com/Gilbert7, 0.1)",
        "Content-Type": "application/json"
    },
    json={
        "content": f"ngrok URL: {ngrok_url}",
        "tts": False,
        "embed": []
    }
)
