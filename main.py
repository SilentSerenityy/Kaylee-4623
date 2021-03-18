import ClientConfig
import discord
import B
import os
import asyncio

bot = ClientConfig.bot

async def status_task():
  while True:
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} servers!"))
    await asyncio.sleep(10)
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=f"ka!help"))
    await asyncio.sleep(10)


@bot.listen()
async def on_ready():
  print("Bot is Ready")
  print(f"Logged in as {bot.user}")
  print(f"Id: {bot.user.id}")
  await status_task()


B.b()
bot.run(os.environ["TOKEN"])