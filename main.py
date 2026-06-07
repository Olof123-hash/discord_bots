import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio
from claudetest import AI


intents = discord.Intents.default()
intents.members = True 
intents.message_content = True


bot = commands.Bot(command_prefix='!', intents=intents)

ai = AI()

load_dotenv()

@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")


@bot.command()
async def get_help(ctx):
    acommands = []
    await ctx.send(f"Here is a list of all available commands {acommands}!")


##removes messages
@bot.command()
@commands.has_permissions(manage_messages=True) 
#only those with the permission to manage messages can use this command

async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"{amount} message(s) got deleted")



@bot.command()
async def ask_bot(ctx, *, question: str):
    async with ctx.typing():  # Shows "Bot is typing..." while waiting
        response = ai.ask(question)
        await ctx.send(response)

@bot.command()
async def about(ctx, *, question:str):
    async with ctx.typing():
        response = ai.about(question)
        await ctx.send(response)

async def main():
    await bot.start(os.getenv('bot_token'))




asyncio.run(main())