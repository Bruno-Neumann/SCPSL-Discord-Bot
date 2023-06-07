import asyncio
import discord
import requests
import json

#Insert the api key and Account ID of your server here.

id  = ""
api = ""

#If you have more than 1 server and want this bot to display the other servers change this value. 
#1st server = 0, 2nd = 1, 3rd = 2 etc

server = 0

bot = commands.Bot(command_prefix="!", intents=discord.Intents.none())

@bot.event
async def on_ready():
    print("The bot is running.")
    while True:
        t = requests.get(f"https://api.scpslgame.com/serverinfo.php?id={id}&key={api}&players=true").text
        data = json.loads(t)
        playercount= data["Servers"][server]["Players"]
        await bot.change_presence(activity=discord.Game(name=playercount))
        print(playercount)        
        await asyncio.sleep(60)


bot.run("Token")
