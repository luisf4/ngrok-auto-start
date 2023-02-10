# ngrok-auto-start
How to use 

1. Create a discord bot on https://discord.com/developers/applications and get the token key 

2. Change the BOT_TOKEN valeu in .env file to your token that you get on step 1

3. Place the project folder in /home 

4.1 Make the start.sh executable 
4.2 chmod +x start.sh 

5.1 Make that it executes on boot
5.2 crontab -e
5.3 @reboot  /home/ngrok-auto-start/start.sh
