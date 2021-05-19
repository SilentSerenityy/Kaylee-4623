from discord.ext import commands
import discord, random, aiosqlite3

class Moderation(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(help="a command to scan for malicious bots, specificially ones that only give you random invites and are fake(work in progress)")
  async def scan_guild(self,ctx):
    
    if isinstance(ctx.channel, discord.TextChannel):
      cur = await self.client.sus_users.cursor()
      sus_users=dict([n for n in await cur.execute("SELECT * FROM SUS_USERS;")])
      await cur.close()
      count = 0
      for x in sus_users:
        user=ctx.guild.get_member(x)
        if user:
          count = count + 1
          await ctx.send(f"Found {x}. \nUsername: {user.name} \nReason: {sus_users[x]}")
          
      if count < 1:
        await ctx.send("No Bad users found.")
        
    if isinstance(ctx.channel,discord.DMChannel):
      await ctx.send("please use the global version")

def setup(client):
  client.add_cog(Moderation(client))
