from discord.ext import commands
from utils import BetterMemberConverter, BetterUserconverter, guildinfo
import re, discord , random , typing

class Info(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command(help="gives you info about a guild",aliases=["server_info","guild_fetch","guild_info","fetch_guild","guildinfo",])
  async def serverinfo(self,ctx,*,args=None):
    if args:
      match=re.match(r'(\d{16,21})',args)
      guild=self.client.get_guild(int(match.group(0)))
      if guild is None:
        guild = ctx.guild

    if args is None:
      guild = ctx.guild

    if guild is None:
      await ctx.send("Guild wanted has not been found")
    
    await guildinfo(ctx,guild)
    
  @commands.command(aliases=["user info", "user_info","user-info","whois"],brief="a command that gives information on users",help="this can work with mentions, ids, usernames, and even full names.")
  async def userinfo(self,ctx,*,user: BetterUserconverter = None):
    user = user or ctx.author
    user_type = user_type = ['User', 'Bot'][user.bot]
    
    if ctx.guild:
      member_version=ctx.guild.get_member(user.id)
      if member_version:
        nickname = str(member_version.nick)
        joined_guild = member_version.joined_at.strftime('%m/%d/%Y %H:%M:%S')
        status = str(member_version.status).upper()
        highest_role = member_version.roles[-1]
      if not member_version:
        nickname = str(member_version)
        joined_guild = "N/A"
        status = "Unknown"
        for guild in self.client.guilds:
          member=guild.get_member(user.id)
          if member:
            status=str(member.status).upper()
            break
        highest_role = "None Found"
    if not ctx.guild:
        nickname = "None"
        joined_guild = "N/A"
        status = "Unknown"
        for guild in self.client.guilds:
          member=guild.get_member(user.id)
          if member:
            status=str(member.status).upper()
            break
        highest_role = "None Found"
    
    guilds_list=[guild for guild in self.client.guilds if guild.get_member(user.id) and guild.get_member(ctx.author.id)]
    if not guilds_list:
      guild_list = "None"

    x = 0
    for g in guilds_list:
      if x < 1:
        guild_list = g.name
      if x > 0:
        guild_list = guild_list + f", {g.name}"
      x = x + 1

    embed=discord.Embed(title=f"{user}",description=f"Type: {user_type}", color=random.randint(0, 16777215),timestamp=ctx.message.created_at)
    embed.add_field(name="Username: ", value = user.name)
    embed.add_field(name="Discriminator:",value=user.discriminator)
    embed.add_field(name="Nickname: ", value = nickname)
    embed.add_field(name="Joined Discord: ",value = (user.created_at.strftime('%m/%d/%Y %H:%M:%S')))
    embed.add_field(name="Joined Guild: ",value = joined_guild)
    embed.add_field(name="Mutual Guilds:", value=guild_list)
    embed.add_field(name="ID:",value=user.id)
    embed.add_field(name="Status:",value=status)
    embed.add_field(name="Highest Role:",value=highest_role)
    embed.set_image(url=user.avatar_url)
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Info(client))