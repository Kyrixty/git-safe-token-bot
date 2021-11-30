from discord.ext import commands

bot = commands.Bot(command_prefix="?")

@bot.event
async def on_ready():
  print("Connected to Discord!")

bot.run("TOKEN")