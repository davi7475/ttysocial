import os
import glob
import tailer
import threading
import datetime
import hashlib
import uuid
import pyfiglet
import getpass
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
print("Bem vindo Ao TTYSocial!!!")
print("Faça Login:")
user = input("Digite seu Usuário (ou digite REGISTRAR para se registrar): ")
if user != "REGISTRAR":
    if os.path.isfile(f"contas/{user}.txt"):
        password = getpass.getpass("Agora, digite sua senha: ")
        password_hash = hashlib.sha512(password.encode('utf-8')).hexdigest()
        with open(f'contas/{user}.txt', 'r', encoding='utf-8') as arquivo:
            primeira_linha = arquivo.readline()
        if primeira_linha.strip() == password_hash:
            iniciar_principal = True
        else:
            print("ERRO: SENHA INVÁLIDA")
    else:
        print("ERRO CONTA NÃO EXISTENTE")
    if iniciar_principal == True:
        while True:
            print("Digite Uma opção:")
            print("1: Chat")
            print("2: Fórum")
            print("3: T-Mail")
            print("4: Chat Privado")
            print("5: Chat em Grupo")
            print("6: Entrar na TEXTNet (Text Extensible Xenial Transfer Network)")
            option = input("--> ")
            match option:
                case "1":
                    print("1: Geral")
                    print("2 Memes")
                    print("3:Pergunta do dia")
                    print("4: Guerras De Spam")
                    sala = input("Qual chat você quer? ")
                    match sala:
                        case "1":
                            path = "geral.txt"
                        case "2:":
                            path = "memes.txt"
                        case "3":
                            path = "perguntadodia.txt"
                        case "4":
                            path = "guerrasdespam.txt"

                    print("Levando ao chat...")
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
                    forum_opcoes = input("Você pode criar um post apertando 1 ou ver posts criados com 2: ")
                    if forum_opcoes == "1":
                        print("Digite o nome do post: ")
                        nome_post = input()
                        print("Digite seu texto (digite '!#@' em uma nova linha para finalizar): ")
                        linhas = []
                        while True:
                            linha = input()
                            if linha.strip() == '!#@':
                                break
                            linhas.append(linha)
                        texto_final = "\n".join(linhas)
                        print("Criando post.....")
                        data = datetime.datetime.now()
                        os.system(f'echo "{texto_final}" >> "forum/{nome_post} Por {user} {data}.txt"')
                    elif forum_opcoes == "2":
                        numerodepostsforum = int(input("Até qual id de post você quer ver? (0 = mais recente) "))
                        print("Aqui estão os posts do fórum:")
                        lista_txt = glob.glob('forum/*.txt')
                        for indice, valor in enumerate(lista_txt):
                            valor1 = valor.replace('txt', '')
                            valor2 = valor1.replace('forum/', '')
                            if indice < numerodepostsforum+1:
                                print(f"ID:: {indice}, Título: {valor2}")
                        postaler = input("Qual o ID do post você quer ler? ")
                        numeropost = int(postaler)
                        with open(lista_txt[numeropost], 'r', encoding='utf-8') as file:
                            conteudo = file.read()
                            print(conteudo)

                case "3":
                    print("1: Enviar T-Mails")
                    print("2: Ler Meus T-Mails")
                    option_tmail = input("Selecione uma das opções acima:   ")
                    if option_tmail == "1":
                        destinatario = input("Digite o nome do usuário que quer enviar: ")
                        if os.path.isdir(f"tmail/{destinatario}"):
                            titulo = input("Digite o título do T-Mail")
                            print("Digite seu texto (digite '!#@' em uma nova linha para finalizar): ")
                            linhas = []
                            while True:
                                linha = input()
                                if linha.strip() == '!#@':
                                    break
                                linhas.append(linha)
                            tmail_final = "\n".join(linhas)
                            data = datetime.datetime.now()
                            os.system(f'echo Por {user} "{tmail_final}" >> tmail/{destinatario}/{titulo}:{data}.txt')
                            
                    elif option_tmail == "2":
                        numerodeposts = int(input("Até qual id de tmail você quer ver? (0 = mais recente) "))
                        lista_txt = glob.glob(f'tmail/{user}/*')
                        for indice, valor in enumerate(lista_txt):
                            valor1 = valor.replace('txt', '')
                            valor2 = valor1.replace(f'tmail/{user}', '')
                            valor3 = valor2.replace('/', '')
                            if indice < numerodeposts+1:
                                print(f"ID: {indice}, Título: {valor3}")
                        postaler = input("Qual o ID do tmail você quer ler? ")
                        numeropost = int(postaler)
                        with open(lista_txt[numeropost], 'r', encoding='utf-8') as file:
                            conteudo = file.read()
                            print(conteudo)
                case "4":
                    usuario_chat = input("Digite o nome do Usuário a conversar ")
                    if os.path.isfile(f"contas/{usuario_chat}.txt"):
                        if user < usuario_chat:
                            path = f"mp/{user}:{usuario_chat}.txt"
                        else:
                            path = f"mp/{usuario_chat}:{user}.txt"
                        os.system(f"touch {path}")
                        nick = user 
                        chatopened = True
                        os.system("clear")
                        thread = threading.Thread(target=receber_mp, args=())
                        thread.start()
                        while chatopened == True:
                            message = input("")
                            if message == "!#@":
                                chatopened == False
                            os.system(f"echo {nick}: {message} >> {path}")        
                case "5":
                    print("Oque Você Quer fazer?")
                    print("1: Criar novo Grupo")
                    print("2: Entrar Em Grupo" )
                    acao = input("-> ")
                    match acao:
                        case "1":
                            senha = input("Digite a senha do seu novo grupo:  ")
                            senha_grupo_hash = hashlib.sha512(senha.encode()).hexdigest()
                            grupo_uuid = uuid.uuid4()
                            os.system(f'echo "" >> grupos/{grupo_uuid}¨{senha_grupo_hash}.txt')
                            print("Criado!")
                            print("Aqui está o UUID do seu grupo, apenas compartilhe para quem quiser que possa entrar nele:    " \
                            f"{grupo_uuid}")
                        case "2":
                            uuid_grupo = input('Digite o UUID do Grupo: ')
                            senha_grupo = input('E agora a senha dele: ')
                            senha_hash = hashlib.sha512(senha_grupo.encode()).hexdigest()
                            if os.path.isfile(f"grupos/{uuid_grupo}¨{senha_hash}.txt"):
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
                    exec(open("TEXTNet.py").read())
                case _:
                    print("Opção Inválida")

else:
    usuario_registrar = input("Digite seu Novo Nome de Usuaŕio: ")
    if usuario_registrar != "REGISTRAR":
        senha_registrar = input("Digite sua nova senha: ")
        senha_registrar_hash = hashlib.sha512(senha_registrar.encode('utf-8')).hexdigest()
        print("Salvando Usuário...")
        if not os.path.isfile(f"contas/{usuario_registrar}.txt"):
            os.system(f'echo "{senha_registrar_hash}" >> "contas/{usuario_registrar}.txt"')
            os.system(f"mkdir tmail/{usuario_registrar}")
            os.system(f'touch tmail/{usuario_registrar}/Voltar.txt"')
            os.system(f'touch mp/"{usuario_registrar}.txt"')
            print("Usuário Salvo!") 
