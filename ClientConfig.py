import discord, os, aiosqlite3, aiohttp
from discord.ext import commands

class Kaylee(commands.Bot):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.special_access = {}

  async def start(self,*args, **kwargs):
    self.session=aiohttp.ClientSession()
    self.sus_users = await aiosqlite3.connect('sus_users.db')
    await super().start(*args, **kwargs)

  async def close(self):
    await self.session.close()
    await self.sus_users.close()
    await super().close()

bot = Kaylee(command_prefix=commands.when_mentioned_or("ka!"),intents = discord.Intents.all())

bot.load_extension('jishaku')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    try:
      bot.load_extension(f'cogs.{filename[:-3]}')
    except commands.errors.NoEntryPointError:
      pass

