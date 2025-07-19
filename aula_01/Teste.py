'''
def multiplica(n1,n2):
    teste = n1*n2
    return teste

while True:
    n1=int (input("Digite o número 1"))
    n2=int (input("Digite o número 2"))

    resultado = multiplica(n1,n2)
    print (resultado)

    continuar = input("Queres continuar?")
    if continuar.lower() != 'sim':
        print("Programa encerrado.")
        break
'''
from test.test_ntpath import tester




def subtracao (n1,n2):
    teste = n1-n2
    return teste
while True:
    n1=int (input("Digite o ano atual."))
    n2=int (input("Digite o ano que você nasceu."))
    Resultado = subtracao (n1,n2)
    print (Resultado, "Anos de idade")

    if Resultado > 18:
        print ("Você é maior de idade.")
    else:
        print ("Você é menor de idade.")
    break











