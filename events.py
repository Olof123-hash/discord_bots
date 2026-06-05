from discord.ext import commands

channel_id = 1511678396504215562



class Events(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
         global channel 
         channel = await self.bot.fetch_channel(channel_id)
         print(channel)  # if this prints None the channel_id is wrong
         await channel.send("Hi, i am ready")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send(f"Welcome to the server {member.name}")

    @commands.Cog.listener()
    async def on_message(self, message):
      if message.author == self.bot.user:
          return
      

      if "shit" in message.content.lower():
          await message.delete()
          await message.channel.send(f"{message.author.mention} - dont use that word")

        
      await self.bot.process_commands(message)


        
      

    