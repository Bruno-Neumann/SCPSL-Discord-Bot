#Only run this bot if you have multiple servers.
#You can duplicate this file if you have more than 2 servers.

import asyncio
import discord
from discord.ext import commands
import json

EnableStatus = True

bot = commands.Bot(command_prefix="!", intents=discord.Intents.none())

waitTime= 15

@bot.event
async def on_ready():
    print("The bot is running.")
    while True:
        f = open('data.json')
        data = json.load(f)

        if data["Success"] == True:

            #Change the 0 if you want to display another server
            #0 = 1st server, 1 = 2nd server, 2 = 3rd server and so on.
            playercount= data["Servers"][1]["Players"]

            if EnableStatus == True:
                sep = '/'
                totalPlayers = int(playercount.split(sep, 1)[0])
                totalSlots = int(playercount.split(sep, 1)[1])
                if totalPlayers == 0:
                    stat = discord.Status.idle
                elif totalPlayers == totalSlots:
                    stat= discord.Status.dnd
                else:
                    stat= discord.Status.online

            await bot.change_presence(status=stat,activity=discord.Game(name=playercount))
            print(playercount)     

            waitTime = data["Cooldown"] + 2
        else:
            print("Error 503: Rate limit exceeded")
        await asyncio.sleep(waitTime)


bot.run("Token")
