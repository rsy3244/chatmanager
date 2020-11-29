from discord.ext import commands
import discord
import os

from datetime import datetime, timedelta

TOKEN = os.environ['DISCORD_BOT_TOKEN']
GUILD_ID = int(os.environ['DISCORD_BOT_GUILD_ID'])
CHANNEL_ID = int(os.environ['DISCORD_BOT_CHANNEL_ID'])

class ChatManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.chat_channel = None
        self.lifetime = timedelta(hours=2)

    @commands.Cog.listener()
    async def on_ready(self):
        print("ready")
        guild = self.bot.get_guild(GUILD_ID)
        self.chat_channel = guild.get_channel(CHANNEL_ID)
        print("""guild name: {}
channel_name: {}""".format(guild, self.chat_channel))

        #delete messages wich are sent before 2 hours ago
        old_messages = await self.chat_channel.history(before=datetime.now()-self.lifetime).flatten()
        await self.chat_channel.delete_messages(old_messages)


    @commands.Cog.listener()
    async def on_message(self, message):
        print("message {} in {}".format(message.content, message.channel))
        print("{} {}".format(message.channel.id, self.chat_channel.id))
        if message.channel == self.chat_channel:
            print("delete message:")
            print(message)
            #遅延時間を設定できるようにする
            print("timeleft: {}".format(self.lifetime.total_seconds()))
            await asyncio.sleep(self.lifetime.total_seconds())
            await message.delete()
            print("{} deleted".format(message.id))


bot = commands.Bot(command_prefix='!')
bot.add_cog(ChatManager(bot))

bot.run(TOKEN)
