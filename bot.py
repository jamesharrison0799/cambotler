import discord
import time
from discord.ext import commands
from configparser import ConfigParser
import os

parser = ConfigParser()
parser.read('config.ini')

client = commands.Bot(command_prefix =parser.get('commands','command_prefix'))
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(".helpme for commands"))
    print('FUCKIN READY FOR IT M8')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing requirements, pls use proper syntax")
    else:
        print(error)

@client.command(pass_context=True)
async def helpme(ctx):
    author = ctx.message.author
    await ctx.author.send('I dont do anything yet')




try:
    client.run(parser.get('discord','token'))
except Exception as e:
    raise
