from require import require
import discord
from require import require
from discord.ext import commands


# get the token
Token = require('./json/secret.json')['bot'].get('token')

bot = commands.Bot(command_prefix='!')

## events
@bot.event
async def on_ready(): 
    print('bot is ready')





bot.run(Token)

