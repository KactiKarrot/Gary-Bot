import os
import random

import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
	print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	missu = [

		'I miss you too :cry:',
		'Screw you b\*\*\*\*'

	]
	loveu = [

		'I love you too :heart:',
		'Screw you b\*\*\*\*'

	]


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
		response1 = random.choice(loveu)
		await message.channel.send(response1)
	elif 'i love you' in message.content.lower():
		response2 = random.choice(loveu)
		await message.channel.send(response2)
	elif 'i love gary' in message.content.lower():
		response5 = random.choice(loveu)
		await message.channel.send(response2)
	elif 'imy' in message.content.lower():
		response3 = random.choice(missu)
		await message.channel.send(response3)
	elif 'i miss you' in message.content.lower():
		response4 = random.choice(missu)
		await message.channel.send(response4)
	elif 'i miss gary' in message.content.lower():
		response6 = random.choice(missu)
		await message.channel.send(response4)
#	elif 'honkers' in message.content.lower():
#		honkers1 = 'Boobies Tits Honkers Jugs Mommy Milkers Melons  Breasticle Jiggler Cans Hooters Bazongas Boobs Tatas Puppies Twins Bouncers The Girls Coconuts  Cha-Chas Bosom Lifesafers  Cantaloupes Milkers Udders Mosquito Bites Maracas Funbags Juganauts Knockers Shelf Air-Bags Nipple Holsters Bongos Shoulder Boulders Fleshy Mounds Business Opportunities Globes  Dumplings Heavers Plumbers Chest Booty  Briskets Milkshakes Equipment Assets Dick Rest Gay Decievers Doodads  Bonbons  Nice Ones Shock Absorbers Thingies Dinner Buckets Marshmellows Chi-Chis Hangers'
#		honkers2 = 'Doorknobs Yabbos Num-Nums Bombers Gazongas Buffet  Mods and Rockers Cancer Magnets Shirt Potatoes Bobbers Fat Sack Billibongs Beanbags Aroogas Bitties Blinkers Bitties Blubber Nuggets Bra Buddies Bra Stuffers Bubbas Bubbles Bust Cum Gutters Caboodles Cannon Balls Carumbas Cum Buckets Milk Buckets Corkers Nip Drippers Devils Dumplings Dairy Pillows Dingers Dingos Bobblings Double-Whammies Flapjacks Fog Lights Head Lights Gagas PP Pleasers Grapefruits Hand Warmers Heifers Highbeams Hood-Ornaments Hoohas Hot Cakes Human Udders Hubcaps Huffies Beach Balls Julius Squeezers Lady Lumps Motherloads Mondos Moo Moos Mommas Muffins Moons Niblets Nipples Nippers Nippies Pointy Milkers Shakers Shimmies Baby Fedders Stacks Swag Bags Sweater Meat Teats Tidbits Torpedoes Tweakers Twin Peaks'
#		honkers3 = 'WahWahs Whoppers Zingers Milk Squirters Bababoey Mushrooms Volleyballs Tennis Balls Basketballs Pancakes Cakes  3d Half Circles Penis Pleasers Traffic Cones Nose Cones Face Warmers Headphones Sag Bags Sex Handles Firm Pirms Plastic Pancakes Burgers Chest Pussy Snowcones Pointers Water Balloons Sour Milkers Breasts Saggers Chest Bulges Mammory  Neck Rest Organic Bottle Openers Cushions Face Pillow Storage Mountains Peaks Plateau Smuggler Compartments Lopsided Mountains Jupiter and Venus Meat Sacks Cup Holder PP Warmers Big Knockers Deflated Balloons Balloons Cherries Chest Balls Chesticles Treasure Chests Milk Bags Blocks Chest Drums Timpinis Eye Catchers Eye Candy Baby Bottles Eye Cocaine Shakey Cakey hungolomghononoloughongous'
#		await message.channel.send(honkers1)
#		await message.channel.send(honkers2)
#		await message.channel.send(honkers3)



client.run(TOKEN)
