import discord
 
USER_ID= '624300941042253824'
ngrok_url ='aaaaaaaaaaaaa'

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
    print(message)
    print(message.author.send)
    await message.author.send(ngrok_url)

    # if message.author == client.user:
    #     return
 
    if message.content.startswith('hi'):

        await message.channel.send('Hello!')
 
client.run('')