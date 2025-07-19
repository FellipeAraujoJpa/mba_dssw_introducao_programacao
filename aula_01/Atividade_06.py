import math

def calcular_tinta_para_cilindro(raio, altura):
    area = 2 * math.pi * raio * (raio + altura)
    litros_necessarios = area / 3
    latas_necessarias = math.ceil(litros_necessarios / 5)
    custo_total = latas_necessarias * 50

    return area, litros_necessarios, latas_necessarias, custo_total


def main():
    print("Calculadora de tinta para tanque cilíndrico")

    try:
        raio = float(input("Digite o raio do tanque (em metros): "))
        altura = float(input("Digite a altura do tanque (em metros): "))

        if raio <= 0 or altura <= 0:
            print("Erro: Raio e altura devem ser maiores que zero.")
            return

        area, litros, latas, custo = calcular_tinta_para_cilindro(raio, altura)

        print("\n=== RESULTADO ===")
        print(f"Área total a ser pintada: {area:.2f} m²")
        print(f"Litros de tinta necessários: {litros:.2f} L")
        print(f"Latas de tinta necessárias: {latas}")
        print(f"Custo total: R$ {custo:.2f}")

    except ValueError:
        print("Erro: Por favor, insira apenas números válidos.")

# Executar o programa
if __name__ == "__main__":
    main()