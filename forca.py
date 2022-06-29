import random

def jogar():
    abertura()
    palavra_secreta = gerar_palavra()

    letras_acertadas = contar_letras(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):  # enquanto não errou tudo e enquanto não acertou, continua no loop

        chute = iniciar_chute()

        if (chute in palavra_secreta):
            chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)

        print(letras_acertadas)
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

    if(acertou):
        acertou_palavra()
    else:
        errou_palavra(palavra_secreta)


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def acertou_palavra():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def errou_palavra(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def abertura():

    print("---------------------------")
    print("Bem vindo ao Jogo de Forca!")
    print("---------------------------")

def gerar_palavra():

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))

    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def contar_letras(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def iniciar_chute():
    chute = input("Qual letra?")
    chute = chute.strip().upper()
    return chute

def chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1


if (__name__ == "__main__"):  # só iniciar a função caso esse seja o programa principal
    jogar()

