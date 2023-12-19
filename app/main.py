import discord
from discord.ext import commands
from mylib.constant import EXTENSIONS, TOKEN, GUILD_ID


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="/",
            intents=discord.Intents.all(),
        )

    async def setup_hook(self):
        for extension in EXTENSIONS:
            await self.load_extension(extension)
        await self.tree.sync(guild=discord.Object(id=GUILD_ID))


if __name__ == "__main__":
    bot = MyBot()
    bot.run(token=TOKEN)
