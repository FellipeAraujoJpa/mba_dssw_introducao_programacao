#input - comando para requerer informação do usuario
#variável = input ("mensagem:")

#nome = input ("Digite seu nome:")
#saudacao = "Olá, " + nome
#print (saudacao)

#junta as informações
#num1 = input("Digite o primeiro numero: ")
#num2 = input("Digite o segundo número: ")
#print(num1 + num2)

#Soma os números
#num1 = int (input("Digite o primeiro numero: "))
#num2 = int (input("Digite o segundo número: "))
#print(num1 + num2)

try:
  num1 = int (input("Digite o primeiro numero: "))
  num2 = int (input("Digite o segundo número: "))
except:
    print ("Você deve inseir números inteiros.")
else:
  print(num1 + num2)