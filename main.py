import discord
import asyncio
from discord.ext import commands
from random import choice, randint
from time import sleep as wait
from discord.ext.commands import Bot
from PIL import Image, ImageDraw, ImageFont, ImageOps
from Strings import *
import requests
import json


bot = commands.Bot(command_prefix='/')

#EVENTO INICIAR

@bot.event
async def on_ready():
    print('@================@')
    print('     BOT ONLINE   ')
    print(bot.user.name)
    print(bot.user.id)
    print('@================@')
    activity = discord.Game(name="Lets´s.code (BR) Servidor para programadores novatos! https://discord.gg/jch5WhD", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    channel_teste1 = bot.get_channel(743483125149073429)
    await channel_teste1.send(choice(lista_iniciar))
    await asyncio.sleep(3)
    await channel_teste1.send('***Bot iniciado! :pushpin:***')
    await channel_teste1.send('https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTn7w2L5uvzD0p31BpHBKfYplJp6ycNb0KJvA&usqp=CAU')
#==============

# COMEÇO COMANDOS RANDOM

@bot.command()
async def berti(message):
    await message.send(choice(lista_gif_berti))

@bot.command()
async def gostosa3d(message):
    await message.send(choice(lista_gif_gostosas3d))

@bot.command()
async def gostosa2d(message):
    await message.send(choice(lista_gif_gostosas2d))

@bot.command()
async def adm(message):
    await message.send(choice(lista_gif_adm))

@bot.command()
async def paitaon(message):
    await message.send(choice(lista_gif_paitaon))

@bot.command()
async def paitaoff(message):
    await message.send(choice(lista_gif_paitaoff))

@bot.command()
async def furro(message):
    await message.send('**MORRA FURRO, MORRA IMEDIATAMENTE**')
    await message.send(choice(lista_gif_furros))

@bot.command()
async def pato(message):
    await message.send('**PATO FODA D+ :sunglasses:**')
    await message.send(choice(lista_gif_patos))

@bot.command()
async def kawai(message):
    await message.send(choice(lista_gif_kawai))

@bot.command()
async def bolsonaro(message):
    await message.send(choice(lista_gif_bolsonaro))

@bot.command()
async def salve(message):
    await message.send(choice(lista_salves))

@bot.command()
async def frase(message):
    await message.send(choice(lista_frases))

@bot.command()
async def tapa(message, arg1):
    embed = discord.Embed(description= '{} **deu um tapa em** {}'.format(message.author.mention, arg1), color=0x1f1d1d) 
    embed.set_image(url= choice(lista_gif_tapas))
    await message.channel.send(embed=embed)

@bot.command()
async def hentai(message):
    numHentai = randint(1, 319999)
    await message.channel.send('Seu link foi gerado, boa poneta {} !'.format(message.author.mention))
    await message.channel.send('https://nhentai.net/g/{}/'.format(numHentai))

@bot.command()
async def deathnote(message, arg1):
    if arg1 == message.author.mention:
        await message.channel.send('{} se matou kkkk'.format(message.author.mention))
        await message.channel.send(choice(lista_gif_suicidio))
    else:
        await message.channel.purge(limit=1)
        embed = discord.Embed(description= '{} **Vai morrer em 30 segundos.**'.format(arg1), color=0xba3500) 
        embed.set_image(url= 'https://media.tenor.com/images/26a9ad42ee92debfb7cc0071d6968a28/tenor.gif')
        await message.channel.send(embed=embed)
        await asyncio.sleep(30)
        embed = discord.Embed(description= '{} **foi morto por um death note.**'.format(arg1), color=0xba3500) 
        embed.set_image(url= 'https://media.tenor.com/images/745f9037e25236727142bd0fb4575743/tenor.gif')
        await message.channel.send(embed=embed)

@bot.command()
async def monkiflip(message):
    await message.send('https://media.tenor.com/images/15c52fa732da36b258c4d58079780468/tenor.gif')

@bot.command()
async def ademir(message):
    await message.channel.purge(limit=1)
    embed = discord.Embed(title='**Foto do ilustre adm.**', description='**Cuidado pra não ficar cego de tanta beleza.**', color=0x121111)
    embed.set_image(url='https://media.discordapp.net/attachments/743482860161466509/751561259224268850/IMG_20200904_185433.jpg?width=219&height=475')
    await message.send(embed=embed)

@bot.command()
async def xandao(message):
    await message.channel.send(choice(lista_gif_xandao))

@bot.command()
async def atirar(message, arg1):
    if arg1 == message.author.mention:
        await message.channel.send('{} se matou kkkk'.format(message.author.mention))
        await message.channel.send(choice(lista_gif_suicidio))
    else:
        await message.channel.send('{} atirou em {} :boom::gun:'.format(message.author.mention, arg1))
        await message.channel.send(choice(lista_gif_atirar))

@bot.command()
async def beijar(message, arg1):
    await message.channel.send('{} deu um beijão em {} :kiss:'.format(message.author.mention, arg1))
    await message.channel.send(choice(lista_gif_beijar))

@bot.command()
async def dolar(message):
    requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
    cotacao = requisicao.json()
    await message.channel.send('O dolar agora está valendo R$ {}'.format(cotacao['USD']['bid']))

@bot.command()
async def pinto(message, arg1):
    tamanho_pinto = randint(0, 20)
    embed = discord.Embed(title= '**Pintometro**', description= 'O pinto do {} mede **{}cm!\n 8{}D**'.format(arg1, tamanho_pinto, '=' * tamanho_pinto), color=0x30caf4) 
    embed.set_thumbnail(url='https://gartic.com.br/imgs/mural/jo/jonathanrb/pinto.png')
    await message.channel.send(embed=embed)

@bot.command()
async def pintometro(message, arg1):
    tamanho_pinto = randint(0, 20)
    embed = discord.Embed(title= '**Pintometro**', description= 'O pinto do {} mede **{}cm!\n 8{}D**'.format(arg1, tamanho_pinto, '=' * tamanho_pinto), color=0x30caf4) 
    embed.set_thumbnail(url='https://gartic.com.br/imgs/mural/jo/jonathanrb/pinto.png')
    await message.channel.send(embed=embed)

@bot.command()
async def gado(message, arg1):
    porcentagem_gado = randint(0, 100)
    embed = discord.Embed(title= '**Gadometro**', description= 'O {} é **{}% gado**'.format(arg1, porcentagem_gado), color=0x30caf4) 
    embed.set_thumbnail(url='https://cdn.awsli.com.br/800x800/462/462594/produto/29654470/63bc5f4ec0.jpg')
    await message.channel.send(embed=embed)

@bot.command()
async def gadometro(message, arg1):
    porcentagem_gado = randint(0, 100)
    embed = discord.Embed(title= '**Gadometro**', description= 'O {} é **{}% gado**'.format(arg1, porcentagem_gado), color=0x30caf4) 
    embed.set_thumbnail(url='https://cdn.awsli.com.br/800x800/462/462594/produto/29654470/63bc5f4ec0.jpg')
    await message.channel.send(embed=embed)

@bot.command()
async def viado(message, arg1):
    porcentagem_viado = randint(0, 100)
    embed = discord.Embed(title= '**Viadometro**', description= 'O {} é **{}% gay** kk'.format(arg1, porcentagem_viado), color=0x30caf4) 
    embed.set_thumbnail(url='https://i.pinimg.com/originals/fa/ac/88/faac886289715c79c4560e39bc921acb.png')
    await message.channel.send(embed=embed)

@bot.command()
async def viadometro(message, arg1):
    porcentagem_viado = randint(0, 100)
    embed = discord.Embed(title= '**Viadometro**', description= 'O {} é **{}% gay** kk'.format(arg1, porcentagem_viado), color=0x30caf4) 
    embed.set_thumbnail(url='https://i.pinimg.com/originals/fa/ac/88/faac886289715c79c4560e39bc921acb.png')
    await message.channel.send(embed=embed)

# FIM COMANDOS RANDOM / COMEÇO COMANDOS GERAIS

@bot.command()
async def ajuda(message):
    await message.channel.purge(limit=1)
    embed = discord.Embed(title='**Todos os comandos do bot: prefix (/)**', description='***Lista de comandos***\n \n**Comandos Random** \nBerti: Manda gifs do nosso salvador Bruno Berti. \nGostosa3d: Manda gifs de gostosas da vida real. \nGostosa2d: Manda gifs de gostosas de anime. \nAdm: Manda gifs do ademir kk. \nPaitaon: Manda gifs do pai ta on. \nPaitaoff: Manda gifs do pai ta off. \nViado/Viadometro: Mostra o quão viado o usuário mencionado é.\nGado/Gadometro: Mostra a porcentagem de gado do usuário mencionado\n Pinto/Pintometro: Mostra o tamanho do pinto do usuário mencionado :hatched_chick: \nFurro: Manda gifs dos furros, Deus me livre. \nPato: Manda gifs dos maravilhosos patos.  \nKawaii: Manda gifs fofinhos >_<.\nBolsonaro: Manda gifs do nosso grande presidente bozorano. \nSalve: Você ganha um salve do bot(Muitom dahora). \nFrase: Lança a braba, Frase de alguem.\nXandao: Nosso salvador :pray:. \nTapa: marque alguem para dar um tapa. \nAtirar: Você irá atirar no usuário mencionado. \nBeijar: Voce irá dar um beijo no usuário mencionado.\nHentai: Gera um link de hentai aleatorio. \nMonkiflip: Um macaco da um flip. \nMacaco: O macaco cai. \nDolar: mostra a cotação atual.\nAdemiro: Foto do lindo bielgomes \n \n**Comandos Gerais:** \nAjuda: Envia lista de comandos no PV.\nComandos: Envia lista de comandos no chat atual. \nPing: Testa o ping do bot! \nFale: O bot fala algo que você escrever. \nCriadores: Mostra os criadores do bot. \n \n**Comandos meme:** \nHipocrisia: Gera um meme hipocrisia. \nStonks: Gera um meme Stonks. \nNotStonks: Gera um meme not stonks. \nBotoes: Gera o meme do botão\nMedo: Gera o meme do medo. \nPegadinhas: Gera o meme do pegadinhas com seu nome. \n \n**Comandos staff:** \nPrefix: Edita o prefixo do bot** (ainda não está disponível)**. \nClear: Limpa o chat **(maximo 100)**.')
    await message.author.send(embed=embed)

@bot.command()
async def comandos(message):
    await message.channel.purge(limit=1)
    embed = discord.Embed(title='**Todos os comandos do bot: prefix (/)**', description='***Lista de comandos***\n \n**Comandos Random** \nBerti: Manda gifs do nosso salvador Bruno Berti. \nGostosa3d: Manda gifs de gostosas da vida real. \nGostosa2d: Manda gifs de gostosas de anime. \nAdm: Manda gifs do ademir kk. \nPaitaon: Manda gifs do pai ta on. \nPaitaoff: Manda gifs do pai ta off. \nViado/Viadometro: Mostra o quão viado o usuário mencionado é.\nGado/Gadometro: Mostra a porcentagem de gado do usuário mencionado\n Pinto/Pintometro: Mostra o tamanho do pinto do usuário mencionado :hatched_chick: \nFurro: Manda gifs dos furros, Deus me livre. \nPato: Manda gifs dos maravilhosos patos.  \nKawaii: Manda gifs fofinhos >_<.\nBolsonaro: Manda gifs do nosso grande presidente bozorano. \nSalve: Você ganha um salve do bot(Muitom dahora). \nFrase: Lança a braba, Frase de alguem.\nXandao: Nosso salvador :pray:. \nTapa: marque alguem para dar um tapa. \nAtirar: Você irá atirar no usuário mencionado. \nBeijar: Voce irá dar um beijo no usuário mencionado.\nHentai: Gera um link de hentai aleatorio. \nMonkiflip: Um macaco da um flip. \nMacaco: O macaco cai. \nDolar: mostra a cotação atual.\nAdemiro: Foto do lindo bielgomes \n \n**Comandos Gerais:**\nAjuda: Envia lista de comandos no PV.\nComandos: Envia lista de comandos no chat atual. \nPing: Testa o ping do bot! \nFale: O bot fala algo que você escrever. \nCriadores: Mostra os criadores do bot. \n \n**Comandos meme:** \nHipocrisia: Gera um meme hipocrisia. \nStonks: Gera um meme Stonks. \nNotStonks: Gera um meme not stonks. \nBotoes: Gera o meme do botão\nMedo: Gera o meme do medo. \nPegadinhas: Gera o meme do pegadinhas com seu nome. \n \n**Comandos staff:** \nPrefix: Edita o prefixo do bot** (ainda não está disponível)**. \nClear: Limpa o chat **(maximo 100)**.')
    await message.channel.send(embed=embed)

@bot.command()
async def ping(message):
    await message.send('**Latencia do bot de {0} ms**'.format(round(bot.latency, 2)))

@bot.command()
async def fale(message, *, arg):
        await message.channel.purge(limit=1)
        if arg == 'sou corno':
            await message.send('Corno é tu')
        else:
            await message.send(arg)

@bot.command()
async def criadores(message):
    await message.send('***LetsCodeBot criado por:*** \njv#3611 e Bielgomes#0313 \n \n**Os computadores são incrivelmente rápidos, precisos e burros; os homens são incrivelmente lentos, imprecisos e brilhantes; juntos, seus poderes ultrapassam os limites da imaginação.**\n \n***Albert Einstein***')

# FIM COMANDOS GERAIS / COMEÇO COMANDOS MEMES

@bot.command()
async def hipocrisia(message, *, arg):
    imagem = Image.open( 'imagens/hipocrisia.jpg' )
    fonte = ImageFont.truetype('fonts/arial.ttf', 20)
    text = arg
    if len(text) > 33:
        texto = text.split('+')
        w, h = fonte.getsize(texto[0])
        w, h = fonte.getsize(texto[1])
        draw = ImageDraw.Draw(imagem)
        draw.text(((460-w)/2, (50-h)/2), texto[0], font=fonte, fill='white')
        draw.text(((460-w)/2, (100-h)/2), texto[1], font=fonte, fill='white')
        imagem.save('tmpHipo.png', format='PNG')
        file = discord.File(open('tmpHipo.png', 'rb'))
        await message.channel.send(file=file)
    else:
        w, h = fonte.getsize(text)
        draw = ImageDraw.Draw(imagem)
        draw.text(((460-w)/2, (100-h)/2), text, font=fonte, fill='white')
        imagem.save('tmpHipo.png', format='PNG')
        file = discord.File(open('tmpHipo.png', 'rb'))
        await message.channel.send(file=file)


@bot.command()
async def stonks(message, *, arg):
    imagem = Image.open( 'imagens/stonks.jpg' )
    fonte = ImageFont.truetype('fonts/arial.ttf', 50)
    text = arg
    if len(text) > 35:
        texto = text.split('+')
        w, h = fonte.getsize(texto[0])
        w, h = fonte.getsize(texto[1])
        draw = ImageDraw.Draw(imagem)
        draw.text(((1200-w)/2, (100-h)/2), texto[0], font=fonte, fill='white')
        draw.text(((1200-w)/2, (200-h)/2), texto[1], font=fonte, fill='white')
        imagem.save('tmpSton.png', format='PNG')
        file = discord.File(open('tmpSton.png', 'rb'))
        await message.channel.send(file=file)
    else:
        w, h = fonte.getsize(text)
        draw = ImageDraw.Draw(imagem)
        draw.text(((1200-w)/2, (100-h)/2), text, font=fonte, fill='white')
        imagem.save('tmpSton.png', format='PNG')
        file = discord.File(open('tmpSton.png', 'rb'))
        await message.channel.send(file=file)

@bot.command()
async def notstonks(message, *, arg):
    imagem = Image.open( 'imagens/notstonks.jpg' )
    fonte = ImageFont.truetype('fonts/arial.ttf', 28)
    text = arg
    if len(text) > 35:
        texto = text.split('+')
        w, h = fonte.getsize(texto[0])
        w, h = fonte.getsize(texto[1])
        draw = ImageDraw.Draw(imagem)
        draw.text(((690-w)/2, (50-h)/2), texto[0], font=fonte, fill='white')
        draw.text(((675-w)/2, (100-h)/2), texto[1], font=fonte, fill='white')
        imagem.save('tmpNotSton.png', format='PNG')
        file = discord.File(open('tmpNotSton.png', 'rb'))
        await message.channel.send(file=file)
    else:
        w, h = fonte.getsize(text)
        draw = ImageDraw.Draw(imagem)
        draw.text(((680-w)/2, (50-h)/2), text, font=fonte, fill='white')
        imagem.save('tmpNotSton.png', format='PNG')
        file = discord.File(open('tmpNotSton.png', 'rb'))
        await message.channel.send(file=file)

@bot.command()
async def botoes(message, *, arg):
    imagem = Image.open( 'imagens/botoes.jpg' )
    fonte = ImageFont.truetype('fonts/arial.ttf', 20)
    text = arg
    if '+' in text:
        texto = text.split('+')
        w, h = fonte.getsize(texto[0])
        w, h = fonte.getsize(texto[1])
        draw = ImageDraw.Draw(imagem)
        draw.text(((200-w)/2, (200-h)/2), texto[0], font=fonte, fill='black')
        draw.text(((550-w)/2, (130-h)/2), texto[1], font=fonte, fill='black')
        imagem.save('tmpBotoes.png', format='PNG')
        file = discord.File(open('tmpBotoes.png', 'rb'))
        await message.channel.send(file=file)
    else:
        await message.channel.send('voce precisa usar "+" para separar as duas frases')

@bot.command()
async def pegadinhas(message, *, arg):
    imagem = Image.open( 'imagens/pegadinhas.jpg' )
    fonte = ImageFont.truetype('fonts/arial.ttf', 70)
    text = arg
    if len(text) > 10:
        texto = text.split('+')
        draw = ImageDraw.Draw(imagem)
        draw.text(xy=(10,140), text=texto[0], font=fonte, fill=(173,12,0))
        draw.text(xy=(10,200), text=texto[1], font=fonte, fill=(173,12,0))
        imagem.save('tmpPegadinhas.png', format='PNG')
        file = discord.File(open('tmpPegadinhas.png', 'rb'))
        await message.channel.send(file=file)
    else:
        draw = ImageDraw.Draw(imagem)
        draw.text(xy=(10,140), text=arg, font=fonte, fill=(173,12,0))
        imagem.save('tmpPegadinhas.png', format='PNG')
        file = discord.File(open('tmpPegadinhas.png', 'rb'))
        await message.channel.send(file=file)

@bot.command()
async def medo(message, *, arg):
    imagem = Image.open( 'imagens/medo.jpg' )
    fonte = ImageFont.truetype('fonts/arial.ttf', 20)
    text = arg
    if '+' in text:
        texto = text.split('+')
        w, h = fonte.getsize(texto[0])
        w, h = fonte.getsize(texto[1])
        draw = ImageDraw.Draw(imagem)
        draw.text(((440-w)/2, (250-h)/2), texto[0], font=fonte, fill='black')
        draw.text(((420-w)/2, (790 -h)/2), texto[1], font=fonte, fill='black')
        imagem.save('tmpMedo.png', format='PNG')
        file = discord.File(open('tmpMedo.png', 'rb'))
        await message.channel.send(file=file)
    else:
        await message.channel.send('voce precisa usar "+" para separar as duas frases')

# FIM COMANDOS MEMES / COMEÇO COMANDOS STAFF
@bot.command()
@commands.has_role('adm')
async def prefix(message):
    await message.send('***Ainda em desenvolvimento!***')

@bot.command()
@commands.has_role('adm' or 'ADM' or 'administrador' or 'Admin' or 'dono' or 'fundador' or 'DONO' or 'ADMIN')                                                                                   
async def clear(message, amount=0):
    if amount > 100:
        await message.send('**Só limpo até 100 mensagens**', delete_after = 5) 
    elif amount <= 1:
        await message.send('**Só apago entre 2 e 100 mensagens!**', delete_after = 5)
    else:
        await message.channel.purge(limit=amount)
        await message.send('**{}, varias mensagens foram apagadas!**'.format(message.author.mention), delete_after = 5)

# FIM COMANDOS STAFF

#BOT TOKEN
bot.run('')

# EMBED
#    embed = discord.Embed(title = "test", description='Salve', color=0xFF0000) 
#    embed.set_image(url= choice(lista_gif_tapas))
#    embed.add_field(name = 'Blue Team', value= choice(lista_gif_tapas))
#    await message.channel.send(embed=embed)
# EMBED

# TROCAR FOTO DO BOT
    #pfp_path = "path/to/file.png"
    #fp = open(pfp_path, 'rb')
    #pfp = fp.read()
    #@client.event
    #async def on_ready():
    #    await client.edit_profile(password=None, avatar=pfp)
# TROCAR FOTO DO BOT

# ENTRADA E SAIDA
#@bot.event
#async def on_member_join(member):
#    url = requests.get(member.avatar_url)
#    avatar = Image.open(BytesIO(url.content))
#    avatar = avatar.resize((250, 250))
#    bigsize = (avatar.size[0] * 3,  avatar.size[1] * 3)
#    mask = Image.new('L', bigsize, 0)
#    draw = ImageDraw.Draw(mask)
#    draw.ellipse((0, 0) + bigsize, fill=255)
#    mask = mask.resize(avatar.size, Image.ANTIALIAS)
#    avatar.putalpha(mask)
#    output = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
#    output.putalpha(mask)
#    output.save('avatar.png')
#    fundo = Image.open( 'imagens/welcome.png' )
#    fonte = ImageFont.truetype('fonts/Digital.otf', 50)
#    escrever = ImageDraw.Draw(fundo)
#    escrever.text(xy=(300,90), text='Bem vindo {}'.format(member.name), fill=(0,0,0), font=fonte)
#    escrever.text(xy=(300,135), text='ao server {}'.format(member.guild.name), fill=(0,0,0), font=fonte)
#    escrever.text(xy=(300,180), text='você é o membro N° {}nd'.format(member.guild.member_count), fill=(0,0,0), font=fonte)
#    fundo.paste(avatar, (25, 25), avatar)
#    fundo.save('tmpBv.png', format='PNG')
#    file = discord.File(open('tmpBv.png', 'rb'))
#    channel_welcome = bot.get_channel(743482398070800394)
#    embed = discord.Embed(title='Bem vindo! {}'.format(str(member)), description='Seja bem vindo ao server {}! você é o membro nº {}nd no server.'.format(member.guild.name, member.guild.member_count), color=0x1f1d1d) 
#    embed.set_thumbnail(url = member.guild.icon_url)
#    embed.set_image(url='attachment://tmpBv.png')
#    await channel_welcome.send(file=file, embed=embed)

#@bot.event
#async def on_member_remove(member):
#    channel_leave = bot.get_channel(743482398070800394)
#    embed = discord.Embed(description='{} saiu do server.'.format(str(member)), color=0x1f1d1d)
#    await channel_leave.send(embed=embed)
#EMTRADA E SAIDA

#    msg=await message.send(embed=embed)
#    await msg.add_reaction("🔁")
#
#    #bot.canal_msg = message

#@bot.event
#async def on_reaction_add(reaction, user):
#    emoji = reaction.emoji
#
#    bot.canal_msg = user.reaction.message
#
#    if user.bot:
#        return
#
#    if emoji == "🔁":
#        await bot.canal_msg.(bot.get_command('hentai'))
#    else:
#        return
