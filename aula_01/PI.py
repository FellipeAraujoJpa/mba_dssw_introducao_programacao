import random

def jogo_adivinha ():
    #O computador vai escolher um número e o usuário irá lançar um palpite para descobrir o número.
    numero_secreto = random.randint (1, 100)
    tentativas_permitidas = 15
    tentativas_realizadas = 0

    print("Olá, seja bem vindo. Vamos brinca? Que tal acertar o meu palpite?")
    print("Você precisar realizar um palpite utilizando o intervalo de 1 e 100")
    print (f"Resta {tentativas_permitidas} tentativas para você concluir.")

    while tentativas_realizadas < tentativas_permitidas:
            try:
                palpite = int(input("Realize o seu palpite."))
                tentativas_realizadas += 1

                if palpite < numero_secreto:
                    print ("Não foi dessa vez: Seu palpite é muito baixo.")
                    print (f"Falta {tentativas_permitidas - tentativas_realizadas} para encerrar.")
                elif palpite > numero_secreto:
                    print("Não foi dessa vez: Seu palpite está muito alto.")
                    print(f"Falta {tentativas_permitidas - tentativas_realizadas} para encerrar.")
                else:
                    print(f"Você venceu ihuuu {numero_secreto} em {tentativas_realizadas}")
            except ValueError:
                    print("Por favor, insira um número válido.")

    if tentativas_realizadas == tentativas_permitidas:
                print(f"Que pena, você perdeu. O número era {numero_secreto}. Tente novamente!")
# para finalizar o jogo
jogo_adivinha()