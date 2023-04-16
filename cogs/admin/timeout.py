import discord
from discord.ext.commands import Bot, Cog, hybrid_command, Context, has_permissions
from datetime import timedelta

class Timeout(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @hybrid_command(name="timeout", description="timeout members")
    @has_permissions(manage_messages=True)
    async def timeout(self, ctx: Context, member: discord.Member, day: int = 0, hour: int = 0, minute: int = 0, reason=None):
        time = timedelta(days=day, hours=hour, minutes=minute)

        timeout_embed = discord.Embed(
            title="🚨timeout member🚨",
            color=discord.Colour.orange(),
        )
        timeout_embed.set_thumbnail(url=member.display_avatar.url)
        timeout_embed.add_field(
            name=f"timeout <@{member.id}>",
            value=f'''
                        timeout: **{member.name}**
                        
                        for ** `{day}` days, `{hour}` hours, `{minute}` minutes **
                            
                        reason: `{reason}`
                            
                        admin: {ctx.author.mention}
                    '''
        )

        # creating the max timeout timedelta object
        limit_time = timedelta(days=28)

        # checking if the author's requested time did not exceed the max limit if so : we change it to the limit
        if time > limit_time:
            time = limit_time

        # finaly timeouting the member
        await member.timeout(time, reason=f"By {ctx.author}")
        embed = discord.Embed(color=discord.Colour.green(),
            description=f"{member.mention} has been successfully timeouted for `{day}` days and `{hour}` hours and `{minute}` minutes in the server"
        )
        await ctx.send(embed=embed)
        await ctx.bot.get_channel(1084038897761263636).send(embed=timeout_embed)
        


    async def cog_load(self):
        print(f"{self.__class__.__name__} loaded!")

        # doing something when the cog gets unloaded
    async def cog_unload(self):
        print(f"{self.__class__.__name__} unloaded!")

async def setup(bot: Bot):
    await bot.add_cog(Timeout(bot))
    