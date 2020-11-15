import forca
import adivinhacao

def escolhe_jogos():
    print("*********************************")
    print("*******Escolha o seu jogo*******!")
    print("*********************************")

    print("(1) Forca, (2) Adivinhação")

    jogo = int(input("Qual Jogo"))

    if(jogo == 1):
        print("Jogo Da Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Adivinhacao")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogos()