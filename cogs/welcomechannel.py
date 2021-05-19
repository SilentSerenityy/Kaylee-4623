from discord.ext import commands
import discord
import random
import os
import json

class guildevents(commands.Cog):
  def __init__(self,client):
    self.client = client


  @commands.Cog.listener()
  async def on_member_join(self,member):
    with open('welcomechannel.json', 'r', encoding='utf-8') as f:
        guilds_dict = json.load(f)
    channel_id = guilds_dict[str(member.guild.id)]
    embed=discord.Embed(title=f"Welcome {member.name}!!",description=f"To {member.guild.name}", color=random.randint(0, 16777215))
    embed.add_field(name = "What to do here?", value = "Chat with the members, have fun, and just generally enjoy it!", inline = False)
    embed.add_field(name = "Remember to-", value = "Read all rules and show respect to everyone in the server.", inline = False)
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_image(url='https://cdn.discordapp.com/attachments/744185901273448458/815310508844122112/LO2IzCa.gif')
    await self.client.get_channel(int(channel_id)).send(embed=embed)

  @commands.command()
  async def set_welcome_channel(self,ctx, channel: discord.TextChannel):
      with open('welcomechannel.json', 'r', encoding='utf-8') as f:
          guilds_dict = json.load(f)

      guilds_dict[str(ctx.guild.id)] = str(channel.id)
      with open('welcomechannel.json', 'w', encoding='utf-8') as f:
          json.dump(guilds_dict, f, indent=4, ensure_ascii=False)
      
      await ctx.send(f'Sent welcome channel for {ctx.message.guild.name} to {channel.name}')

def setup(client):
  client.add_cog(guildevents(client))
