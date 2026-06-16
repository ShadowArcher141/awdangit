from email.mime import text
import os
import random
import re

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
async def squirrel(ctx: commands.Context):
    await ctx.send("Squirrels are the very ever so best creatures to ever walk the lands of earth and must be respected and protected at all costs. Anyone who disrespects them deserves to burn forever in hell!")

@bot.command(aliases=["roll20", "roll12", "roll10", "roll8", "roll6", "roll4", "roll100"])
async def rollDice(ctx: commands.Context):
    """find # of sides for the die to be rolled."""
    Command = ctx.message.content
    string_numbers = re.findall(r'\d+', Command)
    x = [int(num) for num in string_numbers]
    """Roll a die and reply with the result."""
    result = random.randint(1, x[0])
    await ctx.send(f"You rolled a {result}!")

if __name__ == "__main__":
    bot.run(TOKEN)
