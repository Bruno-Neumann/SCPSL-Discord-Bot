import asyncio
import discord
import requests
import json

id  = ""
api = ""

bot = discord.Client

@bot.event
async def on_ready():
    print("The bot is running.")
    while True:
        t = requests.get(f"https://api.scpslgame.com/serverinfo.php?id={id}&key={api}&players=true").text
        data = json.loads(t)
        await bot.change_presence(activity=discord.Game(name=data["Servers"][0]["Players"]))
        print(data["Servers"][0]["Players"])        
        await asyncio.sleep(60)


bot.run("Token")
