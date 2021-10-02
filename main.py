import discord
from discord.ext import commands


intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot("!",intents=intents)


@Bot.event
async def on_ready():
  print("ben hazırım")



  
@Bot.command() 
async def WaterMan(msg):
  await msg.send('en iyisi')
Bot.run('TOKEN YAPIŞTIR') 
#runlamak için consola python main.js(index.py,bot.py,server.py vb.)
  
