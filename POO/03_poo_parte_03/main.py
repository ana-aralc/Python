# classe
class Pessoa:
    # método construtor
    def __init__(self, nome, idade, email, profissao):
        # atributos
        self.nome = nome
        self.idade = idade
        self.email = email
        self.profissao = profissao

    # método de ação
    def apresentar (self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos, trabalho com {self.profissao} e meu e-mail é {self.email}.")

# algoritmo princcipal
if __name__ == "__main__":
    # instancia a classe
    usuario  = Pessoa("", 0, "", "")

    try:
        # seta valores aos atributos do objeto
        usuario.nome = input("Informe o nome do usuário: ").title().strip()
        usuario.idade = int(input("Informe a idade: "))
        usuario.email = input("Informe o e-mail: ").lower().strip()
        usuario.profissao = input("Informe o sua profissão: ").strip()

        # executar o método
        usuario.apresentar()
    except Exception as e:
        print(f"Não foi possível executar o programa. {e}.")
        