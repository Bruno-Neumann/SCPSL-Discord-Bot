import asyncio
import discord
from discord.ext import commands
import requests
import json

#Insert the api key and Account ID of your server here.
id  = ""
api = ""

#Set this to False if you dont want the bot to change status depending on player count
enableStatus = True

#How often the bot should query the API in seconds
waitTime = 15

#Set this to True if you wish to use the secondary bot
enableSecondaryBot = False


bot = commands.Bot(command_prefix="!", intents=discord.Intents.none())
@bot.event
async def on_ready():
    print("The bot is running.")
    while True:
        t = requests.get(f"https://api.scpslgame.com/serverinfo.php?id={id}&key={api}&players=true").text
        data = json.loads(t)

        if data["Success"] == True:
            if enableSecondaryBot == True:
                f = open("data.json", "w")
                f.write(t)
                f.close()

            #Change the 0 if you want to display another server
            #0 = 1st server, 1 = 2nd server, 2 = 3rd server and so on.
            playercount = data["Servers"][0]["Players"]

            if enableStatus == True:
                totalPlayers = int(playercount.split("/", 1)[0])
                totalSlots = int(playercount.split("/", 1)[1])
                if totalPlayers == 0:
                    stat = discord.Status.idle
                elif totalPlayers == totalSlots:
                    stat = discord.Status.dnd
                else:
                    stat = discord.Status.online

            await bot.change_presence(status=stat,activity=discord.Game(name=playercount))
            print(playercount)     

            waitTime = data["Cooldown"] + 1
        else:
            print("Error 503: Rate limit exceeded")
        await asyncio.sleep(waitTime)


bot.run("Token")
