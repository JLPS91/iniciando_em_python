import forca
import adivinhacao
import forca2

print("*************************************")
print("******** Escolha o seu jogo! ********")
print("*************************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo?"))

if jogo == 1:
    print("Jogando forca")
    forca2.jogar()
elif jogo == 2:
    print("Jogando adivinhação")
    adivinhacao.jogar()


