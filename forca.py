import random


def jogar():
    print("************************************")
    print("***** Bem vindo ao jogo forca! *****")
    print("************************************")

    arquivo = open("palavras.txt")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numeros = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numeros].upper()
    letras_acertadas = ["_" for _ in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))

        enforcou = erros == 3
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    print("Fim de jogo!")


if __name__ == '__main__':
    jogar()
