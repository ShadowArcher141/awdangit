import os

import math
import random
import re
from email.mime import text

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise RuntimeError(
        "Missing DISCORD_TOKEN in environment. Copy .env.example to .env and set the token."
    )

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} ({bot.user.id})")


@bot.command(name="ping")
async def ping(ctx: commands.Context):
    """Reply with Pong!"""
    await ctx.send("Pong!")


@bot.command(name="squeak")
async def ping(ctx: commands.Context):
    await ctx.send(
        "Squirrels are the very ever so best creatures to ever walk the lands of earth and must be respected and protected at all costs. Anyone who disrespects them deserves to burn forever in hell!"
    )


@bot.command(name="pong")
async def ping(ctx: commands.Context):
    await ctx.send("ping")


@bot.command(name="cendum")
async def ping(ctx: commands.Context):
    await ctx.send(
        f"At this current point in time the dum chen has -{random.randint(1, 100000)} IQ! Incrediable."
    )


@bot.command(name="lootpull")
async def rng(ctx: commands.Context, pulls: int, rerolls: int):
    def check(message):
        return (
            message.author == ctx.author
            and message.channel == ctx.channel
            and message.content.lower() in ["y", "n"]
        )

    # unique = 50%
    # rare = 30%
    # legendary = 15%
    # fabled = 1.5%
    # mythic = 0.04%
    for i in range(rerolls + 1):
        pulledRolls = []
        for j in range(pulls):
            pull = round(random.uniform(1.0, 100.0), 2)
            if pull <= 50:
                pulledRolls.append(1)
            elif pull <= 80:
                pulledRolls.append(2)
            elif pull <= 98.46:
                pulledRolls.append(3)
            elif pull <= 99.96:
                pulledRolls.append(4)
            elif pull <= 100.0:
                pulledRolls.append(5)
            else:
                await ctx.send("Something strange happened the number did not match")
                await ctx.send(pull)
        pulledRolls.sort(reverse=True)
        cutOff = pulledRolls[:36]
        rows = []
        for k in range(0, len(cutOff), 9):
            rows.append(" ".join(str(x) for x in cutOff[k : k + 9]))
        await ctx.send("```" + "\n".join(rows) + "```")
        if rerolls - i != 0:
            await ctx.send(f"Do you want to reroll? (y/n), {rerolls - i} rerolls")
            response = await bot.wait_for("message", check=check)
            if response.content.lower() in ["y"]:
                continue
            else:
                break


@bot.command(
    aliases=["roll20", "roll12", "roll10", "roll8", "roll6", "roll4", "roll100"]
)
async def rollDice(ctx: commands.Context):
    """find # of sides for the die to be rolled."""
    Command = ctx.message.content
    string_numbers = re.findall(r"\d+", Command)
    x = [int(num) for num in string_numbers]
    """Roll a die and reply with the result."""
    result = random.randint(1, x[0])
    await ctx.send(f"You rolled a {result}!")


if __name__ == "__main__":
    bot.run(TOKEN)
