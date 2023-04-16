import discord
from discord.ext.commands import Cog, Bot, Context, hybrid_group, has_permissions

class Channel(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @hybrid_group(name="channels")
    async def channels(self, ctx: Context):
        pass
    
    #lock channel
    @channels.command(name="lock", description="Lock a Text Channel")
    @has_permissions(manage_channels=True)
    async def lock(self, ctx: Context, channel: discord.TextChannel):
        await channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send(f"{channel.mention} Locked")

    #unlock channel
    @channels.command(name="unlock", description="Unlock a Text Channel")
    @has_permissions(manage_channels=True)
    async def unlock(self, ctx: Context, channel: discord.TextChannel):
        await channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send(f"{channel.mention} Unlocked")


    # doing something when the cog gets loaded
    async def cog_load(self):
        print(f"{self.__class__.__name__} loaded!")

        # doing something when the cog gets unloaded
    async def cog_unload(self):
        print(f"{self.__class__.__name__} unloaded!")

async def setup(bot: Bot):
    await bot.add_cog(Channel(bot=bot))
