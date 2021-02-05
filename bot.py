import os
import random
import discord
import randfacts

from randfacts import getFact
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
	print(f'{client.user.name} has connected to Discord!')
	await client.change_presence(status=discord.Status.online, activity=discord.Game('Spicy boy!'))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	m8ball = [

		'It is certain.',
		'It os decidedly so.',
		'Without a doubt.',
		'Yes - definitely.',
		'You may rely on it.',
		'As I see it, yes.',
		'Most likely.',
		'Outlook good.',
		'Yes.',
		'Signs point to yes.',
		'Reply hazy, try again.',
		'Ask again later.',
		'Better not tell you now.',
		'Cannot predict now.',
		'Concentrate and ask again.',
		'Don\'t count on it.',
		'My reply is no.',
		'My sources say no.',
		'Outlook not so good.',
		'Very doubtful.',

	]
	missu = [

		'I miss you too :cry:',
		'Screw you b\*\*\*\*'

	]
	loveu = [

		'I love you too :heart:',
		'Screw you b\*\*\*\*'

	]
	marry = [

		'Ok :heart:',
		'You\'re ugly',
		'I\'m too out of your league',
		'potato',
		'How much do you make in a year?',
		'I\'m already married to Carl-Bot',
		'no b\*\*\*\*'

	]

	fortune = open("fortunes").readlines()

	if 'train' in message.content.lower():
		await message.channel.send('I like trains!')
	elif 'hi gary' in message.content.lower():
		await message.channel.send('Hello!')
	elif 'sup gary' in message.content.lower():
		await message.channel.send('Hello!')
	elif 'hello gary' in message.content.lower():
		await message.channel.send('Hello!')
	elif 'fuck you' in message.content.lower():
		await message.channel.send('Fuck you')
	elif 'you suck' in message.content.lower():
		await message.channel.send('no u')
	elif 'ily' in message.content.lower():
		await message.channel.send(random.choice(loveu))
	elif 'i love you' in message.content.lower():
		await message.channel.send(random.choice(loveu))
	elif 'i love gary' in message.content.lower():
		await message.channel.send(random.choice(loveu))
	elif 'i miss you' in message.content.lower():
		await message.channel.send(random.choice(missu))
	elif 'i miss gary' in message.content.lower():
		await message.channel.send(random.choice(missu))
	elif message.content.lower().startswith('~gary'):
		await message.channel.send(random.choice(m8ball))
	elif message.content.startswith('~8ball'):
		await message.channel.send(random.choice(m8ball))
	elif message.content.startswith('~knowledge'):
		await message.channel.send(getFact(False))
	elif message.content.startswith('~fortune'):
		await message.channel.send(random.choice(fortune))
	elif 'marry me' in message.content.lower():
		await message.channel.send(random.choice(marry))


#		a_string = "A string is more than its parts!"
#matches = ["more", "wholesome", "milk"]

#if any(x in a_string for x in matches):



client.run(TOKEN)
