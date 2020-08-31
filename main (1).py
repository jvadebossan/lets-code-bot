import discord
import asyncio
from discord.ext import commands
from random import choice, randint
from time import sleep as wait
from discord.ext.commands import Bot
from PIL import  Image, ImageFont, ImageDraw

bot = commands.Bot(command_prefix='/')

#============================================================================================================

lista_gif_berti = [
    'https://tenor.com/view/berti-sarrador-dancing-hyped-summer-pool-gif-17763539',
    'https://tenor.com/view/bruno-berti-irmaos-berti-irm%c3%a3os-berti-lucas-berti-porrada-gif-17518204',
    'https://tenor.com/view/berti-bruno-berti-bertinho-berte-berti-dancing-thrusting-gif-17771441',
    'https://tenor.com/view/bruno-berti-lucas-berti-irmaos-berti-indias-brega-funk-gif-16727590',
    'https://tenor.com/view/bruno-berti-lucas-berti-irmaos-berti-indias-brega-funk-gif-16727590',
    'https://tenor.com/view/berti-dark-sarrada-berti-dark-berti-sarrada-gif-17764030',
    'https://tenor.com/view/sarrando-berti-dancing-humping-gif-17763559',
    'https://tenor.com/view/sarrada-berti-dancing-gif-17895234',
    'https://media.discordapp.net/attachments/643918032468443177/733444131711352913/bertinho.gif?'
]

lista_gif_gostosas3d = [
    'https://tenor.com/view/sexy-jordana-brewster-bikini-pictorial-gif-13847158',
    'https://giphy.com/gifs/twerk-gnE9JR4OxfLig',
    'https://giphy.com/gifs/things-bounce-thechive-SInIQtCeyj1C0',
    'https://giphy.com/gifs/notorious-big-t1kRtJmCI4R1e',
    'https://giphy.com/gifs/a-mans-butt-tight-butts-sexy-guy-3o85xpi3wbmElPKSFq',
    'https://giphy.com/gifs/10x81OqDjnQhr2',
    'https://giphy.com/gifs/funkofficial-hand-3ohzdIfd39bRZhKRLa',
    'https://giphy.com/gifs/things-bounce-thursday-HbeZElJ8EjrEY',
    'https://giphy.com/gifs/dance-sfw-pov-11bNExgnwGHBuw',
    'https://giphy.com/gifs/the-rock-vince-mcmahon-rikishi-127h8dMHnk5H5C',
    'https://tenor.com/view/mia-khalifa-lip-bite-gif-13295397'
]

lista_gif_gostosas2d = [    
    'https://images-ext-2.discordapp.net/external/pEirYOB-Aw3qjC-hwhLJPNSCqw1_Qt9TtBD5JFb1Sd8/https/imgur.com/DrjW7Bk.gif',
    'https://tenor.com/view/yosuga-no-sora-sora-anime-good-girl-beautiful-gif-16500791',
    'https://tenor.com/view/anime-rias-gremory-undressed-manga-gif-16310335',
    'https://tenor.com/view/anime-life-love-gif-13861593',
    'https://tenor.com/view/highschooldxd-rias-akeno-koneko-bouncing-gif-6206479',
    'https://tenor.com/view/yandere-knife-cute-anime-gif-14593966',
    'https://tenor.com/view/iam4ming-sex-gif-9390805',
    'https://tenor.com/view/fortnite-dance-minecraft-steve-dance-steve-fortnite-steve-gif-15531052',
    'https://images-ext-1.discordapp.net/external/swaC2EQsPJaMgnCusSW4Gd85MT7qFPXg8SIDrv6_lIY/https/imgur.com/pv2wKTc.gif',
    'https://tenor.com/view/cute-anime-dancing-silly-happy-excited-gif-13462237',
    'https://tenor.com/view/anime-dance-happy-catgirl-gif-9765182',
    'https://tenor.com/view/sasuke-anime-naruto-dance-xd-gif-8074573'
] 

