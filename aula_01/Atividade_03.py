valor_produto = float(input("Digite o valor do produto:"))
desconto = float(input("Quantos % o produto tem para pagamento a vista:"))

valor_desconto = (valor_produto * desconto) /100
valor_final = (valor_produto - valor_desconto)
print(f' O valor final é {valor_final: .2f}')
print(f' O valor do desconto é {valor_desconto: .2f}')



