# bibliotecas
import classes
import os

# algoritmo principal
if __name__ == "__main__":
    #  instancia de objetos
    usuario = classes.PessoaFisica("", "", "", "", "", "", "")
    empresa = classes.PessoaJuridica("", "", "", "", "", "")

    # limpar tela
    os.system("cls" if os.name == "nt" else "clear")

    # atribui valores ao objeto de tipo de Pessoa Fisica 
    print(f"{'-'*20} DADOS DO USUÁRIO {'-'*20}\n")

    usuario.nome = input("Informe o seu nome: ").title().strip()
    usuario.cpf = input("Informe o seu cpf: ").strip()
    usuario.profissao = input("Informe o sua profissão: ").strip()
    usuario.genero = input("Informe o seu gênero: ").strip().lower()
    usuario.email = input("Informe o seu e-mail: ").title().strip()
    usuario.endereco = input("Informe o seu endereço: ").strip().title()
    usuario.telefone = input("Informe o seu telefone: ").title().strip()

    # limpar tela
    os.system("cls" if os.name == "nt" else "clear")

    # atribui valores ao objeto de tipo de Pessoa Jurídica 

    print(f"{'-'*20} DADOS DA EMPRESA {'-'*20}\n")

    empresa.razao_social = input("Informe a razão social da sua empresa: ").title().strip()
    empresa.nome_fantasia = input("Informe o nome fantasia: ").title().strip()
    empresa.cnpj = input("Informe o CNPJ: ").strip()
    empresa.email = input("Informe o e-mail: ").strip().lower()
    empresa.endereco = input("Informe o endereço da empresa: ").strip().title()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()

    # limpar tela
    os.system("cls" if os.name == "nt" else "clear")

    # exibe os dados do usuário e da empresa
    print("Dados do usuário:\n")
    usuario.exibir_dados()
    print("Dados da empresa:\n")
    empresa.exibir_dados()
