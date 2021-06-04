

import discord
from discord.ext import commands, tasks
import asyncio
import discord.utils
import datetime
import time
import random
from random import choice

class kidnap(commands.Cog):
    def __init__(self, client):
        self.client = client
    

    @commands.command()
    async def kidnap(self,ctx, member : discord.Member):
      embed = discord.Embed(title = f"{ctx.author.name} has taken {member.name} to Brazil lmao")
      embed.set_image(url = 'https://tenor.com/view/brazil-youre-going-to-brazil-car-junk-gif-17878610')
      embed.set_footer(text=f"Have fun {member.name}")
      await ctx.send(embed=embed)
        
def setup(client):
  client.add_cog(kidnap(client))
