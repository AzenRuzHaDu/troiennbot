import discord
from discord.ext import tasks
import os
from scrpper import user_interact, titres_S


client = discord.Client()
titroù = ' | '.join(map(str,titres_S))

msj_sik = "Demat deoc'h ! \n Me zo TroiennBot. Lâred a ran troeinnoù dre zegouezh kavet war al lec'henn-mañ (https://br.m.wikiquote.org/wiki/Krennlavario%C3%B9=hátroio%C3%B9-lavar=brezhonek). " \
          f"\n Setu ar pezh a c'hallit skrivañ evit tapout un droienn diganin :\n {titroù}. \nMa skrivit '$Troienn' e lârin un droienn dre zegouezh. \n Evit gwelet an destenn-mañ kasit '$Sikour' "


#send a random troienn daily
@tasks.loop(hours = 24)
async def myLoop():
    channel= client.get_channel(926943534764933163)
    await channel.send("Setu troienn an devezh : \n" + user_interact("$Troienn"))

@client.event
async def on_ready():
    print('We have log in as {0.user}'.format(client))
    myLoop.start()


@client.event
async def on_message(message):

    msg = message.content
#to avoid responding to the bot messages
    if message.author == client.user:
        return
    if msg == "$Sikour":
        await message.channel.send(msj_sik)
        return
    if any(word in msg for word in titres_S):
        msg_bot = user_interact(msg)
        #Avoid ValueErrors when a keyword is used in the middle of random message
        if msg_bot == "error":
            return
        else:
            await message.channel.send(msg_bot)
    #This one is there for the bot to ignore non relevant messages
    if ValueError:
        return


#job = user_interact("$Troienn")




