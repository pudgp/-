import discord
from discord.ext import commands
import random
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
bot = discord.Client(intents=discord.Intents.all())
@bot.event
async def on_ready():
    print(f'{bot.user.name} запустился и готов к работе!')

@bot.command()
async def advice(ctx):
  await random.choice(ctx.send('Не бросайте мусор на улице!' 'Носите с собой многоразовые пакеты и контейнеры'))

@bot.command()
async def info(ctx):
  await ctx.send('!advice - дает совет')

@bot.command()
async def test(ctx):
  await ctx.send('Время разложения пластика равно от 400 до 700 лет, стекло разлагается тысячу лет, обычная бумага и картон разлагаются за 1-2 месяца')









bot.run(TOKEN)