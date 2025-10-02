# bibliotecas
import os

# lista
usuarios = []

# loop
while True:
    print(f"{'-'*30} MENU {'-'*30}")
    print("1 - Inserir dados do novo usuário")
    print("2 - Exibir lista de usuário")
    print("3 - Alterar dados de um usuário já cadastrado")
    print("4 - Excluir usuário da lista")
    print("5 - Sair do programa")

    opcao = input("Opção desejada: ").strip()

# cls só funciona no cmd do windows, caso use otr so
    os.system("cls" if os.name=="nt" else clear)
    match opcao:
        case "1":
            # inicializa o dicionário
            usuario = {}
            # input do usuário
            usuario['nome'] = input("Informe o nome: ").title().strip()
            usuario['data de nascimento'] = input("Informe ao data de nascimento: ").strip()
            usuario['email'] = input("Informe o e-mail: ").strip()
            usuario['cpf'] = input("Informe o cpf: ").strip()
            usuario['telefone'] = input("Informe o telefone: ").strip()
            usuario['profissão'] = input("Informe a profissão: ").strip()
            usuario['genero'] = input("Informe o genero: ").strip()

            os.system("cls" if os.name=="nt" else clear)
            try:
                # inserir os dados do dicionário na lista
                usuarios.append(usuario) # type: ignore
                print("Usuário cadastrado com sucesso.")
            except Exception as e:
                print(f"Não foi possível inserir novo usuário. {e}.")
            finally:
                continue    
        case "2":
            print("\nLista de usuários")
            for i in range (len(usuarios)): # type: ignore
                print(f"{'-'*40}\n")
                print(f"Índice: {i}.")
                for chave in usuarios[i]: # type: ignore
                    print(f"{chave.capitalize()}: {usuarios[i].get(chave)}.")
            continue

        case "3":
            try:
                i = int(input("Informe o índice desejado: "))
                if i >= 0 and i < len(usuarios):
                    for chave in usuarios[i]:
                        print(f"{chave.capitalize()}: {usuarios[i].get(chave)}")
                    chave_escolhida = input("Informe a chave que deseja alterar: ").lower().strip()
                    usuarios[i][chave_escolhida] = input("Informe o novo valor: ").strip()
                    os.system("cls" if os.name=="nt" else clear)
                    print("Chave alterada com sucesso.")
                else:
                    print("Índice inválido.")
            except Exception as e:
                print(f"Não foi possível inserir novo usuário. {e}.")
            finally:
                continue    
        case "4":
            try:
                i = int(input("Informe o índice: "))
                if i >= 0 and 1 < len(usuarios):
                    for chave in usuarios[i]:
                        print(f"{chave.capitalize()}: {usuarios[i].get(chave)}") 
                        confirma = input("Tem certeza que deseja excluir este usuário? (s/n)").lower().strip()  
                        match confirma:
                            case "s":
                                del(usuarios[i]) 
                                print("Usuário deletado com sucesso.")
                                os.system("cls" if os.name=="nt" else clear)
                            case "n":
                                os.system("cls" if os.name=="nt" else clear)
                                print("Operação cancelada")
                            case _:
                                os.system("cls" if os.name=="nt" else clear)
                                print("Opção inválida. Operação cancelada")
                else:
                    print("Índice inválido")
            except Exception as e:
                print(f"Não foi possível inserir novo usuário. {e}.")
            finally:
                continue    
        case "5":   
            print("Programa encerrado! ;) ")
            break 
        case _: 
            print("Opção inválida.")
            continue  



            """
#TODO - atividade: Crie um programa que faça as seguintes operações:
- Inserir dados de novo usuário - OK
- Exibir lista de usuários - OK
- Alterar dados de um usuário já cadastrado -
- Excluir usuário da lista -
- Sair do programa -
Os dados a serem cadastrados serão os seguintes:
- Nome
- Data de nascimento
- E-mail
- CPF
-Telefone
- Profissão
- Genero
#NOTE - a lista deve começar vazia
"""