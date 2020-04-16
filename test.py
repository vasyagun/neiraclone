import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('я онлайн')

@client.event
async def on_message(message):
    channel = message.channel
    if message.content.startswith('!каталик шип'):

        await channel.send('Итак, вот что мне известно он нем')
        
        emb = discord.Embed(title = 'Информация о катализаторе для оружия Шип', colour = discord.Color.dark_gold())
        emb.set_thumbnail(url= 'https://bungie.net/common/destiny2_content/icons/f1144dc4e0d95d87d63ecedc4d31c84c.jpg')
        emb.add_field(name = 'Если ты отличный парень тебе не светят никогда', value= 'такие девушки как звезды' )
        await channel.send(embed = emb)

       

   
client.run('NzAwMTIzNDMzNTgwNzU3MTYz.XpgHZA.laI9kGVOK2VaoGiTXKTQrf--_ps')