lista_gif_adm = [
    'https://giphy.com/gifs/dvOwFmfbzmAsI9v2IV',
    'https://tenor.com/view/will-smith-banido-meme-dance-gif-16971203',
    'https://tenor.com/view/teste-adm-gif-18233312',
    'https://tenor.com/view/banido-adm-administrador-ban-adm-on-gif-16662125',
    'https://tenor.com/view/depressor-adm-n%c3%a3o-me-da-ban-depressao-n%c3%a3o-d%c3%a1ban-adm-adm-gif-16714385',
    'https://tenor.com/view/wmiguel17-banido-sasuke-jutsu-banned-gif-17769467',
    'https://tenor.com/view/adm-ban-regra-gif-18049769',
    'https://tenor.com/view/treinando-pra-ser-adm-gif-18025277',
    'https://tenor.com/view/treinando-pra-ser-adm-gif-18025277',
    'https://tenor.com/view/atm-parado-is-taking-abath-carabao-bathing-river-carabao-bathing-gif-17779749',
    'https://tenor.com/view/adm-eu-nao-li-as-regras-dance-gif-17880739',
    'https://tenor.com/view/banido-thor-adm-administrador-chris-hemsworth-gif-17550051'
]

lista_gif_paitaon = [
    'https://tenor.com/view/pai-ta-on-big-chungus-reddit-arevalo-dance-gif-16955335',
    'https://tenor.com/view/pai-ta-on-dancing-clown-grooves-dance-moves-gif-17049247',
    'https://tenor.com/view/pai-ta-on-clown-dancing-gif-17553708',
    'https://tenor.com/view/pai-ta-on-dancing-groovy-jumping-the-mask-gif-17772245',
    'https://tenor.com/view/pai-ta-off-maskara-pai-ta-on-pai-ta-gif-18143937',
    'https://tenor.com/view/pai-ta-chato-weekend-vibe-mood-gif-13849068'
]

lista_gif_furros = [
    'https://tenor.com/view/furry-gif-4903957',
    'https://tenor.com/view/furry-furries-fa-ba-fantasy-basel-dance-gif-15180558',
    'https://tenor.com/view/dance-furry-cute-dance-move-gif-16336211',
    'https://tenor.com/view/game-grumps-furry-fursuit-gif-13526097',
    'https://tenor.com/view/mlp-heart-love-gif-9643704',
    'https://tenor.com/view/legoshi-beastars-furry-nervous-gif-15338729',
    'https://tenor.com/view/furry-snug-furry-furry-love-sweet-gif-17325139',
    'https://tenor.com/view/furry-squad-sniper-job-autumnfallings-gif-7485644',
    'https://tenor.com/view/furry-gif-11210434'
]

lista_gif_patos = [
    'https://tenor.com/view/duck-run-running-chase-come-back-here-gif-4536793',
    'https://tenor.com/view/gary-tay-kitten-duckling-gif-7517574',
    'https://tenor.com/view/duck-quack-walk-gif-9046918',
    'https://tenor.com/view/cute-duck-cuddle-its-ok-adorable-duck-gif-12985802',
    'https://tenor.com/view/sleepy-duck-gif-4521800',
    'https://tenor.com/view/aflack-dancing-duck-gif-10526585',
    'https://giphy.com/gifs/dancing-duck-aflack-b9QBHfcNpvqDK',
    'https://giphy.com/gifs/duck-2ATElMHGKoVeo',
    'https://giphy.com/gifs/animated-3d-animal-Y0zTJ7VrKo9P2',
    'https://giphy.com/gifs/duck-cuteness-baby-82nxC1u2BC8VU1wiZq'
]

