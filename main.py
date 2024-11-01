import os
import discord
from discord import app_commands
from discord.ui import View
from discord.ext import commands

from keep_alive import keep_alive
keep_alive()

permission_locked = "1079316234232922162", "915315911991386122"

intents = discord.Intents.all()
intents.message_content = True  # Needed for message content

client = commands.Bot(command_prefix="!", intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.command()
async def attack(ctx, *, message):
  await ctx.message.delete()

  
  if not format(ctx.message.author.id) in permission_locked:
    await ctx.send("You do not have permission to use this command.")

    return 


  webhook = await ctx.channel.create_webhook(name="🗿")


  
  if "|" in message:

    message = message.split("|")

    id = message[0]
    count = message[1]

    if not id and count:
      await ctx.send("Please provide an ID and a count.")
      return

    for x in range(0,int(count)):

      await webhook.send(content=f"<@{format(id)}>")

    webhook.delete()







  
  

# Retrieve the bot token securely from the environment
client.run(os.environ['BOT_TOKEN'])
