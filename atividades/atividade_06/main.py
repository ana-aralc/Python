import os

usuario = {}
while True:
    print(f"{'-'*20} MENU {'-'*20}\n")
    print("1 - Cadastrar nova chave")
    print("2 - Exibir dados do usuário")
    print("3 - Alterar valor da chave")
    print("4 - Excluir chave")
    print("5 - Sair do programa")
    opcao = input("Informe a opção desejada: ")

    os.system("cls")
    match opcao:
        case "1":
# usuário escolhe a chave que deseja alterar
            chave = input("Informe o nome da chave que deseja alterar:").lower().strip()
            usuario[chave] = input("Informe o valor da chave: ")

            os.system("cls")
            print("Chave cadastrada com sucesso!")

            continue
        case "2":
            for chave in usuario: # type: ignore
                print(f"{chave.capitalize()}: {usuario.get(chave)}.") # type: ignore

            print("\n")
            continue
        case "3":
            chave = input("Informe a chave que deseja alterar: ").lower().strip()

            if chave in usuario:
                usuario[chave] = input("Informe o valor da chave: ")
                os.system("cls")
                print("Valor da chave alterado com sucesso!")
            else:
                os.system("cls")
                print("Chave não encontrada.")
            
            continue
        case "4":
            chave = input("Informe a chave que deseja excluir: ").lower().strip()
            if chave in usuario:
                confirmacao = input(f"Tem certeza de que deseja excluir {chave}? (s/n)").lower().strip()
                os.system("cls")
            
            if confirmacao is "s":
                del usuario[chave]
                print("Chave excluída com sucesso!")
            else:
                print("Chave não foi excluída.")
            
            continue
        case "5":
            print("Programa encerrado.")
            break
        case _:
            print("Opção inválida.")
            continue
"""
#TODO - atividade: Crie um programa com um dicionário chamado 'usuario',
com o seguinte menu:
- Cadastrar nova chave 1
- Exibir dados do usuário 2
- Alterar o valor da chave 3
- Excluir chave 4
- Sair do programa 5
#NOTE - os dados a serem inseridos precisam ter a ver com dados do usuário
"""