lista_gif_kawai = [
    'https://tenor.com/view/cute-adorable-charming-gif-13798021',
    'https://tenor.com/view/japan-anime-kawaii-sugoi-gif-4761309',
    'https://tenor.com/view/milk-and-mocha-hugs-bear-couple-love-cute-gif-12498539',
    'https://tenor.com/view/excited-anime-cute-gif-5967731',
    'https://tenor.com/view/kawaii-kokoro-love-loli-gif-9484577',
    'https://tenor.com/view/loli-police-fbi-anime-sit-gif-16156795',
    'https://tenor.com/view/chloevoneinzbern-fate-fatekalied-loli-anime-gif-9809880',
    'https://tenor.com/view/loli-hearts-love-in-love-cute-gif-17645914',
    'https://tenor.com/view/cute-kawaii-zomg-gif-12496012',
    'https://tenor.com/view/hello-guys-cute-kawaii-happy-gif-13759559',
    'https://tenor.com/view/kawaii-cute-yui-gif-13400599'
]

lista_salves = [
    'Salve fi, pai ta on.',
    'Cheguei.',
    'To aqui man.',
    'Salve garai bagulho é loko memo.',
    'Baguio é rardicobra.',
    'Salve salve, o dono do server é mó gado.',
    'Salve, sabia que o Biel é o ser mais lindo do universo?',
    'Salve, amante do deus zoio.',
    'Sé loko mano, salve kebrada.',
    'Chamou?',
    'Salve :)',
    'Salve, lembre-se de se manter hidratado.',
]

lista_gif_bolsonaro = [
    'https://tenor.com/view/bolsonaro-2018-gif-10813661',
    'https://tenor.com/view/bolsonaro-face-mask-wave-heart-gif-17590213',
    'https://tenor.com/view/bolsonaroarminha-bolsonaro-bolsonaroempolgado-bang-bang-bang-gif-12433792',
    'https://tenor.com/view/bolsonaro-camera-camera-stand-gif-12770014',
    'https://tenor.com/view/grande-dia-bolsonaro-presidente-brasil-thumbs-up-gif-14439617',
    'https://tenor.com/view/bolsonaro-nando-moura-gif-8680576',
    'https://tenor.com/view/felipe-neto-amabol-sonaro-tattoo-laugh-felipe-neto-vlogger-gif-17178756',
    'https://giphy.com/gifs/gptv-trump-donald-bolsonaro-hr3AZuH7Y8Dvba9jUf',
    'https://giphy.com/gifs/programapanico-mito-bolsonabo-3o6nUT58nRNMIM0umQ',
    'https://media.discordapp.net/attachments/748691279352823979/748695801315983380/19b5rrcyuqu41.png'
]

lista_frases = [
    '"Liberdade sem leis significa anarquia; leis sem liberdade significa tirania." - Tanya Degurechaff',
    '"Milagres são ilusões causadas por observação e entendimento insuficientes. Eles são apenas... gloriosos mal-entendidos." - Tanya Degurechaff',
    '"Qualquer coisa que pode dar errado, vai dar errado. Essa é uma lei famosa. Se você viver uma vida longa, entenderá." - Tanya Degurechaff',
    '"Não importa o quanto nos modernizamos, não importa como as normas sociais nos afetam, os seres humanos são criaturas tolas." - Tanya Degurechaff',
    '"Vitória. Uma coisa tão tentadora. É claro que todo mundo quer apreciar seu sabor." - Tanya Degurechaff',
    '"O exército é uma organização. E as organizações não são nada sem regras!" - Tanya Degurechaff',
    '"O racionalismo não é a única coisa que move as pessoas." - Tanya Degurechaff',
    '"Honestamente, eu odeio a guerra. Pessoas matando umas as outras. Isso é a pior coisa que a humanidade poderia ter criado. Um desperdício de humanos e economias. No entanto, nossos inimigos são comunistas. Totalitários violando a liberdade pessoal. Não posso viver debaixo do mesmo teto que os comunistas. Temos de pegar em armas, para podermos viver uma vida feliz." - Tanya Degurechaff',
    '"Senhor, ouçais a minha prece é realizai o meu desejo. Do céu,trazei a baixo o martelo dá vossa irá." - Tanya Degurechaff',
    '"Tudo que é feito de carne é como se fosse mato, e toda a gloria dos homens é como se fossem flores campestres. O mato seca, as flores caem.Mas as palavras do Senhor Estarão sempre presentes." - Alucard',
    '"Quando as lágrimas de um ser humano enfim secam para sempre...Este se tornar um demônio,um monstro... Então ri...Ri com teu orgulho e tua arrogância...como sempre fez..." - Alucard',
    '"Não importa em que época estejamos vivendo , sempre haverá a falta de originalidade." - Alucard',
    '"Os humanos são os únicos seres que se divertem com o sofrimento dos seus semelhantes." - Alucard',
    '"A perseverança de quem está no comando incendeia a alma de quem o segue." - Alucard',
    '"Somente humanos podem matar monstros!" - Alucard',
    '"Os computadores são incrivelmente rápidos, precisos e burros; os homens são incrivelmente lentos, imprecisos e brilhantes; juntos, seus poderes ultrapassam os limites da imaginação." - Albert Einstein'
]

