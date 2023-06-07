import discord
from discord.ext import commands

# Créer une instance du bot avec le préfixe "!"
bot = commands.Bot(command_prefix='!')

# Evénement quand le bot se connecte et est fonctionnel
@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user.name}')

# Commande "!greet" pour que le bot vous dise "Hello ..."  
@bot.command()
async def greet(ctx):
    await ctx.send(f'Hello {ctx.author.mention}!')

# Pour lancer le bot
bot.run('YOUR_BOT_TOKEN')
