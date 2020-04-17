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
    author = message.author
    content = message.content
    print('{}:{}'.format(author.name, content))
    if message.content.startswith('!каталик шип'):

        await channel.send(f'Итак,{author.name} вот что мне известно он нем')
        
        emb = discord.Embed(title = 'Информация о катализаторе для оружия Шип', colour = discord.Color.dark_gold())
        emb.set_thumbnail(url= 'https://bungie.net/common/destiny2_content/icons/f1144dc4e0d95d87d63ecedc4d31c84c.jpg')
        emb.add_field(name= 'Описание', value= 'Скорбь... Готов ли ты познать всю глубину отчаяния?⁣⁣⁣⁣⁣',  inline= False)
        emb.add_field(name= 'Условие для получения', value= 'Группой из 3 стражей, вооружившись оружием скорби (Шип). Убить Зулмака Орудие Пыток, ни разу не умерев', inline= False)
        emb.add_field(name= 'Задание катализатора', value= 'Убить стража в патрульной зоне, в любой точке Солнечной системы', inline= False)
        emb.add_field(name= 'Бонус катализатора', value= 'Повышает дальность, стабильность. А также открывает скрытый перк "Взгляд тьмы" - позволяет видеть носителей света в радиусе 20 метров')
        

        await channel.send(embed = emb)

    if message.content.startswith('!катализатор шип'):

        await channel.send(f'Итак,{author.name} вот что мне известно он нем')
        
        emb = discord.Embed(title = 'Информация о катализаторе для оружия Шип', colour = discord.Color.dark_gold())
        emb.set_thumbnail(url= 'https://bungie.net/common/destiny2_content/icons/f1144dc4e0d95d87d63ecedc4d31c84c.jpg')
        emb.add_field(name= 'Описание', value= 'Скорбь... Готов ли ты познать всю глубину отчаяния?⁣⁣⁣⁣⁣',  inline= False)
        emb.add_field(name= 'Условие для получения', value= 'Группой из 3 стражей, вооружившись оружием скорби (Шип). Убить Зулмака Орудие Пыток, ни разу не умерев', inline= False)
        emb.add_field(name= 'Задание катализатора', value= 'Убить стража в патрульной зоне, в любой точке Солнечной системы', inline= False)
        emb.add_field(name= 'Бонус катализатора', value= 'Повышает дальность, стабильность. А также открывает скрытый перк "Взгляд тьмы" - позволяет видеть носителей света в радиусе 20 метров')
        

        await channel.send(embed = emb)
    
    if message.content.startswith('!каталик ластворд'):

        await channel.send(f'Итак,{author.name} вот что мне известно он нем')
        
        emb = discord.Embed(title = 'Информация о катализаторе для оружия Ластворд', colour = discord.Color.dark_gold())
        emb.set_thumbnail(url= 'https://bungie.net/common/destiny2_content/icons/66fbe54a24d5a2b9978c909eb15ab62d.jpg')
        emb.add_field(name= 'Описание', value= 'Ты ведь ковбой да?! Вот и веди себя соответствующе!',  inline= False)
        emb.add_field(name= 'Условие для получения', value= 'Вызвать на дуэль Лорда Шакса, на пике Фелвинтера (карта в pvp)', inline= False)
        emb.add_field(name= 'Задание катализатора', value= 'Загнать всех собак в загон, в недрах Левиафана', inline= False)
        emb.add_field(name= 'Бонус катализатора', value= 'Увеличивает скорострельность от бедра до 360 rpm, а также увеличивает емкость магазина до 20 ед.')
        

        await channel.send(embed = emb)

    if message.content.startswith('!катализатор ластворд'):

        await channel.send(f'Итак,{author.name} вот что мне известно он нем')
        
        emb = discord.Embed(title = 'Информация о катализаторе для оружия Ластворд', colour = discord.Color.dark_gold())
        emb.set_thumbnail(url= 'https://bungie.net/common/destiny2_content/icons/66fbe54a24d5a2b9978c909eb15ab62d.jpg')
        emb.add_field(name= 'Описание', value= 'Ты ведь ковбой, да?! Вот и веди себя сответственно!',  inline= False)
        emb.add_field(name= 'Условие для получения', value= 'Вызвать на дуэль Лорда Шакса, на пике Фелвинтера (карта в pvp)', inline= False)
        emb.add_field(name= 'Задание катализатора', value= 'Загнать всех собак в загон, в недрах Левиафана', inline= False)
        emb.add_field(name= 'Бонус катализатора', value= 'Увеличивает скорострельность от бедра до 360 rpm, а также увеличивает емкость магазина до 20 ед.')
        

        await channel.send(embed = emb)

    if message.content.startswith('!каталик ласт ворд'):

        await channel.send(f'Итак,{author.name} вот что мне известно он нем')
        
        emb = discord.Embed(title = 'Информация о катализаторе для оружия Ластворд', colour = discord.Color.dark_gold())
        emb.set_thumbnail(url= 'https://bungie.net/common/destiny2_content/icons/66fbe54a24d5a2b9978c909eb15ab62d.jpg')
        emb.add_field(name= 'Описание', value= 'Ты ведь ковбой, да?! Вот и веди себя сответственно!',  inline= False)
        emb.add_field(name= 'Условие для получения', value= 'Вызвать на дуэль Лорда Шакса, на пике Фелвинтера (карта в pvp)', inline= False)
        emb.add_field(name= 'Задание катализатора', value= 'Загнать всех собак в загон, в недрах Левиафана', inline= False)
        emb.add_field(name= 'Бонус катализатора', value= 'Увеличивает скорострельность от бедра до 360 rpm, а также увеличивает емкость магазина до 20 ед.')
        

        await channel.send(embed = emb)

    if message.content.startswith('!катализатор ласт ворд'):

        await channel.send(f'Итак,{author.name} вот что мне известно он нем')
        
        emb = discord.Embed(title = 'Информация о катализаторе для оружия Ластворд', colour = discord.Color.dark_gold())
        emb.set_thumbnail(url= 'https://bungie.net/common/destiny2_content/icons/66fbe54a24d5a2b9978c909eb15ab62d.jpg')
        emb.add_field(name= 'Описание', value= 'Ты ведь ковбой, да?! Вот и веди себя сответственно!',  inline= False)
        emb.add_field(name= 'Условие для получения', value= 'Вызвать на дуэль Лорда Шакса, на пике Фелвинтера (карта в pvp)', inline= False)
        emb.add_field(name= 'Задание катализатора', value= 'Загнать всех собак в загон, в недрах Левиафана', inline= False)
        emb.add_field(name= 'Бонус катализатора', value= 'Увеличивает скорострельность от бедра до 360 rpm, а также увеличивает емкость магазина до 20 ед.')
        

        await channel.send(embed = emb)

    if message.content.startswith('!каталик последнее слово'):

        await channel.send(f'Итак,{author.name} вот что мне известно он нем')
        
        emb = discord.Embed(title = 'Информация о катализаторе для оружия Ластворд', colour = discord.Color.dark_gold())
        emb.set_thumbnail(url= 'https://bungie.net/common/destiny2_content/icons/66fbe54a24d5a2b9978c909eb15ab62d.jpg')
        emb.add_field(name= 'Описание', value= 'Ты ведь ковбой, да?! Вот и веди себя сответственно!',  inline= False)
        emb.add_field(name= 'Условие для получения', value= 'Вызвать на дуэль Лорда Шакса, на пике Фелвинтера(карта в pvp)', inline= False)
        emb.add_field(name= 'Задание катализатора', value= 'Загнать всех собак в загон, в недрах Левиафана', inline= False)
        emb.add_field(name= 'Бонус катализатора', value= 'Увеличивает скорострельность от бедра до 360 rpm, а также увеличивает емкость магазина до 20 ед.')
        

        await channel.send(embed = emb)

    if message.content.startswith('!катализатор последнее слово'):

        await channel.send(f'Итак,{author.name} вот что мне известно он нем')
        
        emb = discord.Embed(title = 'Информация о катализаторе для оружия Ластворд', colour = discord.Color.dark_gold())
        emb.set_thumbnail(url= 'https://bungie.net/common/destiny2_content/icons/66fbe54a24d5a2b9978c909eb15ab62d.jpg')
        emb.add_field(name= 'Описание', value= 'Ты ведь ковбой, да?! Вот и веди себя сответственно!',  inline= False)
        emb.add_field(name= 'Условие для получения', value= 'Вызвать на дуэль Лорда Шакса, на пике Фелвинтера(карта в pvp)', inline= False)
        emb.add_field(name= 'Задание катализатора', value= 'Загнать всех собак в загон, в недрах Левиафана', inline= False)
        emb.add_field(name= 'Бонус катализатора', value= 'Увеличивает скорострельность от бедра до 360 rpm, а также увеличивает емкость магазина до 20 ед.')
        

        await channel.send(embed = emb)

       

   
token = os.environ.get('BOT_TOKEN')

client.run(str(token))
