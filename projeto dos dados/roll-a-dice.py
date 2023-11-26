import random

response = "y"

while response == "y":
    print("Jogando o dado...")
    no = random.randint(1, 6)

    if no == 1:
        print("-----")
        print("|   |")
        print("| o |")
        print("|   |")
        print("-----")
    elif no == 2:
        print("-----")
        print("|o  |")
        print("|   |")
        print("|  o|")
        print("-----")
    elif no == 3:
        print("-----")
        print("|o  |")
        print("| o |")
        print("|  o|")
        print("-----")
    elif no == 4:
        print("-----")
        print("|o o|")
        print("|   |")
        print("|o o|")
        print("-----")
    elif no == 5:
        print("-----")
        print("|o o|")
        print("| o |")
        print("|o o|")
        print("-----")
    else:  # no == 6
        print("-----")
        print("|o o|")
        print("|o o|")
        print("|o o|")
        print("-----")

    response = input("Deseja jogar o dado novamente? (y/n): ")

    while response.lower() not in ['y', 'n']:
        response = input("Por favor, digite 'y' para continuar ou 'n' para sair: ")

print("Fim do jogo!")