lista_gif_tapas = [
    'https://tenor.com/view/anime-slap-mad-gif-16057834',
    'https://tenor.com/view/anime-hit-slap-ouch-angry-gif-16268549',
    'https://tenor.com/view/no-angry-anime-slap-gif-7355956',
    'https://tenor.com/view/bunny-girl-slap-angry-girlfriend-anime-gif-15144612',
    'https://tenor.com/view/powerful-head-slap-anime-death-tragic-gif-14358509',
    'https://tenor.com/view/oreimo-anime-slap-gif-10936993',
    'https://tenor.com/view/girl-slap-anime-mad-student-gif-17423278',
    'https://tenor.com/view/anime-slap-slap-in-the-face-smash-gif-17314633',
    'https://tenor.com/view/naruto-anime-slap-slapping-sakura-gif-17897216',
    'https://tenor.com/view/horse-slap-anime-gif-15826924',
    'https://tenor.com/view/anime-slap-gif-12946466',
    'https://tenor.com/view/anime-sad-dog-pet-slap-gif-10943636',
    'https://tenor.com/view/tapa-slap-anime-smile-girls-last-tour-gif-17223486',
    'https://tenor.com/view/gintoki-gintama-sadaharu-dog-anime-gif-15349894',
    'https://tenor.com/view/slap-blood-anime-gif-4961067',
    'https://tenor.com/view/kon-kon-mio-kon-ritsu-anime-slap-gif-17012003',
    'https://tenor.com/view/my-collection-anime-slap-gif-16819981',
    'https://tenor.com/view/shikamaru-temari-naruto-gif-shippuden-gif-8576304',
    'https://tenor.com/view/chikku-neesan-girl-hit-wall-stfu-anime-girl-smack-gif-17078255',
    'https://tenor.com/view/anime-slap-slapping-smacking-heavens-lost-property-gif-5738394'
]

#============================================================================================================

#EVENTO INICIAR

