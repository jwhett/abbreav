#!/usr/bin/env python3

import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
# intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)
abv_trigger = ">ab"
abbreviations = {}
abbreviations["/demo"] = "this is a demo"

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def ab(ctx):
    """Set and fix abbreviations"""
    # maybe this should be ctx.args instead.
    match ctx.message.content.split():
        case [abv_trigger, abbrev]:
            print(f"got request to replace {abbrev}")
            # need to see how avrae does this. i get a perm error.
            #await ctx.message.edit(content=abbreviations[abbrev])
            await ctx.message.reply(content=f"i would replace that with: {abbreviations[abbrev]}")
        case [abv_trigger, abbrev, *rest]:
            value = " ".join(rest)
            print(f"going to set a new abbreviation => {abbrev}: '{value}'")
            abbreviations[abbrev] = value
            await ctx.message.reply(content=f"i set {abbrev} to: '{value}'")


bot.run(os.getenv("abbrv_token"))
