# ngrok-auto-start
## How to use 

1. Create a discord bot on https://discord.com/developers/applications and get the token key 

2. Change the BOT_TOKEN valeu in .env file to your token that you get on step 1

3. git clone https://github.com/luisf4/ngrok-auto-start

4. Create a file in /etc/systemd/system/ngrok.service

5. nano /etc/systemd/system/ngrok.service

6. add 
[Unit]
Description=Ngrok
After=network.service

[Service]
type=simple
User=<YOUR USER HERE>
WorkingDirectory=/root
ExecStart=python3 /PATH/TO/start.py
Restart=on-failure

[Install]
WantedBy=multi-user.target

7. Save the file

8. Give permition to execute the file: sudo chmod 644 /lib/systemd/system/ngrok.service

9. Enable the service: sudo systemctl daemon-reload && sudo systemctl enable ngrok.service

10. Adeed

11. Reboot the system and done!