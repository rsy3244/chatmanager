from discord.ext import commands
import discord
import asyncio
import os
import re
from datetime import datetime, timedelta

TOKEN = os.environ['DISCORD_BOT_TOKEN']
GUILD_ID = int(os.environ['DISCORD_BOT_GUILD_ID'])
CHANNEL_ID = int(os.environ['DISCORD_BOT_CHANNEL_ID'])

class ChatManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.chat_channel = None
        self.lifetime = timedelta(hours=2)
        self.emoji_pattern = re.compile(r'<a?:(\w+):(\d+)>')

    def get_emoji(self, message):
        print(message.content)
        content = self.emoji_pattern.fullmatch(message.content)
        if content != None:
            print(content.groups())
            return self.bot.get_emoji(int(content.group(2)))
        else:
            return None

    @commands.Cog.listener()
    async def on_ready(self):
        print(datetime.utcnow())
        guild = self.bot.get_guild(GUILD_ID)
        self.chat_channel = guild.get_channel(CHANNEL_ID)
        print("""guild name: {}
channel_name: {}""".format(guild, self.chat_channel))

        #delete messages wich are sent before 2 hours ago
        print(datetime.utcnow()-self.lifetime)
        old_messages = await self.chat_channel.history(before=datetime.utcnow()-self.lifetime).flatten()
        for i in old_messages:
            print(i)
        await self.chat_channel.delete_messages(old_messages)
        late_messages = await self.chat_channel.history().flatten()
        print(late_messages)
        print("------------")
        for message in late_messages:
            life_time = (message.created_at + self.lifetime) - datetime.utcnow()
            print("{}: {} sec".format(message.id, life_time.total_seconds()))
            if life_time > timedelta(0):
                await asyncio.sleep(life_time.total_seconds())
            message.delete()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel == self.chat_channel:
            #遅延時間を設定できるようにする
            print("{} will be deleted".format(message.id))
            await asyncio.sleep(self.lifetime.total_seconds())
            await message.delete()
            print("{} deleted".format(message.id))

            emoji = self.get_emoji(message)
            if emoji != None:
                await self.chat_channel.send(content=str(emoji.url))

bot = commands.Bot(command_prefix='!')
bot.add_cog(ChatManager(bot))

bot.run(TOKEN)
