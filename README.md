# SCPSL-Discord-Bot
<br>
### SCPSL Discord Bot is a Player Count bot written in python for Discord.
##
### Requirements

* Verified SCP:SL Gameserver

* Something to run the bot 24/7

* Python 3.5.3 or higher

* Discord Server
##
### Installation Guide

**1.Installing discord.py**

  You can install it on Linux/macOS by using this command
  
    python3 -m pip install -U discord.py
  
  You can install it on Windows by using this command
  
    py -3 -m pip install -U discord.py
    
**2. Installing requests**
  
  You can install it on Linux/macOS by using this command
  
    pip install requests
    
  You can install it on Windows by using this command
  
    pip install requests
    
**3. Using Screen (Linux only)**
  
  Install Screen by using this command
  
    sudo apt install screen
    
**4. Installing the bot**

  * Download the latest release [here](https://github.com/Bruno-Neumann/SCPSL-Discord-Bot/releases/latest)

  * Get your server [account id and api key](https://github.com/Bruno-Neumann/SCPSL-Discord-Bot#get-your-server-account-id-and-the-api-key)

  * Get a [bot token](https://github.com/Bruno-Neumann/SCPSL-Discord-Bot#get-a-bot-token)

  * Edit the [bot.py file](https://github.com/Bruno-Neumann/SCPSL-Discord-Bot#edit-botpy)

##
### Get your server account id and the api key

  You can use the scpsl server console to get the id
  
    !id
  And the api key
  
    !api show

##
### Get a bot token

  You need to got to the [Discord Developer Portal](https://discord.com/developers/applications) then click New Application in the top right corner.
  
  You can name the bot how ever you want.
  
  Click on create and then click on the left side bot.
  
  You need to build a bot then you can see the profile of your bot.
  
  Get the token by clicking on copy.
  
##
### Edit bot.py
  
  Now paste your account id and the api key in the quotes and the  bot token in the quotes.
  
  ![Alt Text](https://i.ibb.co/p1stbVy/tutorial.jpg)
  
##
## Run the bot
  
   On Windows you can just open bot.py

   On Linux you can just open the bot via ssh you need to navigate to the directory where the bot is located and us the command
   
    ./start.sh
##
### Other

  The bot currently only supports one server per bot!
  If you have two servers running you can create a new bot and change the server variable.
  
  If you need help feel free to dm me [Bruno.#7047](https://discordapp.com/users/743877023394693302)
