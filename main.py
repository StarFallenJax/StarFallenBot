import discord
from discord.ext import commands
from discord import Intents
from keep_alive import keep_alive
from datetime import datetime
import os

intents = discord.Intents.all()
client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="The Outpost²"))
    print('StarFallenBot is ready for action!')

@client.event
async def on_message(message):
    if "can you play" in message.content.lower():
        await message.add_reaction("👎")
    if "john" in message.content.lower():
        # Check if the bot has the "manage_roles" permission
        if message.guild.me.permissions_in(message.channel).manage_roles:
            # The bot has the permission, so it can timeout the user
            await message.channel.set_permissions(message.author, send_messages=False, time=600)
        else:
            # The bot does not have the permission, so it cannot timeout the user
            await message.channel.send("I don't have permission to timeout the user!")

# Check if today is Christmas
    if datetime.today().month == 12 and datetime.today().day == 25:
        # Send "Merry Christmas!" in the specified channel
        channel = client.get_channel(1018950323102027806)
        message = await channel.send("Merry Christmas!")
        # React to the message with a Christmas tree emoji
        await message.add_reaction("🎄")

# Check if today is Halloween
    if datetime.today().month == 10 and datetime.today().day == 31:
        # Send "Happy Halloween!" in the specified channel
        channel = client.get_channel(1018950323102027806)
        message = await channel.send("Happy Halloween!")
        # React to the message with a Pumpkin emoji
        await message.add_reaction("🎃")

keep_alive()
client.run(os.getenv('TOKEN'))
