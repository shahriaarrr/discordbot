import discord
from discord.ui import Button, View
from typing import Any

from . import staff_modals

class ContactButton(Button):
    async def callback(self, interaction: discord.Interaction) -> Any:
        modal = staff_modals.ContactForm(timeout=None)
        await interaction.response.send_modal(modal)

class ContactDev(Button):
    async def callback(self, interaction: discord.Interaction) -> Any:
        modal = staff_modals.DevContact(timeout=None)
        await interaction.response.send_modal(modal)
    