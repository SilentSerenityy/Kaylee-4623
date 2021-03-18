from discord.ext import commands
import discord
import random
import datetime

class listen(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_message(self,message):
    punc = [' ','.','!','?']
    if message.guild is None and not message.author.bot:
      tmpStr = message.content.lower()
      tmpStr = tmpStr.replace("cake","")
      for pun in punc:
        tmpStr = tmpStr.replace("cake"+pun,"")
      cake_check = (len(message.content)!=len(tmpStr))

      if (cake_check):
        await message.channel.send("UwU <:BlueberryCake:777631186365054986> is so tasty x3")
  
    if message.guild.id == 777563209061236746 and not message.author.bot:
      tmpStr = message.content.lower()
      tmpStr = tmpStr.replace("cake","")
      for pun in punc:
        tmpStr = tmpStr.replace("cake"+pun,"")
      cake_check = (len(message.content)!=len(tmpStr))

      if (cake_check):
        await message.channel.send("UwU <:BlueberryCake:777631186365054986> is so tasty x3")


def setup(bot):
  bot.add_cog(listen(bot))