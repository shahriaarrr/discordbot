import discord
from discord import ActivityType
import os
from dotenv import load_dotenv
import logging.handlers
import asyncio

import bot

# load .env file to get bot token
load_dotenv()
TOKEN = os.getenv('TOKEN')

# logging system
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
logger.addHandler(handler)

intents = discord.Intents.all()

#build our bot object
my_bot = bot.MyBot(
    command_prefix='$',
    intents=intents,
    allowed_mentions=discord.AllowedMentions(everyone=False, roles=False),
    activity=discord.Activity(type=ActivityType.watching, name="your_custom_status"),
    status=discord.Status.dnd,
    help_command=None,
)

# run the bot
async def run():
    async with my_bot:
        await my_bot.start(TOKEN)

asyncio.run(run())
