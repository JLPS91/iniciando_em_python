import random


def jogar():
    print("***********************************")
    print(" BEM VINDO AO JOGO DE ADIVINHAÇÃO!")
    print("***********************************")

    numero_secreto = random.randrange(1, 101)
    print(numero_secreto)
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nivel: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print(f"Você digitou o número {chute_str}")
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou! E fez {} pontos".format(pontos))
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior que o numero secreto.")
            elif menor:
                print("Você errou! O seu chute foi menor que o numero secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim de jogo!")

if __name__ == '__main__':
    jogar()
