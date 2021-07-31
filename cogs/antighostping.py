from discord.ext import commands
import discord
import random
import os
import json
import re

class guildevents(commands.Cog):
  def __init__(self,client):
    self.client = client


  @commands.Cog.listener()
  async def on_message_delete(self,message):
    #message = str(message)
    #mention = re.findall(r'[@]\S*', message)
    if "<@" in message.content:
      with open('antighostping.json', 'r', encoding='utf-8') as f:
          guilds_dict = json.load(f)
      channel_id = guilds_dict[str(message.guild.id)]
      await self.client.get_channel(int(channel_id)).send(f"{message.author.name} has done a ghost ping.\nMessage : ``{message.content}``")

  @commands.command()
  async def set_antighostping_channel(self,ctx, channel: discord.TextChannel):
      with open('antighostping.json', 'r', encoding='utf-8') as f:
          guilds_dict = json.load(f)

      guilds_dict[str(ctx.guild.id)] = str(channel.id)
      with open('antighostping.json', 'w', encoding='utf-8') as f:
          json.dump(guilds_dict, f, indent=4, ensure_ascii=False)
      
      await ctx.send(f'Sent anti-ghost-ping channel for {ctx.message.guild.name} to {channel.name}')

def setup(client):
  client.add_cog(guildevents(client))
