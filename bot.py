from discord.ext import commands
import discord
import random
from Parser import parse_ya
from readertxt import readtxt
from asyncio import sleep
import os

TOKEN = os.environ['KEY']

VERSION = 1.09
DATE = 2021
INC = "FhBeast"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='*', intents=intents)

phrases = readtxt("phrases.txt")
math_error = readtxt("mathError.txt")
ask_error = readtxt("askError.txt")

ct = None


@bot.event
async def on_ready():
    print(f"{bot.user.name} v{VERSION} (c) {DATE} {INC}, inc")
    while True:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game("Portal"))
        await sleep(15)


@bot.command()
async def say(ctx):
    await ctx.channel.purge(limit=1)
    #await ctx.send(random.choice(phrases))
    print(phrases[0])


@bot.command()
async def math(ctx):
    await ctx.send(random.choice(math_error))


@bot.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)


@bot.command()
async def ask(ctx, *args):
    text = ""
    for arg in args:
        text += arg + " "
    answer = parse_ya(text)
    if answer == "Error":
        answer = random.choice(ask_error)
    await ctx.send(answer)


bot.run(TOKEN)
