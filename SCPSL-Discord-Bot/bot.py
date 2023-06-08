import asyncio
import discord
from discord.ext import commands
import requests
import json

#Insert the api key and Account ID of your server here.

id  = ""
api = ""

bot = commands.Bot(command_prefix="!", intents=discord.Intents.none())

@bot.event
async def on_ready():
    print("The bot is running.")
    while True:
        t = requests.get(f"https://api.scpslgame.com/serverinfo.php?id={id}&key={api}&players=true").text
        data = json.loads(t)
        playercount= data["Servers"][0]["Players"]
        await bot.change_presence(activity=discord.Game(name=playercount))
        print(playercount)        
        await asyncio.sleep(60)


bot.run("Token")
