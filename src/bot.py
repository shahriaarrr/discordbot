import discord
from discord.ext import commands
from asyncio import *
from random import randint,choice

#create your bot class
class CONFING:
    TOKEN = 'BOT TOKEN'
    PREFIX = '-'

client = commands.Bot(command_prefix = CONFING.PREFIX)
#remove the difult help command
client.remove_command('help')

#to show you when your bot ready to work
@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.dnd,
    activity = discord.Game("With Discord Bots"))
    print("Bot Online....")

#join member's message
@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.dnd,
    activity = discord.Activity(type = discord.ActivityType.watching, name = "توسعه گر😁"))
    print("Bot Online....")

#left or remove member's message
@client.event
async def on_member_join(member):
   await client.get_channel(805436123546386514).send(f"{member.name} has joined")

#kick command
@client.command()
@commands.has_permissions(manage_messages = True)
async def kick(ctx, member : discord.Member, *, reason = None ):
    await member.kick(reason = reason)
    await ctx.send(f"Kicked {member.mention}")

#ban command
@client.command()
@commands.has_permissions(manage_messages = True)
async def ban(ctx, member : discord.Member, *, reason = None ):
    await member.ban(reason = reason)
    await ctx.send(f"Banned {member.mention}")

#unban command
@client.command()
@commands.has_permissions(manage_messages=True)
async def unban(ctx, user : discord.User):
    guild = ctx.guild
    bans = await ctx.guild.bans()
    for i in bans:
        if(user in i):  
            await guild.unban(user=user)
            await ctx.send(f'{user.mention} Successfully Unbanned From Server')


#say Hi
@client.command()
async def hi(ctx):
    mention = ctx.author.mention
    await ctx.send("Hi %s🙋‍♂️" % (mention))


@client.command()
async def taas(ctx):
    #a simple game
    x = randint(1, 6)
    await ctx.send("Your number is: %i" % (x))

#you can set your name and pass((just a game))
@client.command()
async def cmd(ctx, * ,values):
    values = values.split()
    password = values[0]
    name = values[1]
    await ctx.send("password: "+password+"\n"+"name: "+name)

#set your bot's status
@client.command()
#If you want to use a command only for admins, you must type the following command before defining the function
@commands.has_permissions(manage_messages = True)
async def setstatus(ctx, status_type):
    #Admin command
    if(status_type == 'idle'):
        #idle status
        await client.change_presence(status = discord.Status.idle)
        await ctx.send("status change to --> idle")
    elif(status_type == 'dnd'):
        #do not disturb message
        await client.change_presence(status = discord.Status.dnd)
        await ctx.send("status change to --> dnd")
    else:
        #online status
        await client.change_presence(status = discord.Status.online)
        await ctx.send("status change to --> online")

#set your bot's activity
@client.command()
@commands.has_permissions(manage_messages = True)
async def setactivity(ctx, activity_type, * ,activity_text):
    #Admin command
    mention = ctx.author.mention
    if(activity_type == 'playing'):
        await client.change_presence(activity = discord.Game(name = activity_text))
        await ctx.send("%s. Activity changed" % (mention))


    elif(activity_type == 'streaming'):
        await client.change_presence(activity = discord.Streaming(name = activity_text,
         url ='http://twitch.tv/twitch' ))
        await ctx.send("%s. Activity changed" % (mention))


    elif(activity_type == 'listening'):
        await client.change_presence(activity = discord.Activity(type = discord.ActivityType.listening,
        name = activity_text)) 
        await ctx.send("%s. Activity changed" % (mention))


    elif(activity_type == 'watching'):
        await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching,
        name = activity_text))
        await ctx.send("%s. Activity changed" % (mention))


    else:
        #unknown command
        await ctx.send("%s Unknown Activity(%s)" % (mention, activity_type))

#embed
@client.command()
async def embed(ctx):
    embed1 = discord.Embed(
        title = "your embed's title",
        description = "your embed's description",
        #Put all your favorite colors in this list below(0x{your color's HTML code})
        colour = 0x19D8E5,
    )

    # await ctx.send(embed = {your embed name})
    await ctx.send(embed = embed1)

@client.command()
async def random_embed(ctx):
    colors = [ 
        0x19D8E5, 
    ]
    text = [
        "List the texts needed to display your embed in this way",
    ]
    text2 = [
        "List the texts needed to display your embed in this way",
    ]
    m1 = discord.Embed(
        title = 'text 1',
        description = choice(text),
        color = choice(colors)
    )
    m2 = discord.Embed(
        title = 'text 2',
        description = choice(text2),
        colors = choice(colors),
    )

    m_all = [m1, m2]
    x = choice(m_all)
    x.set_footer(text = 'your text')
    x.set_image(url = "your image's URL")

    await ctx.send(embed = x)


#clear all of message in text channel
@client.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount = 100):
    #Admin command
    await ctx.channel.purge(limit = amount)
    await ctx.send("Chat Cleared")


@client.command()
async def about(ctx):
    aboutme = '''
    Hi, I'm Shahriar🙋‍♂️

    🤖(bot.py)'s father

    💻Computer engineering student

    👨‍💻Python Developer

    ✒Sometimes the author 

    🔗All links related to me: https://zil.ink/shahriaarrr12
    '''
    m1 = discord.Embed(
        title = "programmer of this project",
        description = aboutme,
        color = 0x51F349,
    )
    await ctx.send(embed = m1)


#run your bot
client.run(CONFING.TOKEN)