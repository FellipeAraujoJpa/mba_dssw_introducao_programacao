'''
def PrimeiraFunc():
    print ("Hojé é dia de eleição")
    print ("É para votar no 22")
    print ("João Pessoa precisa do novo")
def SegundaFunc():
    print ("Não importa o quanto você tenha errado")
    print ("O Senhor tem sempre algo novo")
    print ("Para sua vida")

PrimeiraFunc()
SegundaFunc()
'''
from test.support.asyncore import write
from test.test_doctest.sample_doctest import y_is_one
from test.test_long import truediv

'''
def ola (nome):
    print ("Olá",nome)
    print ("Seja bem vindo")
ola ("Luiz")
'''

'''
def adicionaDois(numero):
    numero +=2
    return numero

inteiro=10
inteiro = adicionaDois (inteiro)
print (inteiro)
'''
'''
def multiplica(n1,n2):
    return n1 * n2
multiplica(10,2)
print (multiplica (10,2))
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
    if continuar.lower() != 's':
        print("Programa encerrado.")
        break



'''
def multiplica(num1=2, num2=2):
    return num1 * num2
print(multiplica())
'''
'''
def multiplicaNumeros(*varArgs):
    total = 1
    for arg in varArgs:
        total *=arg
        return total
print(multiplicaNumeros(5,5,5))
'''

'''
f=lambda x,y: x*y
print (f (2,4))

f =lambda x,y=3: x*y
print (f(2))

f=lambda x,y,w : x*y*w
print (f (w=2,y=2,x=2))
'''








