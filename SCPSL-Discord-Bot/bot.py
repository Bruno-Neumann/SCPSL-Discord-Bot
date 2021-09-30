from asyncio.tasks import wait_for
import discord
import requests
import json
import time
from discord.ext import commands


bot = commands.Bot(command_prefix="!")
@bot.event
async def on_ready():
    print("The bot is running.")
    while True:
        t = requests.get("https://api.scpslgame.com/serverinfo.php?id=<ID>&key=<API>&players=true").text
        data = json.loads(t)
        await bot.change_presence(activity=discord.Game(name=data["Servers"][0]["Players"]))
        print(data["Servers"][0]["Players"])        
        time.sleep(12)


bot.run("Token")

    