#from https://github.com/jmtaber129/discord-bot

from ctypes.util import find_library
import discord
from discord.ext import commands
from discord import opus



class VoiceBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load_opus()

    async def on_ready(self):
        print('Logged in as')
        print(self.bot.user.name)
        print(self.bot.user.id)
        print('------')

    def load_opus(self):
        opus_path = find_library('opus')
        opus.load_opus(opus_path)
        if not opus.is_loaded():
            print('Opus was not loaded')
            self.bot.loop.stop()

    @commands.command(pass_context=True)
    async def rickroll(self, ctx, *, requested_channel: str):
        """ Joins and Rick-Rolls the specified channel name.
        Command use: '!rickroll <channel_name>' """
        if self.bot.is_voice_connected(ctx.message.server):
            await discord.utils.get(self.bot.voice_clients, server=ctx.message.server).disconnect()

        # channel checks
        voice_channel = discord.utils.get(ctx.message.server.channels, name=requested_channel)
        
        if voice_channel == None:
            await self.bot.say(
                'Channel "' + requested_channel +
                '" does not exist. (Channel names are case-sensitive)')
            return
        if voice_channel.type != discord.ChannelType.voice:
            await self.bot.say(
                'Channel "' + requested_channel +
                '" is not a voice channel. (Channel names are case-sensitive)')
            return

        #connects bot
        voice_client = await self.bot.voice_channel.connect()

        yt_player = await voice_client.create_ytdl_player('https://www.youtube.com/watch?v=dQw4w9WgXcQ', after=lambda: self.bot.loop.create_task(voice_client.disconnect()))

        print('Player loaded.')
        yt_player.volume = 0.3
        yt_player.start()

    @commands.command(pass_context=True)
    async def disconnect(self, ctx):
        """ Disconnects the current voice client on the server. """
        await discord.utils.get(self.bot.voice_clients, server=ctx.message.server).disconnect()


def setup(bot):
    bot.add_cog(VoiceBot(bot))
