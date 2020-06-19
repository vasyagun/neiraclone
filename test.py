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

 if message.content.startswith('!правила '):

        await channel.send(f'Eyes up!,{author.name} Рады видеть тебя сдесь!')
        
        emb = discord.Embed(title = 'Небольшой вводный инструктаж', colour = discord.Color.dark_gold())
        emb.set_thumbnail(url= 'https://d.newsweek.com/en/full/1582182/us-health-virus-briefing.jpg?w=790&f=a9624484819a8f1a99321f2425232bb0')
        emb.add_field(name= 'q: Что это за место?', value= 'a: Сервер для выдоцев ИС и их друзей.',  inline= False)
        emb.add_field(name= 'q: Зачем это надо?', value= 'a: Попытка избежать: репресий, застоя, безразличия, токсичности.', inline= False)
        emb.add_field(name= 'q: А надо вступать в клан? ', value= 'a: Необязательно. Можешь состоять в чем хочешь: клан, пати, Единая Россия. Но если чешется, вот ссылка https://www.bungie.net/ru/ClanV2?groupid=4271047 ', inline= False)
        emb.add_field(name= 'q: А что с ролями?', value= 'Любую роль вы можете получить при обращении в небесную канцелярию(синего цвета)')
        emb.add_field(name= '@Админ', value= 'кто это вообще?')
        emb.add_field(name= '@Модер', value= 'а это зачем?')
        emb.add_field(name= '@вопрос', value= 'если что-то интересует, можно упомянуть в любом канале и получить ответ.')
        emb.add_field(name= '@Техно Ведьма', value= 'верные подруги Мары Сов :9509_Mara_Sov_Joy:')
        emb.add_field(name= '@Страж', value= 'стандартная роль')
        emb.add_field(name= '@pvp God', value= 'роль для сасирисных бойцов с КДА>0.95')
        emb.add_field(name= '@Helper', value= 'человечек который может протащить по большинству квестов/активностей')
        emb.add_field(name= '@Криптах', value= 'шарит за все, что происходит в игре. Адепт видосов MadnessBuccanner')
      
        
        await channel.send(embed = emb)       

   
token = os.environ.get('BOT_TOKEN')

client.run(str(token))
