result = ""
def escolha():
    while True:
        print("-"*50)
        AB = input(f"Escreva A ou B para escolher. \n A) Celsius para fahrenheit. \n B) Fahrenheit para celsius. \n Escolha: ")
        while True:
            try:
                result = float(input("Insira o valor a ser transformado (Apenas números): "))
                break
            except:
                print("Apenas números seu animal.")
        if AB.upper() == "A":
            A(result)
            break
        elif AB.upper() == "B":
            B(result)
            break
        else:
            print("Escolha inválida! Tente novamente.")


def A(result):
    result = result*1.8+32
    print(f"O valor de celsius em fahrenheit é: {result}F°")
    recomecar()



def B(result):
    result = (result-32)/1.8
    print(f"O valor de fahrenheit em celsius é: {result}C°")
    recomecar()


def recomecar():
    while True:
        i = input("Deseja fazer outra conta? (S/N)")
        if i.upper() == "S":
            break
        elif i.upper() == "N":
            exit()
        else:
            print("Escolha inválida! Tente novamente.")

escolha()
