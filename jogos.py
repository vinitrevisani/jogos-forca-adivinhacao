import forca
import adivinhacao

def escolher_jogo():
    print("---------------------------------")
    print("-------Escolha o seu jogo!-------")
    print("---------------------------------")

    print("(1) Forca (2) Adivinhação")

    resposta = int(input("Qual jogo? "))


    if(resposta == 1):
        forca.jogar()
    elif(resposta == 2):
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolher_jogo()