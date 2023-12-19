import discord
from discord.ext import commands
from discord import app_commands
from mylib.constant import GUILD_ID


class SlashPing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.guilds(discord.Object(id=GUILD_ID))
    @app_commands.command(name="ping", description="pong!と返します。")
    async def ping(self, interaction):
        await interaction.response.send_message("pong!")


async def setup(bot):
    await bot.add_cog(SlashPing(bot))
