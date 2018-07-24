import discord
import secreto
import asyncio

client = discord.Client()

COR =0x292f33
token = secreto.seu_token()
msg_id = None
msg_user = None


@client.event
async def on_ready():
    print('BOT ONLINE - Olá Mundo!')
    print(client.user.name)
    print(client.user.id)
    print('-----BM-----')

@client.event
async def on_member_join(member):
  canal = client.get_channel("433437170892537867")
  regras = client.get_channel("431996524939968512")
  ajuda = client.get_channel("432002912756170752")
  texto = client.get_channel("388410880381026315")
  msg = " Seja bem vindo(a) ao Boteco da Madruga! {}\n Por favor, leia atentamente as {}\n " \
        "Em caso de dúvidas é só ir no canal de {}\n " \
        "Para visualizar os canais você deverá adicionar o cargo da sua preferência no canal de {}"\
      .format(member.mention, regras.mention, ajuda.mention, comandos.mention)
  await client.send_message(member, msg)

@client.event
async def on_member_remove(member):
   canal = client.get_channel("454323908531716114")
   embed = discord.Embed(title="**Parece que alguém saiu sem pagar. :runner:‍:dash:**", color=0x292f33)
   embed.add_field(name="** {} saiu do boteco. Esperamos que volte! **".format(member.name), value=" ㅤ", inline=False)
   embed.set_thumbnail(url=member.avatar_url)
   await client.send_message(canal, embed=embed)

@client.event
async def on_message(message):

    if message.content.lower().startswith("!lol"):
     embed1 =discord.Embed(
        title="Toque em um dos emojis abaixo para adicionar o cargo.",
        color=COR,
         description="▪ Sem chave, sem acesso.🔑\n" \
                     "▪ Dá pra tocar DJ Avan aí? 🎵\n" \
                     "▪ Conteúdo adulto né pai! 🔞\n" \
                     "▪ Pedra, papel ou tesoura? 🕹\n" \
                     "▪ Passa o pé pela bola... ⚽", )

    botmsg = await client.send_message(message.channel, embed=embed1)

    await client.add_reaction(botmsg, "🔑")
    await client.add_reaction(botmsg, "🎵")
    await client.add_reaction(botmsg, "🔞")
    await client.add_reaction(botmsg, "🕹")
    await client.add_reaction(botmsg, "⚽")


    global msg_id
    msg_id = botmsg.id

    global msg_user
    msg_user = message.author


@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message

    if reaction.emoji == "🔑" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Residente", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "🎵" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "DJ", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "🔞" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "+18", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "🕹" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Games", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "⚽" and msg.id == msg_id:  # and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Futebol", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

@client.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message

    if reaction.emoji == "🔑" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Residente", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "🎵" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "DJ", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "🔞" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "+18", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "🕹" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Games", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "⚽" and msg.id == msg_id:  # and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Futebol", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")


client.run(token)