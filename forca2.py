import random


def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print("\n" f"\t\t\t\t\t\t\t\t\t\t\t\t\tA palavra secreta tem {len(palavra_secreta)} letras: ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t", letras_acertadas, "\n")

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:

        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
            print("\t\t\t\t\t\t\t\t\t\t\t\t\tOps, você errou! Faltam {} tentativas. \n".format(7 - erros))

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print("\t\t\t\t\t\t\t\t\t\t\t\t\t", letras_acertadas)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


def imprime_mensagem_abertura():
    print("\n" "\t\t\t\t\t\t\t\t\t\t\t\t\t************************************")
    print("\n" "\t\t\t\t\t\t\t\t\t\t\t\t\t***** BEM VINDO AO JOGO FORCA! *****")
    print("\n" "\t\t\t\t\t\t\t\t\t\t\t\t\t************************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for _ in palavra]


def pede_chute():
    chute = input("\t\t\t\t\t\t\t\t\t\t\t\t\tChute uma letra? ")
    chute = chute.strip().upper()

    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def imprime_mensagem_vencedor():
    print("\n""\n""\n""\t\t\t\t\t\t\t\t\t\t\t\t\tParabéns, você ganhou!")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t       ___________      ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t      '._==_==_=_.'     ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t      .-\\:      /-.    ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t     | (|:.     |) |    ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t      '-|:.     |-'     ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t        \\::.    /      ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t         '::. .'        ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t           ) (          ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t         _.' '._        ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("\n""\n""\n""\t\t\t\t\t\t\t\t\t\t\t\t\tPoxa, você foi enforcado!")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\tA palavra secreta era {}".format(palavra_secreta))
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t    _______________         ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t   /               \       ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t  /                 \      ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t//                   \/\  ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\|   XXXX     XXXX   | /   ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t |   XXXX     XXXX   |/     ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t |   XXX       XXX   |      ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t |                   |      ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t \__      XXX      __/     ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t   |\     XXX     /|       ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t   | |           | |        ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t   | I I I I I I I |        ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t   |  I I I I I I  |        ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t   \_             _/       ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t     \_         _/         ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t       \_______/           ")


def desenha_forca(erros):
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t  _______     ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t |/      |    ")

    if erros == 1:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |      (_)   ")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |            ")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |            ")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |            ")

    if erros == 2:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |      (_)   ")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |      \     ")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |            ")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |            ")

    if erros == 3:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |      (_)   ")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |      \|    ")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |            ")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |            ")

    if erros == 4:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |      (_)   ")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |      \|/   ")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |            ")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |            ")

    if erros == 5:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |      (_)   ")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |      \|/   ")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |       |    ")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |            ")

    if erros == 6:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |      (_)   ")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |      \|/   ")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |       |    ")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |      /     ")

    if erros == 7:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |      (_)   ")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |      \|/   ")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |       |    ")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t |      / \   ")

    print("\t\t\t\t\t\t\t\t\t\t\t\t\t |            ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t_|___         ")
    print()


if __name__ == '__main__':
    jogar()
