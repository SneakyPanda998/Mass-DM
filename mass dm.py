import discord

import os
import re
import json

from urllib.request import Request, urlopen

client = discord.Client()
@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send('YOUR MESSAGE')
      print(f"Message sent to: {user.name}")
    except:
       print(f"Message not sent to: {user.name}")
       
client.run("TOKEN", bot=False)