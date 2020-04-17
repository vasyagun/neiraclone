import discord
from discord.ext import commands
import os

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
        emb.add_field(name= 'Title', value= 'Скорбь... Готовли ты познать всю глубину отчаяния?                                                                                              .')
        emb.add_field(name= 'Условие для получения', value= 'Группой из 3 стражей, вооружившись оружеем скорби. Убить Зулмака Орудее Пыток ни разу не умерев                                 .')
        emb.add_field(name= 'Задание катализатора', value= 'Убить стража в патрульной зоне, в любой точке Солнечной системы                                                                  .')
        emb.add_field(name= 'Бонус катализатора', value= 'Повышает дальность, стабильность. А также открывает скрытый перк Взглять тьмы - позволяет видеть носителей света в радиусе 20 метров')
        await channel.send(embed = emb)

       

   
token = os.environ.get('BOT_TOKEN')

client.run(str(token))
