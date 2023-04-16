import discord
from discord.ext import commands
from typing import Any

'''
Cogs:
    Using Cogs in Discord.py, instead of putting all the commands in one file,
    we can consider a separate file for each command or group of commands with
    the same function or sub-commands and load these files in the main source of our bot.

extentions:
    In this version of the robot, we consider all the Cogs as a tuple called extentions and load this tuple.
'''
bot_extentions = (
    
)

class MyBot(commands.Bot):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)

    async def setup_hook(self) -> None:
        for extention in bot_extentions:
            await self.load_extension(extention)
        await self.tree.sync()
