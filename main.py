import discord
import os
import requests
import json
import random

client=discord.Client()

sad_words=['sad','sed','so sad','cant','sorry']

motivation = ['-_-','just SUADYL !','dont be sorry be better...','why though?', 'have a bo oh o waer ']

def get_quote():
  response=requests.get('https://zenquotes.io/api/random')
  json_data=json.loads(response.text)
  quote=json_data[0]['q'] + ' -' + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user :
    return

  msg=message.content

  if msg.startswith('yikes'):
    quote=get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(motivation) )
  
client.run(os.environ['BOT'])