import os
import glob
import tailer # type: ignore
import ast
import threading
from sentence_transformers import SentenceTransformer, util
import datetime
import hashlib
from thefuzz import fuzz
import uuid
import time
import pyfiglet # type: ignore
import getpass
from rich.console import Console
from rich.markdown import Markdown
from tui import TUI as tui
iniciar_principal = False
def enviar_mp():
    while True:
        message = input("")
        if message == "!#@":
            chatopened == False
        os.system(f"echo {nick}: {message} >> {path}")
def receber_mp():
    while True:
        with open(path) as f:
            for line in tailer.follow(f):
                print(line)
ascii_art = pyfiglet.figlet_format("TTYSocial")
print(ascii_art)
time.sleep(3)
tui.texto("Bem vindo Ao TTYSocial!!!")
tui.texto("Faça Login:")
user = tui.entrada_linha_obrigatoria("Digite seu Usuário (ou digite REGISTRAR para se registrar): ")
if user != "REGISTRAR" and user != "Vovô Geraldo":
    if os.path.isfile(f'contas/{user}.txt'):
        password = tui.entrada_linha_obrigatoria("Agora, digite sua senha: ")
        password_hash = hashlib.sha512(password.encode('utf-8')).hexdigest()
        with open(f'contas/{user}.txt', 'r', encoding='utf-8') as arquivo:
            primeira_linha = arquivo.readline()
        if primeira_linha.strip() == password_hash:
            iniciar_principal = True
        else:
            tui.texto("ERRO: SENHA INVÁLIDA")
    else:
        tui.texto("ERRO CONTA NÃO EXISTENTE")
    if iniciar_principal == True:
        while True:
            menu_principal = [
            ("1", "Chat (EVENTO)"),
            ("2", "Fórum"),
            ("3", "T-Mail"),
            ("4", "Chat Privado"),
            ("5", "Chat em Grupo"),
            ("6", "Sites"),
            ("7", "Entrar na TEXTNet (Text Extensible Xenial Transfer Network)"),
            ("8", "Jogos"),
            ("9", "Wiki"),
            ("10","Referências")
            ]
            option = tui.menu(menu=menu_principal)
            match option:
                case "1":
                    menu_chat = [
                    ("1", "Geral"),
                    ("2", "Memes"),
                    ("3", "Pergunta do dia"),
                    ("4", "Guerras De Spam"),
                    ("5", "Assobio (Créditos: Associação Nacional do Assobio)")
                    ]
                    sala = tui.menu(menu=menu_chat)
                    match sala:
                        case "1":
                            path = "geral.txt"
                        case "2:":
                            path = "memes.txt"
                        case "3":
                            path = "perguntadodia.txt"
                        case "4":
                            path = "guerrasdespam.txt"
                        case "5":
                            path = "assobio.txt"
                    os.system("clear")
                    print("Levando ao chat...")
                    def receber_mp():
                        while True:
                            with open(path) as f:
                                for line in tailer.follow(f):
                                    print(line)
                            
                    nick = user
                    thread2 = threading.Thread(target=receber_mp, args=())
                    thread2.start()
                    chatopened = True
                    while chatopened == True:
                        message = input("")
                        if message == "!#@":
                            chatopened == False
                        os.system(f"echo {nick}: {message} >> {path}")
                case "2":
                    forum_opcoes = tui.entrada_linha_obrigatoria("Você pode criar um post apertando 1 ou ver posts criados com 2: ")
                    if forum_opcoes == "1":
                        nome_post = tui.entrada_linha_obrigatoria("Digite o nome do post: ")
                        texto_final = tui.entrada_multilinha("Digite seu texto (pressione TAB e depois ENTER para finalizar): ")
                        print("Criando post.....")
                        data = datetime.datetime.now()
                        os.system(f'echo "{texto_final}" >> "forum/{nome_post} Por {user} {data}.txt"')
                    elif forum_opcoes == "2":
                        menu_forum = []
                        numerodepostsforum = int(tui.entrada_linha_obrigatoria("Até qual id de post você quer ver? (0 = mais recente) "))
                        tui.texto("Aqui estão os posts do fórum:")
                        lista_txt = glob.glob('forum/*.txt')
                        for indice, valor in enumerate(lista_txt):
                            valor1 = valor.replace('txt', '')
                            valor2 = valor1.replace('forum/', '')
                            if indice < numerodepostsforum+1:
                                menu_forum.append(ast.literal_eval(f"('{indice}', '{valor2}')"))
                        postaler = tui.menu(menu_forum)
                        with open(lista_txt[int(postaler)], 'r', encoding='utf-8') as file:
                            conteudo = file.read()
                            tui.texto(conteudo)

                case "3":
                    menu_tmail = [
                    ("1" ,"Enviar T-Mails"),
                    ("2" ,"Ler Meus T-Mails")]

                    option_tmail = tui.menu(menu_tmail)
                    if option_tmail == "1":
                        destinatario = tui.entrada_linha_obrigatoria("Digite o nome do usuário que quer enviar: ")
                        if os.path.isdir(f"tmail/{destinatario}"):
                            titulo = tui.entrada_linha_obrigatoria("Digite o título do T-Mail")
                            tmail_final = tui.entrada_multilinha("Digite sua mensagem (pressione TAB e depois ENTER para finalizar): ")
                            data = datetime.datetime.now()
                            os.system(f'echo Por {user} "{tmail_final}" >> tmail/{destinatario}/{titulo}:{data}.txt')
                            
                    elif option_tmail == "2":
                        numerodeposts = int(tui.entrada_linha_obrigatoria("Até qual id de tmail você quer ver? (0 = mais recente) "))
                        lista_txt = glob.glob(f'tmail/{user}/*')
                        menu_tmails = []
                        for indice, valor in enumerate(lista_txt):
                            valor1 = valor.replace('txt', '')
                            valor2 = valor1.replace(f'tmail/{user}', '')
                            valor3 = valor2.replace('/', '')
                            if indice < numerodeposts+1:
                                menu_tmails.append(ast.literal_eval(f"('{indice}', '{valor3}')"))
                        postaler = tui.menu(menu_tmails)
                        numeropost = int(postaler)
                        with open(lista_txt[numeropost], 'r', encoding='utf-8') as file:
                            conteudo = file.read()
                            tui.texto(conteudo)
                case "4":
                    usuario_chat = tui.entrada_linha_obrigatoria("Digite o nome do Usuário a conversar ")
                    if os.path.isfile(f"contas/{usuario_chat}.txt"):
                        if user < usuario_chat:
                            path = f'mp/{user}:{usuario_chat}.txt'
                        else:
                            path = f'mp/{usuario_chat}:{user}.txt'
                        os.system(f'touch {path}')
                        nick = user 
                        chatopened = True
                        os.system("clear")
                        thread = threading.Thread(target=receber_mp, args=())
                        thread.start()
                        while chatopened == True:
                            message = input("")
                            if message == "!#@":
                                chatopened == False
                            os.system(f"echo {nick}: {message} >> '{path}'")        
                case "5":
                    [
                    ("1", "Criar novo Grupo"),
                    ("2", "Entrar Em Grupo" )
                    ]
                    acao = tui.menu("Qual opção você quer?")
                    match acao:
                        case "1":
                            senha = tui.entrada_linha("Digite a senha do seu novo grupo:  (Enter para confirmar ou pular)")
                            senha_grupo_hash = hashlib.sha512(senha.encode()).hexdigest()
                            grupo_uuid = uuid.uuid4()
                            os.system(f'echo "" >> grupos/{grupo_uuid}¨{senha_grupo_hash}.txt')
                            tui.texto("Criado!")
                            tui.texto(f"Aqui está o UUID do seu grupo, apenas compartilhe para quem quiser que possa entrar nele: {grupo_uuid}")
                        case "2":
                            uuid_grupo = tui.entrada_linha_obrigatoria('Digite o UUID do Grupo: ')
                            senha_grupo = tui.entrada_linha('E agora a senha dele: (Enter para confirmar ou pular))')
                            senha_hash = hashlib.sha512(senha_grupo.encode()).hexdigest()
                            if os.path.isfile(f"grupos/{uuid_grupo}¨{senha_hash}.txt"):
                                os.system("clear")
                                path = f"grupos/{uuid_grupo}¨{senha_hash}.txt"
                                nick = user
                                thread2 = threading.Thread(target=receber_mp, args=())
                                thread2.start()
                                chatopened = True
                                while chatopened == True:
                                    message = input("")
                                    if message == "!#@":
                                        chatopened == False
                                    os.system(f"echo {nick}: {message} >> {path}")
                
                case "6":
                    opcao_sites = tui.entrada_linha_obrigatoria("Digite 1 Para Ver sites existentes ou 2 criar um site")
                    match opcao_sites:
                        case "1":
                            link = tui.entrada_linha_obrigatoria("Digite o nome do site ")
                            tempo = int(tui.entrada_linha_obrigatoria("Quando acessar o site, quanto tempo em segundos você quer para ler antes de voltar ao menu?"))
                            if os.path.isfile(f"sites/{link}"):
                                console = Console()
                                with open(f"sites/{link}", "r") as f:
                                    markdown_text = Markdown(f.read())
                                
                                console.print(markdown_text)
                                time.sleep(tempo)
                        case "2":
                            titulo = tui.entrada_linha_obrigatoria("Digite o nome do site ")
                            if not os.path.isfile(f"sites/{titulo}"):
                                site_final = tui.entrada_multilinha("Digite Conteúdo do seu site (Markdown È suportado) (pressione TAB e depois ENTER para finalizar): ")
                                print("Criando Site...")
                                os.system(f"echo '{site_final}' >> 'sites/{titulo}'")
                            else: print("Nome já usado")
                case "7":
                    exec(open("TEXTNet.py").read())
                case "8":
                    opcao_jogos = tui.entrada_linha_obrigatoria("Aperte 1 para jogar jogos ou 2 Para pedir para um jogo ser adicionado")
                    match opcao_jogos:
                        case "1":
                            menu_jogos = [
                            ("1", "Pac-Man"),
                            ("2", "Nethack (RPG em inglês)"),
                            ("3", "Tetris")
                            ]
                            opcao_jogo = tui.menu(menu_jogos)
                            match opcao_jogo:
                                case "1":
                                    os.system("pacman4console")
                                case "2":
                                    os.system("nethack")
                                case "3":
                                    os.system("/snap/bin/tetris-thefenriswolf.tetris")
                        case "2":
                            nome_jogo = tui.entrada_linha_obrigatoria("Digite o Nome Do jogo: ")
                            codigo_final = tui.entrada_multilinha("Digite o Código do seu Jogo \nRegras \n Não Vale executar comandos nem criar arquivos \nO jogo Deve ser apenas em texto, sem interface gráfica\nSem Conteúdo sexual.\n (pressione TAB e depois ENTER para finalizar)")
                            tui.texto("Submetendo Jogo... para Avaliação...")
                            with open(f"pedidos-de-jogos/{str(uuid.uuid4())}.txt", "x") as arquivo:
                                arquivo.write(f"{user}:{datetime.datetime.now()}\n{codigo_final}")
                case "9":
                    menu_wiki = [
                        ("1", "Criar Nova página"),
                        ("2", "Ver página existente")
                    ]
                    opcao_wiki = tui.menu(menu_wiki)
                    match opcao_wiki:
                        case "1":
                            paginacriada = False
                            lista_txt_wiki = glob.glob(f'wiki/*')
                            nome_pagina = tui.entrada_linha_obrigatoria("Digite o nome da página")
                            for valor in lista_txt_wiki:
                                valor1 = valor.replace('txt', '')
                                valor2 = valor1.replace('wiki/', '')
                                modelo = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
                                vetor1 = modelo.encode(valor2)
                                vetor2 = modelo.encode(nome_pagina)
                                if util.cos_sim(vetor1, vetor2) >= 0.5:
                                    paginacriada = True
                                    nomeparecido = valor2
                            if paginacriada == True:
                                tui.texto(f"Página semelhante já criada com o nome de: {nomeparecido}")
                            else:
                                conteudo_pagina = tui.entrada_multilinha("Agora digite o Conteúdo da Página, Markdown é suportado")
                                os.system(f"echo '{conteudo_pagina}' >> wiki/{nome_pagina}")
                                tui.texto("Criado!")
                        case "2":
                            conteudo_a_ler = tui.entrada_linha_obrigatoria("Digite o nome da página a ler:")
                            with open(f"wiki/{conteudo_a_ler}", "r") as f:
                                markdown_pagina = markdown_text = Markdown(f.read())
                            tempo_a_ler = tui.entrada_linha_obrigatoria("Quanto tempo você quer para ver a página antes de voltar ao menu?")
                            console = Console()
                            os.system("clear")
                            console.print(markdown_pagina)
                            time.sleep(int(tempo_a_ler))
                case "10":
                    tui.texto("")
                case _:
                    print("Opção Inválida")
