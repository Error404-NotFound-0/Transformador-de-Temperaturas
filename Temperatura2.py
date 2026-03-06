def converter():
    while True:
        print("-" * 50)
        escolha = input("A) Celsius para Fahrenheit\nB) Fahrenheit para Celsius\nEscolha (ou 'Q' para sair): ").upper()

        if escolha == 'Q':
            break
        
        if escolha.upper not in ['A', 'B']:
            print("Escolha inválida!")
            continue

        try:
            valor = float(input("Insira o valor: "))
            if escolha == 'A':
                resultado = (valor * 1.8) + 32
                print(f"{valor}°C é igual a {resultado:.2f}°F")
            else:
                resultado = (valor - 32) / 1.8
                print(f"{valor}°F é igual a {resultado:.2f}°C")
        except ValueError:
            print("Por favor, digite apenas números válidos.")

converter()
