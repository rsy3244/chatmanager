from discord.ext import commands
import discord
import os

TOKEN = os.environ['DISCORD_BOT_TOKEN']
GUILD_ID = os.environ['DISCORD_BOT_GUILD_ID']
CHANNEL_ID = os.environ['DISCORD_BOT_CHANNEL_ID']

class ChatManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.chat_channel = None

    @commands.Cog.listener()
    async def on_ready(self):
        print("ready")
        guild = self.bot.get_guild(554668279541792794)
        self.chat_channel = guild.get_channel(770572504980389889)
        print("""guild name: {}
        channel_name: {}""".format(guild.name, self.chat_channel.name))

    @commands.Cog.listener()
    async def on_message(self, message):
        print("message {} in {}".format(message.content, message.channel))
        print("{} {}".format(message.channel.id, self.chat_channel.id))
        if message.channel == self.chat_channel:
            print("delete message:")
            print(message)
            #遅延時間を設定できるようにする
            await message.delete(delay=7200)
            print("{} deleted".format(message.id))


bot = commands.Bot(command_prefix='!')
bot.add_cog(ChatManager(bot))

bot.run("MzM3MjM2OTAwMTEwNjYzNjgw.WW9qVg.FlX69k3sT-tgze_iVHf2LgCpqFg")
