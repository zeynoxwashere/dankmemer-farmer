# Credits to Pineapple#1000 and MOLE#2165 for the original code

import discord, asyncio

from discord.ext import commands

import random

token = "your discord token"

#Bot prefix, like ?help

prefix = "?"

#Prefix

client = discord.Client()

client = commands.Bot(command_prefix=prefix,self_bot=True)

#Farm

@client.command(name='start', aliases=['farm'])

async def _fish_dank(ctx): # b'\xfc'

    await ctx.message.delete()

    count = 0

    while True:

        try:

            count += 1

            await ctx.send('pls fish')
            await asyncio.sleep(random.randint(1,5))

            await ctx.send('pls hunt')
            await asyncio.sleep(random.randint(1,5))

            await ctx.send('pls dig')
            await asyncio.sleep(random.randint(1,5))

            await ctx.send('pls beg')
            
            if(random.randint(1,5) == 2): #added this so it sometimes also deposits all the coins
                await asyncio.sleep(random.randint(1,5))
                await ctx.send('pls dep max')

            print(f'[AUTO-FARM] Farm number: {count} sent')

            await asyncio.sleep(random.randint(45,60))

        except Exception as e:

            print(f"[ERROR]: {e}")

           

#onReady

@client.event

async def on_ready():

	print(f"Logged in. Write {prefix}start to begin!")

client.run(token,bot=False)
