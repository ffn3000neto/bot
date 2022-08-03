import discord
from discord.ext import commands

bot = commands.Bot("-")

palavraos = ["porra","bosta","buceta","caralho","fdp","soca","broxa","fofo","sapequinha","bastardo","plebe","foda","foda-se","foder","fuder","nem fodendo","pau","pica","pqp","punheta","cu","trepar","xoxota",'sacanagem','cacete','arrombado',"babaca",'bicha','boiola','cracudo','filha da puta','galinha','puta','piranha','vagabundo','vagabunda','viado','corno','fudido','escroto','fudido','canalha','paspalho','trouxa','vaca','vadia','otario','bostao'
]
palavragrande= palavraos[0:]

@bot.event
async def on_ready():
    print(f"Estou Pronto! Estou conectado como {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if palavragrande in message.content:
        await message.channel.send(
            f"Sem palavras de baixo calão por aqui {message.author.name}"
        )

        await message.object()

@bot.command(name="oi")
async def send_hello(ctx):
    name = ctx.author.name

    response = f"Olá, {name}, vc parece gay"

    await ctx.send(response)




bot.run("MTAwNDM2ODMzMTUxMzUyODM0MA.Gaj9-s.7xgSe52eh1MQJIW1XiVUzQN6fTqP7Ctg-qF3vo")
