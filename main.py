import discord
import asyncio
import random

client = discord.Client()


@client.event
async def on_ready():
    print('BOT ONLINE - OLÁ MUNDO')
    print(client.user.name)
    print(client.user.id)
    print('-----BM-----')


@client.event
async def on_message(message):
    if message.content.lower().startswith('!bora'):
        await client.send_message(message.channel, "Bora tomar uma?")

    if message.content.lower().startswith('!moeda'):
        if message.author.id == "385987172978917386": #permissão por id
            escolha = random.randint(1, 2)
            if escolha == 1:
                await client.add_reaction(message, '😀')
            if escolha == 2:
                await client.add_reaction(message, '👑')
        else:
            await client.send_message(message.channel, "Você não tem permissão para usar esse comando!")


client.run('NDY1MzI3MDA4NDcwMDA3ODEw.DiL5MA.JxeDFeGU-MOmzKAzyroe3MD1UyM')