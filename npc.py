import discord
from discord import Intents, Client, Game

intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

try:
    with open('token.txt', 'r') as file:
        token = file.read().strip()
except FileNotFoundError:
    print("Token file not found!")
    exit()

@client.event
async def on_message(message):
    target_user_id = 949241373922570240
    target_user_id_2 = 1182399676750770286
    if message.author.id == target_user_id or message.author.id == target_user_id_2:
        gif = "https://tenor.com/view/stfu-shut-up-stop-shut-your-mouth-shut-it-down-gif-20324546"
        await message.channel.send(gif)
	    
@client.event
async def on_message(message):
    if 'max' in message.content.lower():
        gif = "https://discord.com/channels/1182016042264952984/1182016043628105810/1226911570542727179"
        await message.channel.send(gif)

@client.event
async def on_ready():
	await client.change_presence(activity=Game(name="Subway Surfers"))
	print("Ready!")

client.run(token)
