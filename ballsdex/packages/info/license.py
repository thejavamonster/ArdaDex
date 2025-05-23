from typing import TYPE_CHECKING

import discord
from discord.ui import Button, View, button

if TYPE_CHECKING:
    from ballsdex.core.bot import BallsDexBot


class LicenseInfo(View):
    @button(label="License info")
    async def license_info(self, interaction: discord.Interaction["BallsDexBot"], button: Button):
        await interaction.response.send_message(
            "This bot is an instance of BallsDex-DiscordBot "
            "(hereinafter referred to as Ballsdex).\n"
            "Ballsdex is a free and open source application made available to the public and "
            "licensed under the MIT license. The full text of this license is attached below.\n",
            ephemeral=True,
            file=discord.File("LICENSE", filename="LICENSE.txt"),
        )
