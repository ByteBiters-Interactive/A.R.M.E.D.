# -------------------------------------------------------------------------------- #
# ++++++++++++++++++++++++++++++++++ A.R.M.E.D. ++++++++++++++++++++++++++++++++++ #
# -------------------------------------------------------------------------------- #


# Imports
# Requires:: 'pip install discord.py'
from datetime import datetime
import json
import discord
from discord.ext import commands, tasks

# Read informations out config.json file
try:
    with open('resources/config.json', 'r', encoding='utf-8') as file:
        config_data = json.load(file)
except FileNotFoundError as e:
    print('error with config.json: ' + str(e))

message_content = config_data.get('message')
iteration_cycle = config_data.get('iteration_cycle')
day = config_data.get("day")

embed = discord.Embed(description=message_content, color=discord.Color.blurple())


class bot_core(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Execute core function of the bot
    @tasks.loop(hours=float(iteration_cycle))
    async def core_function(ctx):
        print(ctx)
        if int(datetime.now().day) == int(day):
            await ctx.send(embed=embed)
            print(f'[{datetime.now()}]: money-message was sent.')


async def setup(bot):
    await bot.add_cog(bot_core(bot))
    print(f'[{datetime.now()}]: loaded \'bot_core.py\'.')
    

# ---------------------------------------------------------------------- #
# by sylvan013
