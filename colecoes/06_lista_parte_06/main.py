# importando bibliotecas
import os
# lista
nomes = [
    "Fulano", 
    "Cicrano",
    "Beltrano",
    "João", 
    "Maria",
    "Alex",
    "Fernanda",
    "Alexa",
    "Alexandra",
    "Joana"
]
# Deletando um item específico
# del(nomes[4])

# #  exibe a nova lista
# for nome in nomes:
#     print(nome)

# exibe a lista original
for i in range(len(nomes)):
    print(f"Índice {i}: {nomes[i]}.")

# usuário informa a posição da lista que deseja excluir
try:
    i = int (input("Informe o índice que deseja excluir: "))
    os.system("cls")
    if i >= 0 and i < len(nomes):
        print(f"Item a ser excluído: {nomes[i]}")
        confirma = input(f"Deseja excluir {nomes[1]}? (s/n)").lower().strip()
        os.system("cls")
        match confirma:
            case "s":
                item_excluido = nomes[i]
                del(nomes[i])
                print(f"Item {item_excluido} excluído com sucesso")
            case "n":
                print(f"{nomes[i]} não será excluído ")
            case _:
                print("Opção inválida")
    else:
        print("Índice inválido")

except Exception as e:
    print(f"Não foi possíverl excluir o item. {e}")

finally:
    print(f"Nova lista:\n")
    for i in range(len(nomes)):
        print(f"Índice {i}: {nomes[i]}.")