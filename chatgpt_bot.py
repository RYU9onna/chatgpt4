import os
import openai
import discord
from discord.ext import commands

# 環境変数からAPIキーとDiscordボットトークンを取得
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
DISCORD_BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]

# OpenAI APIクライアントを初期化
openai.api_key = OPENAI_API_KEY

# Discordボットを初期化
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online!")

@bot.command(name="chat")
async def chat(ctx, *, message):
    prompt = f"User: {message}\nAI:"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    reply = response.choices[0].text.strip()
    await ctx.send(reply)

bot.run(DISCORD_BOT_TOKEN)
