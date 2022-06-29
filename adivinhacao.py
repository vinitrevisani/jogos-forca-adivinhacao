import random
def jogar():
    print("---------------------------------")
    print("Bem vindo ao Jogo de Adivinhação!")
    print("---------------------------------")

    numero_secreto = round(random.randrange(1,101))
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    dificuldade = int(input("Digite o nível:"))

    if(dificuldade == 1):
        total_de_tentativas = 12
    elif(dificuldade == 2):
        total_de_tentativas = 6
    else:
        total_de_tentativas = 3

    for rodada in range(1, total_de_tentativas + 1) :
        print("Tentativa {} de {}".format(rodada , total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")

        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue



        print("Você digitou" , chute)

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto



        if(acertou):
            print(f"Você acertou, sua pontuação foi {pontos}")
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor que o número secreto.")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos


    print(f"O numero secreto era {numero_secreto}")
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()