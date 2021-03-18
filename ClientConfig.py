import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix=commands.when_mentioned_or("ka!"),intents = discord.Intents.all())

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    try:
      bot.load_extension(f'cogs.{filename[:-3]}')
    except commands.errors.NoEntryPointError:
      pass