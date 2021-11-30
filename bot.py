import os

from discord.ext import commands
from dotenv      import load_dotenv

bot = commands.Bot(command_prefix="?")

# Assume that the .env file is always going to be in the same directory as bot.py
root = os.path.dirname(__file__) + "/" # root dir
load_dotenv(f"{root}.env")

@bot.event
async def on_ready():
  print("Connected to Discord!")

bot.run(os.getenv("TOKEN"))