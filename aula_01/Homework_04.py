metros = float(input("Digite sua altura (mts):"))
peso = float(input("Digite seu peso (kg):"))
IMC = peso / (metros * metros)
print(f"O seu IMC é de {IMC: .2F}")

if IMC >= 30:
    print("Você está acima do peso indicado")
else:
        print("Você está no peso adequado")