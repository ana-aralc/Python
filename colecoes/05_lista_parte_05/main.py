#  importa bibliotecas
import os

# lista
frutas = [
    "Morango",
    "Banana",
    "Maçã",
    "Pêra",
    "Uva",
    "Maracujá",
    "Abacaxi",
    "Laranja",
    "Pêssego"
]

# mudando o valor de pêra para mamão
# frutas[3] = "Mamão"

# #  exibe a lista
# for fruta in frutas:
#     print(fruta)

# usuário informa qual fruta ele quer mudar

#  exibe a lista com seus respectivos índices
for i in range(len(frutas)):
    print(f"Índice {i}: {frutas [i]}.")

# usuário informa o índice que deseja alterar
try:
    i = int(input("Informe o número do ídice a ser alterado: "))
    os.system("cls")
    if i >= 0 and i < len(frutas):
        print(f"Valor encontrado: {frutas[i]}.")
        frutas[i] = input(f"Informe o nome da fruta: ")
        print("Fruta alterada com sucesso")
        os.system("cls")
    else:
        print("Valor do ídice inválido.")
except Exception as e:
    print(f"Não foi possível alterar a operação {e}.")
finally: 
    print("\nNova lista:\n")
    for i in range(len(frutas)):
        print(f"Índice {i}: {frutas [i]}.")