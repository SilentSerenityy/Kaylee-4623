import random , discord , aiohttp , os , aiosqlite3
from discord.ext import commands, menus
from utils import BetterMemberConverter, BetterUserconverter

class Owner(commands.Cog):
  def __init__(self, bot):
    self.client = bot
    self.bot = bot

  async def cog_command_error(self,ctx,error):
    if ctx.command and ctx.command.has_error_handler():
      pass
    else:
      await ctx.send(error)

  async def cog_check(self, ctx):
    return await self.client.is_owner(ctx.author)

  class SusUsersEmbed(menus.ListPageSource):
    async def format_page(self, menu, item):
      embed=discord.Embed(title = "Users Deemed Suspicious by JDJG Inc. Official", color=random.randint(0, 16777215))
      embed.add_field(name = f"User ID : {item[0]}", value = f"**Reason :** {item[1]}", inline = False)
      return embed

  @commands.command(brief="A command to add sus_users with a reason")
  async def addsus(self,ctx,*,user:BetterUserconverter=None):
    if user is None:
      await ctx.send("can't have a user be none.")
    
    def check(m):
      return m.author.id == ctx.author.id

    if user:
      await ctx.reply("Please give me a reason why:")
      reason = await self.client.wait_for("message",check=check)
      cur = await self.client.sus_users.cursor()
      await cur.execute("INSERT INTO sus_users VALUES (?, ?)", (user.id, reason.content))
      await self.client.sus_users.commit()
      await cur.close()
      await ctx.send("added sus users, succesfully")

  @commands.command(brief="a command to remove sus users.")
  async def removesus(self,ctx,*,user:BetterUserconverter=None):
    if user is None:
      await ctx.send("You can't have a none user.")

    if user:
      cur = await self.client.sus_users.cursor()
      await cur.execute("DELETE FROM sus_users WHERE user_id = ?", (user.id,))
      await self.client.sus_users.commit()
      await cur.close()
      await ctx.send("Removed sus users.")

    class SusUsersEmbed(menus.ListPageSource):
      async def format_page(self, menu, item):
        embed=discord.Embed(title = "Users Deemed Suspicious by JDJG Inc. Official", color=random.randint(0, 16777215))
        embed.add_field(name = f"User ID : {item[0]}", value = f"**Reason :** {item[1]}", inline = False)
        return embed

  @commands.command(brief="a command to grab all in the sus_users list")
  async def sus_users(self,ctx):
    cur = await self.client.sus_users.cursor()
    sus_users=([n for n in await cur.execute("SELECT * FROM SUS_USERS;")])
    await cur.close()
    await self.client.sus_users.commit()  
    menu = menus.MenuPages(self.SusUsersEmbed(sus_users, per_page=1),delete_message_after=True)
    await menu.start(ctx)

  @commands.command()
  async def update_sus(self,ctx):
    await self.client.sus_users.commit()
    await ctx.send("Updated SQL boss.")

  @update_sus.error
  async def update_sus_error(self,ctx,error):
    await ctx.send(error)

def setup(client):
  client.add_cog(Owner(client))
 