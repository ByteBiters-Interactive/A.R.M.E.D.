# -------------------------------------------------------------------------------- #
# ++++++++++++++++++++++++++++++++++ A.R.M.E.D. ++++++++++++++++++++++++++++++++++ #
# -------------------------------------------------------------------------------- #


# Imports
# Requires:: 'pip install discord.py'
from datetime import datetime
import json
from discord.ext import commands
from bot_core import bot_core

# Read informations out config.json file
try:
    with open('resources/config.json', 'r', encoding='utf-8') as file:
        config_data = json.load(file)
except FileNotFoundError as e:
    print('config.json not found: ' + str(e))

message_content = config_data.get('message')


class bot_commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # !ping command
    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.send('Pong!')
        print(f'[{datetime.now()}]: command \'ping\' was used.')

    # !send_manual command
    @commands.command(name='send_manual')
    async def send_manual(self, ctx):
        await ctx.send(message_content)
        print(f'[{datetime.now()}]: command \'send_manual\' was used.')

    # !start command
    @commands.command(name='start')
    async def start(self, ctx):
        await bot_core.core_function.start(ctx)
        print(f'[{datetime.now()}]: bot started.')
        await ctx.send('bot started.')
        

async def setup(bot):
    await bot.add_cog(bot_commands(bot))
    print(f'[{datetime.now()}]: loaded \'bot_commands.py\'.')
    

# ---------------------------------------------------------------------- #
# by sylvan013
