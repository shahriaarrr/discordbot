import discord
from discord.ext.commands import Cog, Bot, Context, hybrid_command

class About(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @hybrid_command(name="dev", description="about developer")
    async def dev(self, ctx: Context):
        about_embed = discord.Embed(
            title="About developer of َAgah discord bot",
            color=0x51F349,
        )
        about_embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/1049342836203589652/1073230088222552064/profile_avatar_a38b8ccf-1cef-4cb2-aeef-aa32bae276ef.png",
        )
        about_embed.add_field(name="Who am i?",
                              value='''
                Hi, I'm Shahriar🙋‍♂️
                🤖ZAAL's father
                💻Computer engineering student
                👨‍💻Python Developer
                ✒Sometimes the author 
                🔗All links related to me: https://shahriaarrr.ir / https://blog.shahriaarrr.ir
                ''',
        )

        await ctx.send(embed=about_embed)

    #about your discord server
    @hybrid_command(name="agah", description="about this discord server")
    async def agah(self, ctx: Context):
        about_embed = discord.Embed(
            title="about_this_server",
            color=0x51F349,
        )
        about_embed.set_thumbnail(
            url="img_link",
        )
        about_embed.add_field(name="about_server",
                              value="your_text",
        )

        await ctx.send(embed=about_embed)

    async def cog_load(self):
        print(f"{self.__class__.__name__} loaded!")

    # doing something when the cog gets unloaded
    async def cog_unload(self):
        print(f"{self.__class__.__name__} unloaded!")


async def setup(bot: Bot):
    await bot.add_cog(About(bot))