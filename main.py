import discord
import os

# bot imported from discord.ext.commands module
# command is an object that wraps a function invoked by a text command in discord
# Command has the ability to use a Converter to change the types of its arguments

from discord.ext import commands

# bot initializer
# text command must start with ! prefix
bot = commands.Bot(command_prefix='!')


#event
@bot.event
async def on_ready():
  await bot.change_presence(activity = discord.Game('Fortnite'))
  print('We have logged in as {0.user}'.format(bot))


# uses bot.command() passing invocation command (name) as its argument. only called when !ping is mentioned in chat
# decorator
@bot.command(name='ping', help = 'ping + how many times you will ping')

# any command function (callback) must accept at least one parameter called ctx (context surrounding the invoked Command)
# Context holds data such as the cannel and guild that the user called the Command from

# pings whatever chat command was called in x times @ x member
async def pinging(ctx, harassTime: int, toHarass: discord.Member):
  for x in range(harassTime):
    await ctx.send('Harassing ' + toHarass.mention)

# dms user 
@bot.command(name='test', help = 'test')
async def test(ctx):
  await ctx.send()

bot.run(os.getenv('TOKEN'))
