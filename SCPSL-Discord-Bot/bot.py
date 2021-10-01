import asyncio
import discord
from discord.ext import commands
import requests
import json

bot = commands.Bot(command_prefix="!")
@bot.event
async def on_ready():
    print("The bot is running.")
    while True:
        t = requests.get("https://api.scpslgame.com/serverinfo.php?id=<ID>&key=<API>&players=true").text
        data = json.loads(t)
        await bot.change_presence(activity=discord.Game(name=data["Servers"][0]["Players"]))
        print(data["Servers"][0]["Players"])        
        await asyncio.sleep(60)


bot.run("Token")

    
