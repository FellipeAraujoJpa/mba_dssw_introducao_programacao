import random


def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas_permitidas = 10
    tentativas_feitas = 0

    print("Boas vendas. Iremos iniciar o jogo de adivinhas, preparado?")
    print("Eu escolhi um número entre 1 e 100.")
    print(f"Você tem {tentativas_permitidas} tentativas para adivinhar o número.")

    while tentativas_feitas < tentativas_permitidas:
        try:
            palpite = int(input("Faça seu palpite: "))
            tentativas_feitas += 1

            if palpite < 1 or palpite > 100:
                print("Por favor, escolha um número entre 1 e 100.")
                tentativas_feitas -= 1
                continue

            if palpite < numero_secreto:
                print("Seu palpite é muito baixo.")
            elif palpite > numero_secreto:
                print("Seu palpite é muito alto.")
            else:
                print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas_feitas} tentativas.")
                break
        except ValueError:
            print("Por favor, insira um número válido.")

    if tentativas_feitas == tentativas_permitidas:
        print(f"Você esgotou suas tentativas. O número era {numero_secreto}. Tente novamente!")


# Executa o jogo
jogo_adivinhacao()