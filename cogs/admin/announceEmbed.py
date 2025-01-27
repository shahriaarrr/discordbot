import discord
from discord.ext.commands import Bot, Cog, hybrid_command, Context, has_permissions

class announceEmbedCog(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @hybrid_command(name="announce", description="send announce message")
    @has_permissions(manage_messages=True)
    async def send_embed(self, ctx: Context, title: str, description: str, image_url: str = None):
        embed = discord.Embed(
            title=title,
            description=description,
            color=discord.Color.blue()
        )
        
        if image_url:
            embed.set_image(url=image_url)

        if ctx.interaction:
            await ctx.interaction.response.send_message("done", ephemeral=True)
        
        await ctx.channel.send(embed=embed)

    async def cog_load(self):
        print(f"{self.__class__.__name__} loaded!")

    async def cog_unload(self):
        print(f"{self.__class__.__name__} unloaded!")

async def setup(bot: Bot):
    await bot.add_cog(announceEmbedCog(bot))
