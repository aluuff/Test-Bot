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
    await bot.change_presence(activity=discord.Game('Fortnite'))
    print('We have logged in as {0.user}'.format(bot))


# uses bot.command() passing invocation command (name) as its argument. only called when !ping is mentioned in chat
# decorator
@bot.command(name='ping', help='ping + how many times you will ping')
# any command function (callback) must accept at least one parameter called ctx (context surrounding the invoked Command)
# Context holds data such as the cannel and guild that the user called the Command from

# pings whatever chat command was called in x times @ x member
async def pinging(ctx, harassTime: int, toHarass: discord.Member):
  if (toHarass.mention == '<@827452610361557022>'):
    await ctx.send('dont ping the bot u dummy')
  elif (toHarass.mention == '<@308118210832629760>'):
    await ctx.send('ha, cant ping julia C:< <:juliacool:822672611523297280>')
  else:
      for x in range(harassTime):
        await ctx.send('Harassing ' + toHarass.mention)


@bot.command(name='stinky', help='stinky')
async def test(ctx):
  await ctx.send('julia is stinky')


@bot.command(name='stinkier')
async def reallyStink(ctx, stinker: str, i: int):
  for x in range(i):
     await ctx.send(stinker + " is stinky")

#pings sean
@bot.command(name='sean')
async def sean(ctx):
  seanID = '<@151545192590213120>'
  await ctx.send(seanID + ' sean bot ping')
  
@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  if message.content == 'does sean stink':
    await message.channel.send('yes')
  
  await bot.process_commands(message)

bot.run(os.getenv('TOKEN'))
