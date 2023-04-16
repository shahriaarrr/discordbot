import discord
from discord.ext.commands import Cog, Bot, Context, hybrid_command, has_permissions

class Role(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    #give user server role
    @hybrid_command(name="add-role", description="assign role to user")
    @has_permissions(manage_messages=True)
    async def add_role(self, ctx: Context, member: discord.Member, rolename: discord.Role, reason=None):
        if not rolename:
            await ctx.send(f"hey {ctx.author.mention}\ndon't forget to provide a name!")
        else:
            addRole_embed = discord.Embed(
                title="🚨assign Role🚨",
                color=0x33D1FF
            )
            addRole_embed.set_thumbnail(url=member.display_avatar.url)
            addRole_embed.add_field(
                name=f"new member of role: {rolename.name}",
                value=f'''
                                        member {member.mention}
                                        reason: {reason}
                                        admin: {ctx.author.mention}
                                    '''
            )
            await member.add_roles(rolename)
            await ctx.send(f"Successfully created and assigned `{rolename.name}` to {member.mention}!")
            await ctx.bot.get_channel(channel_id).send(embed=addRole_embed)


    #get role from user
    @hybrid_command(name="rm-role", description="remove a role from user")
    @has_permissions(manage_messages=True)
    async def remove_role(self, ctx: Context, member: discord.Member, role: discord.Role, reason=None):
        await member.remove_roles(role)
        rmRole_embed = discord.Embed(
            title="🚨remove Role🚨",
            color=0xed0216
        )
        rmRole_embed.set_thumbnail(url=member.display_avatar.url)
        rmRole_embed.add_field(
            name=f"remove role: {role.name}",
            value=f'''
                                                member {member.mention}
                                                reason: {reason}
                                                admin: {ctx.author.mention}
                                            '''
        )
        await ctx.send(f"got `{role.name}` from {member.mention}!")
        await ctx.bot.get_channel(channel_id).send(embed=rmRole_embed)

    async def cog_load(self):
        print(f"{self.__class__.__name__} loaded!")

    # doing something when the cog gets unloaded
    async def cog_unload(self):
        print(f"{self.__class__.__name__} unloaded!")


async def setup(bot: Bot):
    await bot.add_cog(Role(bot))