# Work with Python 3.6
import random
import asyncio
import aiohttp
import json
import subprocess
import discord
import time
import psutil
import configparser
from discord import Game
from discord.ext.commands import Bot

def dict_factory(cursor, row):
    d = {}
    for idx,col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

config = configparser.RawConfigParser()
config.read('config.ini')

BOT_PREFIX = (config.get('DEFAULT','BOT_PREFIX'))
TOKEN = config.get('DEFAULT','DISCORD_TOKEN')  # Get at discordapp.com/developers/applications/me
GAMESERVER = config.get('DEFAULT','GAMESERVER')

client = Bot(command_prefix=BOT_PREFIX)

playing = []

for value in config.get('DEFAULT','PLAYING').split(','):
    playing.append(value)

allowed = []

for value in config.get('DEFAULT','ALLOWED').split(','):
    allowed.append(value)

remove_from_output = ['[K','32m','[0m']

def directcommand(command, sender, channel):
    command = command.replace(GAMESERVER+' ','')
    if command == 'details':
        command = 'postdetails'
    elif command == 'update':
        command = 'force-update'

    try:
        output = subprocess.run('/home/'+GAMESERVER+'/'+GAMESERVER+' "'+command+'"', shell=True,stdout=subprocess.PIPE,universal_newlines=True)
        output = str(output.stdout)
        for t in remove_from_output:
            output = output.replace(t,'')
        return output
    except expression as identifier:
        return "Command encountered an error."

def is_command(m):
    return m.content.startswith(BOT_PREFIX)

@client.event
async def on_message(message):
    # we overwrite the default here to check command levels
    if message.content.startswith(BOT_PREFIX):
        await client.process_commands(message)

@client.group(pass_context=True,name=GAMESERVER)
async def gameserver_command(context):
    if context.invoked_subcommand is None:
        await client.say('Invalid command passed...')

@gameserver_command.command(pass_context=True, name="start")
async def start_command(context):
    await client.delete_message(context.message)
    if str(context.message.channel) in allowed:
        print('Content: ['+str(context.message.content[1:])+'] Author: ['+str(context.message.author)+'] Channel: ['+str(context.message.channel)+']')
        em = discord.Embed(title=context.message.content[1:],description=directcommand(context.message.content[1:],context.message.author,context.message.channel))
        em.set_author(name=context.message.author,icon_url=client.user.default_avatar_url)
        await client.send_message(context.message.channel,embed=em) # we pass the context so we can have all the commands in help
    else:
        await client.say("The channel ("+str(context.message.channel)+") does not have permission to run commands. Please refrain from trying.")


@gameserver_command.command(pass_context=True, name="stop")
async def stop_command(context):
    await client.delete_message(context.message)
    if str(context.message.channel) in allowed:
        print('Content: ['+str(context.message.content[1:])+'] Author: ['+str(context.message.author)+'] Channel: ['+str(context.message.channel)+']')
        em = discord.Embed(title=context.message.content[1:],description=directcommand(context.message.content[1:],context.message.author,context.message.channel))
        em.set_author(name=context.message.author,icon_url=client.user.default_avatar_url)
        await client.send_message(context.message.channel,embed=em) # we pass the context so we can have all the commands in help
    else:
        await client.say("The channel ("+str(context.message.channel)+") does not have permission to run commands. Please refrain from trying.")

@gameserver_command.command(pass_context=True, name="restart")
async def restart_command(context):
    await client.delete_message(context.message)
    if str(context.message.channel) in allowed:
        print('Content: ['+str(context.message.content[1:])+'] Author: ['+str(context.message.author)+'] Channel: ['+str(context.message.channel)+']')
        em = discord.Embed(title=context.message.content[1:],description=directcommand(context.message.content[1:],context.message.author,context.message.channel))
        em.set_author(name=context.message.author,icon_url=client.user.default_avatar_url)
        await client.send_message(context.message.channel,embed=em) # we pass the context so we can have all the commands in help
    else:
        await client.say("The channel ("+str(context.message.channel)+") does not have permission to run commands. Please refrain from trying.")

@gameserver_command.command(pass_context=True, name="details")
async def details_command(context):
    await client.delete_message(context.message)
    if str(context.message.channel) in allowed:
        print('Content: ['+str(context.message.content[1:])+'] Author: ['+str(context.message.author)+'] Channel: ['+str(context.message.channel)+']')
        em = discord.Embed(title=context.message.content[1:],description=directcommand(context.message.content[1:],context.message.author,context.message.channel))
        em.set_author(name=context.message.author,icon_url=client.user.default_avatar_url)
        await client.send_message(context.message.channel,embed=em) # we pass the context so we can have all the commands in help
    else:
        await client.say("The channel ("+str(context.message.channel)+") does not have permission to run commands. Please refrain from trying.")

@gameserver_command.command(pass_context=True, name="update")
async def update_command(context):
    await client.delete_message(context.message)
    if str(context.message.channel) in allowed:
        print('Content: ['+str(context.message.content[1:])+'] Author: ['+str(context.message.author)+'] Channel: ['+str(context.message.channel)+']')
        em = discord.Embed(title=context.message.content[1:],description=directcommand(context.message.content[1:],context.message.author,context.message.channel))
        em.set_author(name=context.message.author,icon_url=client.user.default_avatar_url)
        await client.send_message(context.message.channel,embed=em) # we pass the context so we can have all the commands in help
    else:
        await client.say("The channel ("+str(context.message.channel)+") does not have permission to run commands. Please refrain from trying.")

@gameserver_command.command(pass_context=True, name="validate")
async def validate_command(context):
    await client.delete_message(context.message)
    if str(context.message.channel) in allowed:
        print('Content: ['+str(context.message.content[1:])+'] Author: ['+str(context.message.author)+'] Channel: ['+str(context.message.channel)+']')
        em = discord.Embed(title=context.message.content[1:],description=directcommand(context.message.content[1:],context.message.author,context.message.channel))
        em.set_author(name=context.message.author,icon_url=client.user.default_avatar_url)
        await client.send_message(context.message.channel,embed=em) # we pass the context so we can have all the commands in help
    else:
        await client.say("The channel ("+str(context.message.channel)+") does not have permission to run commands. Please refrain from trying.")

@client.command(pass_context=True,name="stats")
async def stats(context):
    process = psutil.Process()
    msg = "Bot stats\nCPU: "+str(process.cpu_percent())+"%\nRam: "+str(process.memory_percent())+"%"
    em = discord.Embed(title=context.message.content[1:],description=msg)
    em.set_author(name=context.message.author,icon_url=client.user.default_avatar_url)
    await client.send_message(context.message.channel,embed=em)

@client.command(name="clean",pass_context=True)
async def clean(context):
    deleted = await client.purge_from(context.message.channel,limit=1000,check=is_command)
    await client.send_message(context.message.channel,'Deleted {} message(s)'.format(len(deleted)))


@client.event
async def on_ready():
    print("We are connected and running as "+GAMESERVER+"!")
    print("---"+str(len(playing))+" now playing options.")
    print("---"+str(len(allowed))+" allowed channel(s)")

async def change_presence_loop():
    await client.wait_until_ready()
    await asyncio.sleep(4)
    while not client.is_closed:
        now_playing = random.choice(playing)
        print("Now Playing: "+now_playing)
        await client.change_presence(game=Game(name=now_playing))
        await asyncio.sleep(60*60) # change every hour

client.loop.create_task(change_presence_loop())
client.run(TOKEN)
