import discord
import time
from discord.ext import commands, tasks
from configparser import ConfigParser
import os
import random
from datetime import datetime


parser = ConfigParser()
parser.read('config.ini')

client = commands.Bot(command_prefix =parser.get('commands','command_prefix'))
client.remove_command('help')

games = [
"Dream Daddy: A Dad Dating Simulator",
"Being a DIK - Season 1",
"NEEDY STREAMER OVERLOAD",
"Chasing Tails",
"Neko Maid",
"Tails and Pines",
"Bikini Armour Explorers",
"Click Girlfriend"
"Galaxy Girls",
"FarmD",
"Wars & Roses",
"Dialtown: Phone Dating Sim",
"Foot Odor Girl",
"VR Sweet Heart",
"Super Seducer",
"DIY MY LADY IN VR WORLD",
"Orc Massage",
"HuniePop 2: Double Date",
"Blush Blush",
"Love & Sex: Second Base",
"Maid Mansion",
"Boyfriend Dungeon",
"CUCKOLD SIMULATOR: Life as a Beta Male Cuck",
"My Ex-Boyfriend the Space Tyrant",
"Escape from Pleasure Planet"
]


@client.event
async def on_ready():
    gme = games[random.randint(1,len(games))]
    print(gme)
    await client.change_presence(activity=discord.Game(gme))
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
async def report(ctx):
    author = ctx.message.author
    await ctx.author.send("https://monzo.me/jamesharrison44/10.00?d=PLEASE%20REMOVE%20THIS%20COMMAND:%20")

@client.command(pass_context=True)
async def change(ctx):
    author = ctx.message.author
    await ctx.author.send("https://monzo.me/jamesharrison44/25.00?d=PLEASE%20CHANGE%20THIS%20COMMAND:%20")

@client.command(pass_context=True)
async def donate(ctx):
    author = ctx.message.author
    await ctx.author.send("https://monzo.me/jamesharrison44/50.00?d=Ta%20babe%20xox")

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
        player = vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source='recordings/joel.mp3'))
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

@client.command(pass_context=True)
async def harry(ctx):
    try:
        vc = await ctx.message.author.voice.channel.connect()
        player = vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source='recordings/harry.mp3'))
        time.sleep(7)
        await discord.utils.get(client.voice_clients).disconnect()
    except Exception as e:
        print(e)

# @client.command(pass_context=True)
# async def jason(ctx):
#     try:
#         vc = await ctx.message.author.voice.channel.connect()
#         directory = 'recordings/jason/'
#         src = os.walk(directory)[random.randint(lent(os.walk(directory)))]
#         player = vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source=src))
#         time.sleep(7)
#         await discord.utils.get(client.voice_clients).disconnect()
#     except Exception as e:
#         print(e)

@client.command(pass_context=True)
async def jason(ctx):
    try:
        vc = await ctx.message.author.voice.channel.connect()
        player = vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source='recordings/jason.mp3'))
        time.sleep(7)
        await discord.utils.get(client.voice_clients).disconnect()
    except Exception as e:
        print(e)

@client.command(pass_context=True)
async def jod(ctx):
    try:
        vc = await ctx.message.author.voice.channel.connect()
        player = vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source='recordings/jod.mp3'))
        time.sleep(7)
        await discord.utils.get(client.voice_clients).disconnect()
    except Exception as e:
        print(e)

@client.command(pass_context=True)
async def matt(ctx):
    try:
        vc = await ctx.message.author.voice.channel.connect()
        player = vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source='recordings/matt.mp3'))
        time.sleep(7)
        await discord.utils.get(client.voice_clients).disconnect()
    except Exception as e:
        print(e)

@client.command(pass_context=True)
async def cao(ctx):
    try:
        vc = await ctx.message.author.voice.channel.connect()
        player = vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source='recordings/cao.mp3'))
        time.sleep(7)
        await discord.utils.get(client.voice_clients).disconnect()
    except Exception as e:
        print(e)

@client.command(pass_context=True)
async def dec(ctx):
    try:
        vc = await ctx.message.author.voice.channel.connect()
        player = vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source='recordings/dec.mp3'))
        time.sleep(7)
        await discord.utils.get(client.voice_clients).disconnect()
    except Exception as e:
        print(e)

@client.command(pass_context=True)
async def niccybrown(ctx):
    try:
        vc = await ctx.message.author.voice.channel.connect()
        player = vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source='recordings/niccybrown.mp3'))
        time.sleep(7)
        await discord.utils.get(client.voice_clients).disconnect()
    except Exception as e:
        print(e)


# @client.command(pass_context=True)
# async def eve(ctx):
#     try:
#         vc = await ctx.message.author.voice.channel.connect()
#         player = vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source='recordings/eve.mp3'))
#         time.sleep(7)
#         await discord.utils.get(client.voice_clients).disconnect()
#     except Exception as e:
#         print(e)

@client.command(pass_context=True)
async def source(ctx):
    await ctx.author.send("https://github.com/jamesharrison0799/cambotler")

@tasks.loop(minutes =random.randint(10,35))
async def updateRichPresence():
    gme = games[random.randint(0,len(games)-1)]
    print(f"changed to {gme} @ {datetime.now().strftime('%H:%M:%S')}")
    await client.wait_until_ready()
    await client.change_presence(activity=discord.Game(gme))


try:
    updateRichPresence.start()
    client.run(parser.get('discord','token'))

except Exception as e:
    raise
