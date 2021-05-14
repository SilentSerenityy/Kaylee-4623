from discord.ext import commands
import discord, random, aiosqlite3

class dehoist(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def dehoistnickname(self,ctx,symbol):
    nick = None
    for member in ctx.guild.members:
      obj = str(symbol)
      nickname = str(member.nick)
      if nickname.startswith(obj):
        await member.edit(nick=None)
        await ctx.send(f"{member.name} has been de-hoisted!")

  @commands.command()
  async def dehoistname(self,ctx,symbol):
    nick = None
    for member in ctx.guild.members:
      obj = str(symbol)
      dispname = str(member.name)
      if dispname.startswith(obj):
        await member.edit(nick=None)
        await ctx.send(f"{member.name} has been de-hoisted!")
      

def setup(client):
  client.add_cog(dehoist(client))