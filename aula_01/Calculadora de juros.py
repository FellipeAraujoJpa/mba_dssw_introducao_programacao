def multiplicaçao (n1,n2):
    Teste = n1*n2
    return Teste
while True:
    nome = input('Digite o nome da cliente que está devendo:')
    n1 = int (input('Qual o valor da mensalidade?'))
    n2 = int (input('Quantos meses está em aberto?'))

    divida = (n1*n2)
    juros = (n2 * n1 * 0.05)
    valor_atualizado = (divida + juros)
    desconto = (juros * 0.5)
    #desconto - (valor_atualizado * 0.5)
    print('o valor do seu debito é:', divida)
    print('o valor dos juros atualizados é:', juros)
    print (nome, 'o seu debito atualizado é', valor_atualizado)
    print('Desconto de 50% para fechar hoje', valor_atualizado - desconto)
    break