@bot.event
async def on_ready():
    print('@================@')
    print('     BOT ONLINE   ')
    print(bot.user.name)
    print(bot.user.id)
    print('@================@')
    activity = discord.Game(name="Lets´s.code (BR) Servidor para programadores novatos! https://discord.gg/jch5WhD", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    channel_teste1 = bot.get_channel(743483125149073429)
    await channel_teste1.send('**Sistema inicializado. Conectando ao Banco de dados :globe_with_meridians:**')
    wait(3)
    await channel_teste1.send('***Conexão com o Banco de dados estabelecida :pushpin:***')
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
async def hentai(message):
    num1 = randint(1, 2)
    num2 = randint(1, 9)
    num3 = randint(1, 9)
    num4 = randint(1, 9)
    num5 = randint(1, 9)
    num6 = randint(1, 9)
    link_hentai = str(num1) + str(num2) + str(num3) + str(num4) + str(num5) + str(num6)
    await message.send('**o {} pediu um link de hentai, Boa poneta companheiro!**' .format(message.author.mention))
    await message.channel.send('https://nhentai.net/g/{}/'.format(link_hentai))


# FIM COMANDOS RANDOM / COMEÇO COMANDOS GERAIS

@bot.command(pass_context=True)
async def ajuda(message):
    await message.channel.purge(limit=1)
    await message.author.send('***Lista de comandos***\n \n**Comandos Random** \nBerti: Manda gifs do nosso salvador Bruno Berti. \nGostosa3d: Manda gifs de gostosas da vida real. \nGostosa2d: Manda gifs de gostosas de anime. \nAdm: Manda gifs do ademir kk. \nPai ta on: Manda gifs do pai ta on. \nFurro: Manda gifs dos furros, Deus me livre. \nPato: Manda gifs dos maravilhosos patos.  \nKawai: Manda gifs fofinhos >_<.\nBolsonaro: Manda gifs do nosso grande presidente bozorano. \nSalve: Você ganha um salve do bot(Muitom dahora). \nFrase: Lança a braba, Frase de alguem. \nHentai: Gera um link de hentai aleatorio.\n \n**Comandos Gerais:** \nAjuda: Mostra todos os comandos.\nPing: Testa o ping do bot! \nFale: O bot fala algo que você escrever. \nCriadores: Mostra os criadores do bot. \n \n**Comandos meme:** \nHipocrisia: Gera um meme com o texto escrito. **(BUGADO)** \n \n**Comandos staff:** \nPrefix: Edita o prefixo do bot** (ainda não está disponível)**. \nClear: Limpa o chat **(maximo 100)**. \n')

@bot.command()
async def ping(message):
    await message.send('**Latencia do bot de {0} ms**'.format(round(bot.latency, 1)))

@bot.command() 
async def fale(message, *, arg):
    await message.send(arg)

@bot.command()
async def criadores(message):
    await message.send('***LetsCodeBot criado por:*** \njv#3611 e Bielgomes#0313 \n \n**Os computadores são incrivelmente rápidos, precisos e burros; os homens são incrivelmente lentos, imprecisos e brilhantes; juntos, seus poderes ultrapassam os limites da imaginação.**\n \n***Albert Einstein***')

# FIM COMANDOS GERAIS / COMEÇO COMANDOS MEMES

@bot.command()
async def hipocrisia(message, *, arg):
    imagem = Image.open( 'hipocrisia.jpg' )
    fonte = ImageFont.truetype("arial.ttf", 20)
    text = arg
    w, h = fonte.getsize(text)
    draw = ImageDraw.Draw(imagem)
    draw.text(((500-w)/2, (100-h)/2), text, font=fonte, fill='white')
    imagem.save('tmp.png', format='PNG')
    file = discord.File(open('tmp.png', 'rb'))
    await message.channel.send(file=file)

# FIM COMANDOS MEMES / COMEÇO COMANDOS STAFF

@bot.command()
@commands.has_role('adm')
async def prefix(message):
    await message.send('***Ainda em desenvolvimento!***')

@bot.command() 
@commands.has_role('adm')                                                                                   
async def clear(message, amount=0):
    if amount > 100:
        await message.send('**Só limpo até 100 mensagens**', delete_after = 5) 
    else:
        await message.channel.purge(limit=amount)
        await message.send('**{}, {} mensagens foram apagadas!**'.format(message.author.mention, amount), delete_after = 10)

# FIM COMANDOS STAFF

@bot.command()
async def tapa(message, arg1):
    await message.send('**{} tomou um tapa de {}**'.format(arg1, message.author.mention))
    await message.send(choice(lista_gif_tapas))

#BOT TOKEN
bot.run('NzQ5Mjk2MDA1MDEwMjkyNzk2.X0p6SA.uGrJSvNCZrUg7weMU-qCxZ43Voc')