from discord.ext import commands
from python_aternos import Client
from Loader import Loader


class Aternos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.loader = Loader()
        username, password = self.loader.get_credentials()
        if self.loader.get_hashed():
            self.aternos = Client.from_hashed(username, password)
        else:
            self.aternos = Client.from_credentials(username, password)
        self.loader.hash_data(self.aternos)

    @commands.command()
    async def checkonline(self, ctx):
        await ctx.send(f"The server is {str(self.aternos.list_servers()[0].status)}")

    @commands.command()
    async def startserver(self, ctx):
        if self.aternos.list_servers()[0].status == "online":
            await ctx.send("The server is already online.")
        else:
            server = self.aternos.list_servers()[0]
            server.start()

    @commands.command()
    async def stopserver(self, ctx):
        if self.aternos.list_servers()[0].status == "offline":
            await ctx.send("The server is already offline.")
        else:
            server = self.aternos.list_servers()[0]
            server.stop()

    @commands.command()
    async def getip(self, ctx):
        await ctx.send(self.aternos.list_servers()[0].address)


def setup(bot):
    bot.add_cog(Aternos(bot))