def main():
    temperatura = input("Qual medida de temperatura é utilizada em sua região?: ").strip().lower()

    try:
        if temperatura == "celsius":
            celsius = float(input("Qual a temperatura? "))
            fahrenheit = (celsius * 9 / 5) + 32
            print(f"{celsius}ºC é referente a {fahrenheit:.2f}ºF")

        elif temperatura == "fahrenheit":
            fahrenheit =  float(input("Qual a temperatura? "))
            celsius = (fahrenheit - 32) * 5 / 9
            print(f"{fahrenheit}ºF é referente a {celsius: .2f}ºc")
        else:
            print("Unidade de temperatura não reconhecida. Use 'celsius' ou 'fahrenheit'.")
    except ValueError:
        print("Erro: Por favor, insira um valor numérico válido.")
if __name__ == "__main__":
    main()