elif user == "Vovô Geraldo":
    tui.texto("Memorial ao Meu Avô Falecido Geraldo Garcia do Amaral")
    tui.texto("1: Históŕias")
    tui.texto("2: Emprego")
    tui.texto("3: Bar")
    tui.texto("4: Final da vida e Falecimento")
    opção = tui.entrada_linha_obrigatoria("Oque Você quer saber sobre ele? ")
    match int(opção):
        case 1:
            tui.texto("1: A vez que ele (quase) se formou em química")
            opcao_historias = int(tui.entrada_linha_obrigatoria("Escolha uma opção"))
            match opcao_historias:
                case 1:
                    tui.texto("Era uma vez o meu avô, ele queria ir para uma universidade, mas tinha um problema, ele só fez escola até o primeiro ensino fundamental, então ele sabia quase nada para passar em um vesibular")
                    tui.texto("Mas o meu avô era dedicado, ele estudou muito, e quando digo muito, digo muito mesmo, e advinha só? ele passou em uma universidade de química!")
                    tui.texto("Ná Època, ser formado em química era ter uma vida bem sucedida garantida. além dissoa ajudar ele no emprego que ele queria, Cavador De Poço")
                    tui.texto("Mas infelizmente, como ele só estudou até a quinta série(antes de ter que trabalhar na roça com o pai dele), ele não entendia quase nada das aulas e teve que abandonar o estudo")
        case 2:
            tui.texto("Meu avô originalmente trabalhava como cavador de poço, mas isso exigia ele ter que ir para muito longe(no interior do maranhão(sim, ele nasceu lá)) para cavar os poços, afinal, os locais perto da capital ja tinham água potável. Então Depois dele se aposentar, ele decidiu abrir um bar")
        case 3:
            tui.texto("Quando meu avô abriu um bar, ele foi um sucesso, mas logo outras pessoas começaram a gerar concorrencia abrindo outros bares na região, mas meu Avô era um excelente estragegista comercial e os outros bares acabaram fechando por não conseguir concorrer com o bar do meu avô")
            tui.texto("O problema é que, além de gerir o bar, ele também bebia muito no própio bar dele, e quando ele ficava bêbado, sobrava pro meu pai cuidar do bar até ele ficar normal denovo")
            tui.texto("mas meu avô percebeu que isto estava prejudicando o desenvolvimento do meu pai, então ele conseguiu parar de beber")
        case 4:
            tui.texto("Muitas Décadas depois, o meu avô ja estava velhino e com alzheimer, mas ele cuidava muito bem da cabeça, então os sintomas não estavam aparecendo, além de ir na academia")
            tui.texto("Mas Chegou a COVID-19, e ele ficou muito parado sem fazer nada, com isso, os sintomas começaram a aparecer")
            tui.texto("Depois Da COVID ele ficou uns 5-6 anos em estágio cada vez pior de alzheimer, nos seus últimos meses, ele não conseguia mais engolir alimento, falar direito, andar, e coisas do tipo")
            tui.texto("Como ele não conseguia engolir alimento direito, o alimento acabava entrando no pulmão dele, e assim ele tinha pneumonia atrás de pneumonia, até que ele ficou itnernado por quase um mês até ele falecer")
            tui.texto("Meu Avô era um homem muito trabalhador, bondoso, justo, preucupado com a família, e, mais do que tudo, tinha um bom coração")
else:
    usuario_registrar = tui.entrada_linha_obrigatoria("Digite seu Novo Nome de Usuaŕio: ")
    if usuario_registrar != "REGISTRAR":
        if usuario_registrar != "Vovô Geraldo":
            senha_registrar = tui.entrada_linha_obrigatoria("Digite sua nova senha: ")
            senha_registrar_hash = hashlib.sha512(senha_registrar.encode('utf-8')).hexdigest()
            print("Salvando Usuário...")
            if not os.path.isfile(f"'contas/{usuario_registrar}.txt'"):
                os.system(f'echo "{senha_registrar_hash}" >> "contas/{usuario_registrar}.txt"')
                os.system(f"mkdir 'tmail/{usuario_registrar}'")
                os.system(f"touch 'tmail/{usuario_registrar}/Voltar.txt'")
                os.system(f"touch 'mp/{usuario_registrar}.txt'")
                tui.texto("Usuário Salvo!") 
        else: tui.texto("Nome de Usuário Já usado para o memorial do meu avô falecido")
    else: tui.texto("Usuário Inválido")
