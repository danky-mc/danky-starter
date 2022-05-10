import discord

TOKEN = 'OTczNjk1MzEyMjI3MDk4NjQ1.GwP8HX.cEZkpgfONHQNutR22dC13jHkFrMQ7e-mGF3xXs'

client = discord.Client()

@client.event
async def on_ready():
    print("We have successfully logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'in-game':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return

    if user_message.lower() == '!anywhere':
        await message.channel.send('This can be used in anywhere!')
        return

client.run(TOKEN)
