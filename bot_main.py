# -------------------------------------------------------------------------------- #
# ++++++++++++++++++++++++++++++++++ A.R.M.E.D. ++++++++++++++++++++++++++++++++++ #
# -------------------------------------------------------------------------------- #


# Imports
# Requires: 'pip install discord.py'
import discord
from discord.ext import commands

# Intents
intents = discord.Intents.all() 
intents.message_content = True

# Create bot-instance
bot = commands.Bot(command_prefix='!', intents=intents)


# on_ready()-function. Prints startup informations and loads extension files
@bot.event
async def on_ready():

    print(   ) #////////////////////////#
    print(f'Bot is online as: \"{bot.user.name}\"!\t[Bot-ID: {bot.user.id}]\n\n')
    print('\033[4mConnected to the following servers:\033[0m') 
    for server in bot.guilds:
        print(f'Server: {server}\tServer-ID: {server.id}')

    print('\n') #////////////////////////#

    print('\033[4mDEBUG: The following Extentions were loaded:\033[0m') 
    await bot.load_extension('bot_commands')
    await bot.load_extension('bot_core')

    print(   ) #////////////////////////#
    print('---------------------------------------------------------')


token_path = 'resources/bot_token.txt' 
token = ''

# Read token from bot_token.txt file
try:
    with open(token_path, 'r') as file:
        token = file.read()
except FileNotFoundError:
    print(f"The file '{token_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

# Run the bot with the token
bot.run(token)


# ---------------------------------------------------------------------- #
# by sylvan013
