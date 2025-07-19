'''
clientes = int(input ('Quantos clientes ativos tem em sua empresa?'))
precos = float (input ('Qual o valor da mensalidade paga pelos clientes?'))
ano = float (input('Quantos meses foram pagos de mensalidades?'))
print(precos*clientes*ano)
print (f"No ano em vigência, você teve um lucro total de: R${precos*clientes*ano}.")
'''
from test.test_ntpath import tester


def multiplicaçao (n1,n2,n3):
    Teste = n1*n2*n3
    return Teste
while True:
    nome = input('Digite o nome da cliente que está devendo:')
    n1 = int (input('Qual o valor da mensalidade?'))
    n2 = int (input('Quantos meses está em aberto?'))
    n3 = int (input('Quais porcentos de juntos será cobrado?'))
    Resultado = n1*n2*n3
    print (nome, ('está lhe devendo o valor de'), Resultado)
    break








