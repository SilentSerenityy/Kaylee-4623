import discord
from discord.ext import commands
import random
import random
import asyncio
import aiohttp

class emote(commands.Cog):
  def __init__(self, client):
      self.client = client

  @commands.command(brief="gives a random kawaii emoji.",aliases=["ka"])
  async def kawaii_random(self,ctx,*,message=None,amount=1):
    if message is None:
      await ctx.send("You don't want to say anything cute?")
    kawaii_emotes= self.client.get_guild(773571474761973840)
    kawaii_emotes2 = self.client.get_guild(806669712410411068)
    kawaii_emotes3 = self.client.get_guild(692576207404793946)
    emoji_choosen = random.choice(kawaii_emotes.emojis+kawaii_emotes2.emojis+kawaii_emotes3.emojis)
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"{message} {emoji_choosen}")


def setup(client):
    client.add_cog(emote(client))