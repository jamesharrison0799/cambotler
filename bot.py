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
    await client.change_presence(activity=discord.Game("Dream Daddy: A Dad Dating Simulator"))
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
    await ctx.author.send("I don't know")

@client.command(pass_context=True)
async def auughhh(ctx, times=1):
    try:
        vc = await ctx.message.author.voice.channel.connect()
        for n in range(times):
            player = vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source='augh.wav'))
            time.sleep(3)
        await discord.utils.get(client.voice_clients).disconnect()
    except Exception as e:
        print(e)

@client.command(pass_context=True)
async def jp(ctx):
    try:

        vc = await ctx.message.author.voice.channel.connect()
        player = vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source='arecciIHAnpmeaQR97iF8.wav'))
        time.sleep(5)
        await discord.utils.get(client.voice_clients).disconnect()
    except Exception as e:
        print(e)

@client.command(pass_context=True)
async def joel(ctx):
    try:
        vc = await ctx.message.author.voice.channel.connect()
        player = vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source='Recording.mp3'))
        time.sleep(5)
        await discord.utils.get(client.voice_clients).disconnect()
    except Exception as e:
        print(e)

@client.command(pass_context=True)
async def james(ctx):
    try:
        vc = await ctx.message.author.voice.channel.connect()
        player = vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source='recordings/james.mp3'))
        time.sleep(5)
        await discord.utils.get(client.voice_clients).disconnect()
    except Exception as e:
        print(e)

@client.command(pass_context=True)
async def tom(ctx):
    try:
        vc = await ctx.message.author.voice.channel.connect()
        player = vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source='recordings/tom.mp3'))
        time.sleep(5)
        await discord.utils.get(client.voice_clients).disconnect()
    except Exception as e:
        print(e)

@client.command(pass_context=True)
async def sam(ctx):
    try:
        vc = await ctx.message.author.voice.channel.connect()
        player = vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source='recordings/sam.mp3'))
        time.sleep(5)
        await discord.utils.get(client.voice_clients).disconnect()
    except Exception as e:
        print(e)

@client.command(pass_context=True)
async def lewisb(ctx):
    try:
        vc = await ctx.message.author.voice.channel.connect()
        player = vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source='recordings/lewis_b.mp3'))
        time.sleep(5)
        await discord.utils.get(client.voice_clients).disconnect()
    except Exception as e:
        print(e)

@client.command(pass_context=True)
async def cameron(ctx):
    try:
        vc = await ctx.message.author.voice.channel.connect()
        player = vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source='recordings/cameron.mp3'))
        time.sleep(7)
        await discord.utils.get(client.voice_clients).disconnect()
    except Exception as e:
        print(e)



try:
    client.run(parser.get('discord','token'))
except Exception as e:
    raise
