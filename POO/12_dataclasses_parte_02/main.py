from classes import PessoaFisica, PessoaJuridica
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    usuario = PessoaFisica(
        nome="", 
        cpf="", 
        profissao="",
        email="",
        telefone="",
        endereco=""
        )
    
    empresa = PessoaJuridica(
        nome_fantasia="", 
        razao_social="", 
        cnpj="",
        email="",
        telefone="",
        endereco=""
        )

    print("Informe os dados do usuário:\n")

    usuario.nome = input("Informe o nome do usuário: ").strip().title()
    usuario.cpf = input("Informe o cpf do usuário: ").strip()
    usuario.profissao = input("Informe a profissão do usuário: ").strip()
    usuario.email = input("Informe o e-mail do usuário: ").strip().lower()
    usuario.telefone = input("Informe o telefone do usuário: ").strip()
    usuario.endereco = input("Informe o endereço do usuário: ").strip().title()

    print("Informe os dados da empresa:\n")

    usuario.razao_social = input("Informe a razão social da empresa: ").strip().title()
    usuario.nome_fantasia = input("Informe o nome da empresa: ").strip()
    usuario.cnpj = input("Informe o CNPJ: ").strip()
    usuario.email = input("Informe o e-mail da empresa: ").strip().lower()
    usuario.telefone = input("Informe o telefone da empresa: ").strip()
    usuario.endereco = input("Informe o endereço da empresa: ").strip().title()
    
    # limpa a tela
    limpar() 

    # saída de dados
    print(usuario)
    print(empresa)