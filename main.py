from discord.ext import commands
import sys, traceback
from Loader import Loader

bot = commands.Bot(command_prefix=commands.when_mentioned_or("_"), description="Discord bot for starting An Aternos server")

loader = Loader()
discord_bot_token = loader.get_token()


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

if __name__ == '__main__':
    for extension in ["cogs.aternos"]:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load cog - {extension}.', file=sys.stderr)
            traceback.print_exc()

bot.run(discord_bot_token)