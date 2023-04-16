import discord
from discord.ext.commands import Cog, Bot, Context, hybrid_command
from discord.ui import View
from discord import app_commands

from . import staff_modals, staff_button


class StaffContact(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        view = View(timeout=None)
        button = staff_button.ContactButton(style=discord.ButtonStyle.green, label="Contact to staff team", custom_id="cot")
        view.add_item(button)
        bot.add_view(view)

    @hybrid_command(name='contact', description="to contact to server staff use this command")
    async def contact(self, ctx: Context):
        view = View(timeout=None)
        button = staff_button.ContactButton(style=discord.ButtonStyle.green, label="Contact to staff team", custom_id="cot")
        view.add_item(button)

        contact_embed = discord.Embed(
            title="Contact to staff team",
            color=0x00FF00,
            description="if you want to contact to staff team press the button"
        )
        await ctx.send(embed=contact_embed, view=view)


    @hybrid_command(name='dev_contact', description="to contact to developer of this bot use this command")
    async def dev_contact(self, ctx: Context):
        view = View()
        button = staff_button.ContactDev(style=discord.ButtonStyle.red, label="Contact to shahriaarrr")
        view.add_item(button)

        contact_embed = discord.Embed(
            title="Contact to shahriaarrr",
            color=0x00FF00,
            description="if you want to contact to developer of this bot press this button"
        )
        await ctx.send(embed=contact_embed, view=view)

    async def cog_load(self):
        print(f"{self.__class__.__name__} loaded!")

        # doing something when the cog gets unloaded
    async def cog_unload(self):
        print(f"{self.__class__.__name__} unloaded!")

async def setup(bot: Bot):
    await bot.add_cog(StaffContact(bot=bot))
