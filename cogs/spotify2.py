import discord
import requests
import dateutil.parser
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw

import re
 
 
def rgb_to_hex(rgb_color):
    rgb_color = re.search('\(.*\)', rgb_color).group(0).replace(' ', '').lstrip('(').rstrip(')')
    [r, g, b, a] = [int(x) for x in rgb_color.split(',')]
    # check if in range 0~255
    assert 0 <= r <= 255
    assert 0 <= g <= 255
    assert 0 <= b <= 255
    assert 0 <= a <= 255
 
    r = hex(r).lstrip('0x')
    g = hex(g).lstrip('0x')
    b = hex(b).lstrip('0x')
    a = hex(a).lstrip('0x')
    # re-write '7' to '07'
    r = (2 - len(r)) * '0' + r
    g = (2 - len(g)) * '0' + g
    b = (2 - len(b)) * '0' + b
    a = (2 - len(a)) * '0' + a
 
    hex_color = '#' + r + g + b + a
    return hex_color

class Spotify(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def spotify2(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        spotify_result = next((activity for activity in user.activities if isinstance(activity, discord.Spotify)), None)
        if spotify_result is None:
            await ctx.send(f'{user.name} is not listening to Spotify.')

        album_image = Image.open(requests.get(spotify_result.album_cover_url, stream=True).raw).convert('RGBA')

        url = spotify_result.album_cover_url
        urll = "https://cdn.discordapp.com/emojis/585766969144508416.png?v=1"

        embed = discord.Embed(title = f"{ctx.author.name} is listening to Spotify", icon_url=(urll))

        embed.set_thumbnail(url = url)

        embed.add_field(name = f"{spotify_result.title}\n{spotify_result.artist}\n{spotify_result.album}", value = "_ _" ,inline = False)

        embed.set_footer(text = f"00:00   ━●━━━━━━━━━   {dateutil.parser.parse(str(spotify_result.duration)).strftime('%M:%S')}")
        await ctx.send(embed = embed)


def setup(client):
    client.add_cog(Spotify(client))
