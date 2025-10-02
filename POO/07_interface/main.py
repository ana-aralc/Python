# importações 
import classes
import os

if __name__ == "__main__":
    # instancia objeto
    usuario = classes.PessoaFisica("", "", "", "", "", "") 
    empresa = classes.PessoaJuridica("", "", "", "", "", "") 

    while True:
        print("1 - Inserir dados do usuário")
        print("2 - Inserir dados do usuário da empresa")
        print("3 - Exibir dados do usuário e da empresa")
        print("4 - Sair do programa")
        opcao = input("Informe a opção desejada: ").strip()
        os.system("cls" if os.name == "nt" else "clear")
        match opcao:
            case "1":
                try:
                    usuario.nome = input("Informe o nome do usuário: ").title().strip()
                    usuario.cpf = input("Informe o CPF: ").strip()
                    usuario.profissao = input("Informe a prifissão: ").strip()
                    usuario.email = input("Informe o e-mail: ").strip().lower
                    usuario.endereco = input("Informe o endereço: ").strip().title().strip()
                    usuario.telefone = input("Informe o telefone: ").strip()

                    os.system("cls" if os.name == "nt" else "clear")

                    print(f"Dados de {usuario.nome} inseridos com sucesso!")
                except Exception as e:
                    print(f"Não foi possível inserir dados do usuário")
                finally:
                    continue
            case "2":
                try:
                    empresa.razao_social = input("Informe a razão social da empresa: ").strip().title()  
                    empresa.nome_fantasia = input("Informe o nome da empresa: ").strip().title()  
                    empresa.cnpj = input("Informe o cnpj da empresa: ").strip()
                    empresa.email = input("Informe o e-mail da empresa: ").strip()
                    empresa.endereco = input("Informe o endereço da empresa: ").strip()
                    empresa.telefone = input("Informe o telefone da empresa: ").strip()

                    os.system("cls" if os.name == "nt" else "clear")

                except Exception as e:
                    print(f"Não foi possível inserir dados da empresa:")
                finally:
                    continue
            case "3":
                    try:
                        print(f"{'-'*20} Dados do usuário {'-'*20}\n")
                        usuario.exibir_dados()
                        print(f"{'-'*20} Dados da empresa {'-'*20}\n")
                        empresa.exibir_dados()
                        
                    except Exception as e:
                        print(f"Não foi possível exibir dados da empresa:")
                    finally:
                        continue
            case "4":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                continue

    # usuario.nome = "Alex"
    # usuario.email = "alex@gmail.com"
    # usuario.profissao = "Programador"
    # usuario.exibir_dados()