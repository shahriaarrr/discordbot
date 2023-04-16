import discord
import traceback
from discord.ext.commands import Bot

class ContactForm(discord.ui.Modal, title="contact to discord team"):
    name = discord.ui.TextInput(
        label='name',
        placeholder='boby',
        max_length=20,
    )
    subject = discord.ui.TextInput(
        label='subject',
        placeholder='Selling Elon Musk on the dark web :)',
        max_length=40,
    )
    email = discord.ui.TextInput(
        label="Email",
        placeholder='shahriaarrr@gmail.com',
        required=False,
        max_length=120,
    )
    message = discord.ui.TextInput(
        label="context",
        style=discord.TextStyle.long,
        placeholder="We have an Elon Musk for sale on the dark web...",
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Thanks for your message, {self.name.value}!', ephemeral=True)

        contactmsg_embed = discord.Embed(
            title="🚨contact message🚨",
            color=0xed0216
        )
        contactmsg_embed.set_thumbnail(url=interaction.user.display_avatar.url)
        contactmsg_embed.add_field(
            name=f"message sent by: {interaction.user.mention}",
            value=f'''
                                                        name: {self.name}
                                                        
                                                        subject: {self.subject}
                                                        
                                                        email: {self.email}
                                                        
                                                        message: 
                                                                ```{self.message}```
                                                    '''
        )

        await interaction.client.get_channel(channel_id).send(embed=contactmsg_embed)



    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)

        # Make sure we know what the error actually is
        traceback.print_exception(type(error), error, error.__traceback__)


class DevContact(ContactForm, title="Contact to zaal developer"):

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Thanks for your message, {self.name.value}!', ephemeral=True)

        contactmsg_embed = discord.Embed(
            title="🚨contact message to dev </>🚨",
            color=0xed0216
        )
        contactmsg_embed.set_thumbnail(url=interaction.user.display_avatar.url)
        contactmsg_embed.add_field(
            name=f"message sent by: {interaction.user.mention}",
            value=f'''
                                                        name: {self.name}
                                                        subject: {self.subject}
                                                        email: {self.email}
                                                        message: 
                                                                ```{self.message}```
                                                    '''
        )

        await interaction.client.get_channel(channel_id).send(embed=contactmsg_embed)

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)

        # Make sure we know what the error actually is
        traceback.print_exception(type(error), error, error.__traceback__)