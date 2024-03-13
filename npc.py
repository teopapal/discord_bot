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
    if message.author.id == target_user_id:
        await message.channel.send(f'stfu im better')
	    
@client.event
async def on_ready():
	await client.change_presence(activity=Game(name="Subway Surfers"))
	print("Ready!")

client.run(token)
