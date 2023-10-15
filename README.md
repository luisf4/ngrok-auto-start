# How to use 

Hello! This tutorial is about setting up a Discord bot with Ngrok, a tool that allows you to expose a local server to the internet. With this setup, you can develop and test your Discord bot locally and have it interact with a live Discord server send your link or TCP url.
![Snap](https://github.com/luisf4/ngrok-auto-start/assets/97737113/23b41128-928c-47f8-8bec-1855e77e6068)

## Prerequisites

Before we begin, make sure you have the following:

- A Discord account
- Basic knowledge of Python and how to create a Discord bot
- Access to a terminal on your computer

## Configure 
1. Create a discord bot on https://discord.com/developers/applications and get the token key 

2. Go to the file start.py and change the variable 'BOT_TOKEN' to your token that you got on step 1 and change the path to the config.yml

3. Go to https://ngrok.com/ and sing up, after that you will get a auth token from ngrok

4. Open the file config.yml and paste your auth token on the variable 'authtoken' and set the protocol and port that your service is running


## Create a service

5. Move the file ``` ngrok.service ``` to ``` /etc/systemd/system/ngrok.service ``` 

6. Configure variables acoording  
```
[Unit]
Description=Ngrok
After=network.service

[Service]
type=simple
User=<YOUR USER HERE>
WorkingDirectory=/root
ExecStart=python3 </PATH/TO/YOURstart.py>
Restart=on-failure

[Install]
WantedBy=multi-user.target
```
7. Save the file

8. Make the file executable: ``` sudo chmod 644 /lib/systemd/system/ngrok.service```

9. Enable the service:``` sudo systemctl daemon-reload && sudo systemctl enable ngrok.service```

10. Reboot the system and the service should be started. done!!
