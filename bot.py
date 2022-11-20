from discord.ext import commands
import discord
import random
from readertxt import readtxt
from asyncio import sleep
from wordEditor import simplify_word
import os

TOKEN = os.environ['KEY']

VERSION = 1.09
DATE = 2022
INC = "FhBeast"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='*', intents=intents)

phrases = readtxt("phrases.txt")

ban_words = ['тест', 'текст']

ct = None


@bot.event
async def on_ready():
    print(f"{bot.user.name} v{VERSION} (c) {DATE} {INC}, inc")
    while True:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(""))
        await sleep(15)


@bot.command()
async def say(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send(random.choice(phrases))


@bot.command()
async def math(ctx):
    await ctx.send(random.choice(math_error))


@bot.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)


@bot.event
async def on_message(message):
    if message.author.bot:
        return
    msg_words = message.content.split()
    for i in range(len(msg_words)):
        msg_words[i] = simplify_word(msg_words[i])
    await message.channel.send(' '.join(msg_words))


bot.run(TOKEN)
