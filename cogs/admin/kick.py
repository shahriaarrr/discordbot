import discord
from discord.ext.commands import Cog, Bot, Context, hybrid_command, has_permissions

class Kick(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    #kick user
    @hybrid_command(name='kick', description="kick member")
    @has_permissions(manage_messages=True)
    async def kick(self, ctx: Context, member: discord.Member, reason=None):

        # check author have permission
        if not ctx.author.guild_permissions.moderate_members:
            embed = discord.Embed(
                color=discord.Colour.red(), description="You do not have the permission to use this command")
            await ctx.send(embed=embed)
            return

        kick_embed = discord.Embed(
            title="🚨kick member🚨",
            color=0xFF000
        )
        kick_embed.set_thumbnail(url=member.display_avatar.url)
        kick_embed.add_field(
            name=f"Kicked <@{member.id}>",
            value = f'''
                kick {member.name}
                reason: {reason}
                admin: {ctx.author.mention}
            '''
        )
        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member.mention}")
        await ctx.bot.get_channel(channel_id).send(embed=kick_embed)

    async def cog_load(self):
        print(f"{self.__class__.__name__} loaded!")

    # doing something when the cog gets unloaded
    async def cog_unload(self):
        print(f"{self.__class__.__name__} unloaded!")


async def setup(bot: Bot):
    await bot.add_cog(Kick(bot))
