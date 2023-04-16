import discord
from discord.ext.commands import Cog, Bot, Context, hybrid_command, has_permissions

class Clear(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @hybrid_command(name="clear", description="Clear messages in channel")
    @has_permissions(manage_messages=True)
    async def clear(self, ctx: Context, int: int = 20):
        await ctx.send(f"Deleting {int} Messages")
        await ctx.channel.purge(limit=int)
        await ctx.send(f"{int} Messages Deleted")


    # doing something when the cog gets loaded
    async def cog_load(self):
        print(f"{self.__class__.__name__} loaded!")

    # doing something when the cog gets unloaded
    async def cog_unload(self):
        print(f"{self.__class__.__name__} unloaded!")


async def setup(bot: Bot):
    await bot.add_cog(Clear(bot=bot))
    