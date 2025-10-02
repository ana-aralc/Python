import classes
import os

if __name__ == "__main__":
    # instacia a classe Filho
    filho = classes.Filho("", "", "", "", 0.0, 0.0)

    try:
        # input
        filho.nome = input("Informe o nome: ").strip().title()
        filho.email = input("Informe o e-mail: ").strip().lower()
        filho.telefone = input("Informe o telefone: ").strip()
        filho.genero = input("Informe o gênero: ").strip()
        filho.peso = float(input("Informe o peso em kg: ").replace(",", "."))
        filho.altura = float(input("Informe a altura em metros: ").replace(",", "."))


    # limpar tela
        os.system("cls" if os.name == "nt" else "clear")

        # output
        filho.exibir_info()
    except Exception as e:
        print(f"Não foi possível executar.{e}.")