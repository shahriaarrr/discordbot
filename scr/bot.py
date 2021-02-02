import discord
from discord.ext import commands
from asyncio import *
from random import randint

class CONFING:
    TOKEN = 'BOT TOKEN'
    PREFIX = '-'

client = commands.Bot(command_prefix = CONFING.PREFIX)
client.remove_command('help')

@client.event
async def on_ready():
    print("Bot Online....")

@client.command()
async def salam(ctx):
    mention = ctx.author.mention
    await ctx.send("salam %s" % (mention))

@client.command()
async def taas(ctx):
    x = randint(1, 6)
    await ctx.send("Your number is: %i" % (x))

@client.command()
async def cmd(ctx, * ,values):
    values = values.split()
    password = values[0]
    name = values[1]
    await ctx.send("password: "+password+"\n"+"name: "+name)

@client.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount = 100):
    await ctx.channel.purge(limit = amount)
    await ctx.send("Chat Cleared")




client.run(CONFING.TOKEN)
