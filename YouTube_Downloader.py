import pytube
from pytube import YouTube
import discord
from discord.ext import commands



TOKEN = ""



bot = commands.Bot(command_prefix = '!')



@bot.event
async def on_ready():
	print("Ready")

@bot.event
async def on_message(message):
	if message.content.startswith('!download') and message.author.id == '268138118270418954':
		await bot.send_message(message.channel, 'Received')
		yt = YouTube(message.content.replace('!download ', '', 1))
		stream = yt.streams.first()
		stream.download()
bot.run(TOKEN)