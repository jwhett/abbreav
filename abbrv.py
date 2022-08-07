#!/usr/bin/env python3

import discord
from discord.ext import commands
import os
import tomli
import tomli_w

config_filename = "config.toml"
try:
    with open(config_filename, "rb") as config_file:
        config = tomli.load(config_file)
        print("found and loaded config from disk!")
except OSError:
    print("could not find config on disk. using defaults and env for secrets.")
    config = {}
    config["secrets"] = {"token": os.getenv("token")}
    config["abbr"] = {}
    config["abbr"] = {"ping": "pong"}


print(f">>> loaded {len(config['abbr'])} abbreviations.")

intents = discord.Intents.default()
# intents.message_content = True
bot = commands.Bot(command_prefix=">", intents=intents)


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def ab(ctx):
    """Set and fix abbreviations"""
    # maybe this should be ctx.args instead.
    match ctx.message.content.split():
        case [">ab", "save"]:
            try:
                with open(config_filename, "wb") as config_file:
                    tomli_w.dump(config, config_file)
                await ctx.message.channel.send(content="wrote config!")
                print(f"wrote current config to {config_filename}")
            except OSError as e:
                await ctx.message.channel.send(
                    content=f"failed to write config file: {e}"
                )
        case [">ab", abbrev]:
            print(f"got request to replace {abbrev}")
            await ctx.message.delete()
            await ctx.message.channel.send(content=config["abbr"][abbrev])
        case [">ab", abbrev, *rest]:
            value = " ".join(rest)
            config["abbr"][abbrev] = value
            print(f"set a new abbreviation => {abbrev}: '{value}'")
            await ctx.message.delete()
            await ctx.message.channel.send(content=f"set '{abbrev}': '{value}'")


bot.run(config["secrets"]["token"])
