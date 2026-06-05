from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def members(self, ctx):
        all_members = [str(member) for member in ctx.guild.members if member != self.bot.user]
        await ctx.send("\n".join(all_members))

    @commands.command()
    async def assing(ctx):
         pass