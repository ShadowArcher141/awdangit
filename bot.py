import os

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


if __name__ == "__main__":
    bot.run(TOKEN)
