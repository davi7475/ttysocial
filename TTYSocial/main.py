import os
import glob
import tailer
import threading
import datetime
import hashlib
iniciar_principal = False
def receber_msg():
    while chatopened == True:
        with open(salaarquivo) as f:
         for line in tailer.follow(f):
            print(line)
def enviar_msg():
    match sala:
        case "1":
            salaarquivo = "geral.txt"
        case "2:":
            salaarquivo = "memes.txt"
        case "3":
            salaarquivo = "perguntadodia.txt"
        case "4":
            salaarquivo = "guerrasdespam.txt"

    while chatopened == True:
        message = input("")
        if message == "/exit":
              chatopened == False
        os.system(f"echo {nick}: {message} >> {salaarquivo}")
print("Bem vindo Ao TTYSocial!!!")
print("Faça Login:")
user = input("Digite seu Usuário (ou digite REGISTAR para se registrar): ")
if user != "REGISTRAR":
    if os.path.isfile(f"contas/{user}.txt"):
        password = input("Agora, digite sua senha: ")
        password_hash = hashlib.sha512(password.encode('utf-8')).hexdigest()
        with open(f'contas/{user}.txt', 'r', encoding='utf-8') as arquivo:
            primeira_linha = arquivo.readline()
        if primeira_linha.strip() == password_hash:
            iniciar_principal = True
    else:
        print("ERRO")
    if iniciar_principal == True:
        while True:
            print("Digite Uma opção:")
            print("1: Chat")
            print("2: Fórum")
            print("3: T-Mail")
            option = input("-->")
            match option:
                case "1":
                    print("1: Geral")
                    print("2 Memes")
                    print("3:Pergunta do dia")
                    print("4: Guerras De Spam")
                    sala = input("Qual chat você quer?")
                    match sala:
                        case "1":
                            salaarquivo = "geral.txt"
                        case "2:":
                            salaarquivo = "memes.txt"
                        case "3":
                            salaarquivo = "perguntadodia.txt"
                        case "4":
                            salaarquivo = "guerrasdespam.txt"

                    print("Levando ao chat...")
                    nick = user 
                    os.system("clear")
                    chatopened = True
                    enviar_thread = threading.Thread(target=enviar_msg, args=(""))
                    enviar_thread.start()
                    recv_thread = threading.Thread(target=receber_msg, args=(""))
                    recv_thread.start()
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
                        print("Aqui estão todos os posts do fórum:")
                        lista_txt = glob.glob('forum/*.txt')
                        for indice, valor in enumerate(lista_txt):
                            valor1 = valor.replace('txt', '')
                            valor2 = valor1.replace('forum/', '')
                            print(f"ID:: {indice}, Título: {valor2}")
                        postaler = input("Qual o ID do post você quer ler? ")
                        numeropost = int(postaler)
                        with open(lista_txt[numeropost], 'r', encoding='utf-8') as file:
                            conteudo = file.read()
                            print(conteudo)

                case "3":
                    print("1: Enviar T-Mails")
                    print("2: Ler Meus T-Mails")
                    option_tmail = input("Selecione uma das opções acima:")
                    if option_tmail == "1":
                        destinatario = input("Digite o nome do usuário que quer enviar:")
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
                        lista_txt = glob.glob(f'tmail/{user}/*')
                        for indice, valor in enumerate(lista_txt):
                            valor1 = valor.replace('txt', '')
                            valor2 = valor1.replace(f'tmail/{user}', '')
                            valor3 = valor2.replace('/', '')
                            print(f"ID:: {indice}, Título: {valor3}")
                        postaler = input("Qual o ID do tmail você quer ler? ")
                        numeropost = int(postaler)
                        with open(lista_txt[numeropost], 'r', encoding='utf-8') as file:
                            conteudo = file.read()
                            print(conteudo)
                        
                case _:
                    print("Opção Inválida")
                
else:
    usuario_registrar = input("Digite seu Novo Nome de Usuaŕio: ")
    if usuario_registrar != "REGISTRAR":
        senha_registrar = input("Digite sua nova senha: ")
        senha_registrar_hash = hashlib.sha512(senha_registrar.encode('utf-8')).hexdigest()
        print("Salvando Usuário...")
        if not os.path.isfile(f"/contas/{usuario_registrar}.txt"):
            os.system(f'echo "{senha_registrar_hash}" >> "contas/{usuario_registrar}.txt"')
            os.system(f"mkdir tmail/{usuario_registrar}")
            print("Usuário Salvo!")
