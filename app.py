import os
import discord
from discord.ext import commands

# 環境変数からDiscordボットトークンを取得
DISCORD_BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]

# Discordボットを初期化
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online!")

bot.run(DISCORD_BOT_TOKEN)