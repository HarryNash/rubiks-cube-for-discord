import discord, asyncio

from secret import discord_token
from commands import hands, jumble, solve, custom, text
from cube_constants import (HANDS_OP, JUMBLE_OP, SOLVE_OP, CUSTOM_OP, TEXT_OP,
							HELP_OP, GRAFFITIED_IMAGE, HELP_TEXT)

client = discord.Client()
lock = asyncio.Lock()

@client.event
async def on_ready():
	"""Indicates the bot is ready by printing it's credentials."""
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
async def on_message(message):
	"""Detects and carries out any commands then sends a cube image or text."""
	txt = None
	await lock.acquire()
	if (message.content.startswith(HANDS_OP)):
		txt = hands(message.channel.id, message.content[len(HANDS_OP + ' '):])
	elif (message.content.startswith(JUMBLE_OP)):
		jumble(message.channel.id)
	elif (message.content.startswith(SOLVE_OP)):
		solve(message.channel.id)
	elif (message.content.startswith(CUSTOM_OP)):
		txt = custom(message.channel.id, message.content[len(CUSTOM_OP + ' '):])
	elif (message.content.startswith(TEXT_OP)):
		txt = text(message.channel.id)
	elif (message.content.startswith(HELP_OP)):
		txt = HELP_TEXT
	else:
		lock.release()
		return

	if (txt == None):
		await client.send_file(message.channel, GRAFFITIED_IMAGE)
	else:
		await client.send_message(message.channel, txt)
	lock.release()

client.run(discord_token)
