import random

def jogo_adivinha ():
    numero_secreto = random.randint (1,100) #a maquina vai gerar um numero secreto dentro desse intervalo
    tentativas_permitidas = 10 #quantidades permitidas que o jogador irá possuir para descobrir o número secreto
    tentativas_realizadas = 0

    #print de instruções e boas vindas sobre o jogo de adivinha
    print ("Olá, seja bem vindo ao jogo de adivinha. Vamos tentar descobri o meu palpite?")
    print("Você precisa utilizar o intervalo entre 1 e 100 nos seus palpites.")
    print(f"Você tem {tentativas_permitidas} tentativas para conseguir.")
    print("Vamos iniciar. Boa sorte!")

    while tentativas_realizadas < tentativas_permitidas:
        try:
            palpite = int (input("Digite o seu palpite:")) #o jogador precisar inserir o palpite entre o intervalo permitido
            tentativas_realizadas += 1
            if palpite < 1 or palpite > 100: #se o palpite for menor que 1 e maior que 100 gerar um print informando que o palpite não é valido.
                print("O número que você digitou não é valido, por favor digite um número valido.")
                print("Restam", tentativas_permitidas - tentativas_realizadas, "tentativas.")
                continue
            if palpite < numero_secreto:
                print ("Não foi dessa vez, seu palpite é MUITO BAIXO.") #caso o palpite do jogador for menor que o número secreto, vai gerar esse print
                print (f"Você tem {tentativas_permitidas-tentativas_realizadas} tentativas disponiveis.") #vai informar quantas tentativas disponiveis ainda tem restante
            elif palpite > numero_secreto:
                print("Não foi dessa vez, seu palpite é MUITO ALTO.") #caso o palpite do jogador for maior que o número secreto, vai gerar esse print
                print(f"Você tem {tentativas_permitidas-tentativas_realizadas} tentativas disponiveis.") #vai informar quantas tentativas disponiveis ainda tem restante
            else:
                print("IHUMMM, Você acertou o número secreto ",numero_secreto," na tentatina Nº ",tentativas_realizadas,"") #caso o jogador acerte o palpite, irá gerar esse print
                break #finaliza o jogo
        except ValueError:
            print ("Por favor, insira um número no intervalo de 1 a 100.") #caso o jogador insira um valor diferente de inteiro
            tentativas_realizadas += 1
            print("Restam", tentativas_permitidas - tentativas_realizadas, "tentativas.")
    if tentativas_realizadas == tentativas_permitidas: #quando consumiu todas as tentativas de palpite
        print("Que pena, você perdeu. Tente novamente.") #caso não tenha mais jogadas permitidas para o jogador lançar o palpite
        return
jogo_adivinha()



