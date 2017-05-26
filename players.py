import discord
from discord.ext import commands

class Players():
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def