# TODO - atividade
# importa biblioteca
import os

# lista
nomes = []

# exibe a lista original
for i in range(len(nomes)):
    print(f"Índice {i}: {nomes[i]}.")

while True:
    print(f"{'-'*30} MENU {'-'*30}")
    print("1 - Inserir novo nome na lista")
    print("2 - Exibir lista")
    print("3 - Pesquisar nome na lista")
    print("4 - Alterar item da lista")
    print("5 - Excluir item da lista")
    print("6 - Sair do programa")

    opcao = input("Opção desejada: ").strip()

    os.system("cls")
    match opcao:
        case "1":
            novo_nome = input("Informe o nome a ser cadastrado: ").strip().title()
            os.system("cls")
            try:
                nomes.append(novo_nome) # type: ignore
                print(f"{novo_nome} inserido com sucesso.")
            except Exception as e:
                print(f"Não foi possível inserir nome na lista. {e}.")
            finally:
                continue
        case "2":
            print("\nLista:\n")
            try:
                for nome in nomes: # type: ignore
                    print(nome) # type: ignore
                print("\n")
            except Exception as e:
                print(f"Não foi possível exibir a lista. {e}.")
            finally:
                continue
        case "3":
            nome_pesquisado = input("Informe o nome a pesquisar: ").title().strip()
            os.system("cls")
            result = nomes.count(nome_pesquisado) # type: ignore
            print(f"{nome_pesquisado} foi encontrado {result} vezes.")
            continue
        case "4":
            try:
                i = int(input("Informe o índice que deseja alterar:"))
                if i >= 0 and i < len(nomes): #type ignore
                    nomes[i] = input("Informe o novo nome:")
                    print("Nome alterado com sucesso.")
                else:
                    print("Índice inválido.")
            except Exception as e:
                print(f"Não foi possível alterar item da lista. {e}.")
            finally:
                continue

        case "5":    
            try:
                i = int(input("Informe o índice que deseja excluir: "))
                if i >= 0 and i < len(nomes): #type ignore
                    del(nomes [i])
                    print("Nome excluído com sucesso")
                else:
                    print("Índice inválido.")
            except Exception as e:
                print(f"Não foi possível alterar item da lista. {e}.")
            finally:
                continue
        case "6":
            print("Programa encerrado! =D")
            break 
        case _:
            print("Opção inválida.")
            continue




        # except Exception as e:
        # print(f"Não foi possíverl excluir o item. {e}")

        # finally:
        # print(f"Nova lista:\n")
        # for i in range(len(nomes)):
        #   print(f"Índice {i}: {nomes[i]}.")

        # SAIR DO PROGRAMA
        
        # case "6":
        #     print("Programa encerrado! ;) ")
        #     break
        # case _:
        #     print("Opção inválida.")
        #     continue
"""Crie um programa em que o usuário pode escolher entre:
- Inserir um nome em uma lista ✔
- Exibir a lista de nomes ✔
- Pesquisar por um nome na lista  ✔
- Alterar item da lista 
- Excluir item da lista
- Sair do programa V
"""
# NOTE - a lista deve começar vazia.
# NOTE - todos os itens devem ser inseridos pelo usuário


