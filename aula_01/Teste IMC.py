def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2)


def classificar_imc(imc):
    if imc < 16.0:
        return "Desnutrição severa"
    elif 16.0 <= imc < 17.0:
        return "Desnutrição leve"
    elif 17.0 <= imc < 18.5:
        return "Desnutrido"
    elif 18.5 <= imc < 25.0:
        return "Peso normal"
    elif 25.0 <= imc < 30.0:
        return "Sobrepeso"
    elif 30.0 <= imc < 40.0:
        return "Obeso"
    else:
        return "Obesidade mórbida"


def main():
    print("=== CALCULADORA DE IMC ===")

    try:
        altura = float(input("Digite sua altura em metros (ex: 1.75): "))
        peso = float(input("Digite seu peso em kg (ex: 68.50): "))

        if altura <= 0 or peso <= 0:
            print("\nAltura e peso devem ser maiores que zero.")
            return

        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)

        print("\n==== RESULTADO ====")
        print(f"Altura: {altura:.2f} m")
        print(f"Peso: {peso:.2f} kg")
        print(f"IMC: {imc:.2f}")
        print(f"Classificação: {classificacao}")

    except ValueError:
        print("\nErro: Por favor, insira valores numéricos válidos.")


# Executar o programa
if __name__ == "__main__":
    main()