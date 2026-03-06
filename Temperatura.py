def escolha():
    print("-"*50)
    AB = input(f"Escreva A ou B para escolher. \n A) Celsius para fahrenheit. \n B) Fahrenheit para celsius. \n Escolha: ")
    if AB.upper() == "A":
        A()
    elif AB.upper() == "B":
        B()
    else:
        print("Escolha inválida! Tente novamente.")
        escolha()


def A():
    try:
        result = float(input("Insira o valor a ser transformado (Apenas números): "))
    except:
        print("Apenas números seu animal.")
        A()
    result = result*1.8+32
    print(f"O valor de celsius em fahrenheit é: {result}F°")
    recomecar()



def B():
    try:
        result = float(input("Insira o valor a ser transformado (Apenas números): "))
    except:
        print("Apenas números seu animal.")
        B()
    result = (result-32)/1.8
    print(f"O valor de fahrenheit em celsius é: {result}C°")
    recomecar()


def recomecar():
    i = input("Deseja fazer outra conta? (S/N)")
    if i.upper() == "S":
        escolha()
    elif i.upper() == "N":
        exit()
    else:
        print("Escolha inválida! Tente novamente.")
        recomecar()


escolha()

