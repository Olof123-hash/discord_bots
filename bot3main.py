from imports import Imports
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from commands import General
from events import Events
import asyncio
'MTUxMTM5MzU5MjczODg0NDc2Mg.G9QFPM.eg3TzNArSykch9cSqP5TKhewwmqsbd7RwbgTgk'
##

def configure ():
    load_dotenv()

channel_id = 1511678396504215562


intents = discord.Intents.default()
intents.members = True 
intents.message_content = True


bot = commands.Bot(command_prefix='!', intents=intents)

async def main():
    configure()
    await bot.add_cog(General(bot))
    await bot.add_cog(Events(bot))
    await bot.start(os.getenv('bot_token'))


asyncio.run(main())
