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
    async def spotify(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        spotify_result = next((activity for activity in user.activities if isinstance(activity, discord.Spotify)), None)
        if spotify_result is None:
            await ctx.send(f'{user.name} is not listening to Spotify.')
        album_image = Image.open(requests.get(spotify_result.album_cover_url, stream=True).raw).convert('RGBA')
        album_color = album_image.getpixel((250, 100))
        print(album_color)
        rgb_input = f"{album_color}"
        hex_output = rgb_to_hex(rgb_input)
        aa = hex_output
        bb = aa.replace('#', '')
        cc = bb.replace('ff', '')

        a = cc.replace('a', '0')
        b = a.replace('b', '1')
        c = b.replace('c', '2')
        d = c.replace('d', '3')
        e = d.replace('e', '4')
        f = e.replace('f', '5') 
        g = f.replace('g', '6')
        h = g.replace('h', '7')
        i = h.replace('i', '8') 
        j = i.replace('j', '9')
        k = j.replace('k', '0')
        l = k.replace('l', '1') 
        m = l.replace('m', '2')
        n = m.replace('n', '3')
        o = n.replace('o', '4') 
        p = o.replace('p', '5')
        q = p.replace('q', '6')
        r = q.replace('r', '7') 
        s = r.replace('s', '8')
        t = s.replace('t', '9')
        u = t.replace('u', '0') 
        v = u.replace('v', '1')
        w = v.replace('w', '2')
        x = w.replace('x', '3') 
        y = x.replace('y', '4')
        z = y.replace('z', '5')

        color = int(z)
        url = spotify_result.album_cover_url
        embed = discord.Embed(title = f"{ctx.author.name} is currently listening to Spotify",color = color)
        embed.set_image(url = url)
        embed.add_field(name = "Song Name:", value = f"{spotify_result.title}",inline = False)
        embed.add_field(name = "Artists:", value = f"{spotify_result.artist}",inline = False)
        embed.add_field(name = "Album:", value = f"{spotify_result.album}",inline = False)
        embed.add_field(name = "Duration:", value = f"{dateutil.parser.parse(str(spotify_result.duration)).strftime('%M:%S')}",inline = False)
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Spotify(client))
