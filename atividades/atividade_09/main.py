# biblioteca
import random

atendente = "Claudia"
# classe
class Pessoa:
    # método construtor
    def __init__(self, nome, idade, email, telefone, genero, sangue):
        # atributos
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self.genero = genero
        self.sangue = sangue
        
    # método de ação
    def atendente_da_boas_vindas (self):
        return "Boa tarde! Me chamo Claudia, poderia informar os seus dados?"

    def cumprimentar(self):
        return f"Olá, eu me chamo {self.nome}. Vim doar sangue!"
    
    def dados(self):
        return f"Tenho {self.idade} anos, meu número é {self.telefone} e o meu é {self.email}"
    
        

# algoritmo principal
if __name__ == "__main__":
    # instancia os objetos
    usuario_1 = Pessoa("", "", "", "", bool(random.getrandbits(0)), bool(random.getrandbits(1)))
    usuario_2 = Pessoa("", "", "", "", bool(random.getrandbits(0)), bool(random.getrandbits(1)))
    # atendente = Pessoa("", "", "", "", bool(random.getrandbits(0)), bool(random.getrandbits(1)))

    # seta os valores dos atributos do objeto usuario 1
    usuario_1.nome = input("Infome seu nome: ").title().strip()
    usuario_1.idade = input("Infome seu idade: ").lower().strip()
    usuario_1.email = input("Infome seu tipo e-mail: ").strip()

    # seta os valores dos atributos do objeto usuario 2
    usuario_2.nome = input("Infome seu nome: ").title().strip()
    usuario_2.idade = input("Infome sua idade: ").lower().strip()
    usuario_2.email = input("Infome seu e-mail:  ").strip()
    
   # seta os valores dos atributos da atendente
    # atendente.nome = input("Infome seu nome: ").title().strip()
        
    # CONVERSA
    print(f"Atendente: -{(atendente.atendente_da_boas_vindas)}") 


"""
# TODO - atividade: Crie um programa que receba os dados de dois objetos diferentes da mesma classe Pessoa. Os dados serão os seguintes:
Nome
Idade 
E-mail
Telefone
Gênero
Tipo sanguíneo
Suponha que o objeto 'usuario_2' esteja precisando de doação de sangue do 'usuario_1', o programa deve informar os dados dos dois usuários e ao final informar se o suario_1 pode doar sangue para o usuario_2 ou não.
#NOTE - as duas últimas perguntas deverão ter uma resposta randômica.
"""
# TIPO SANGUINEO É RANDOM E O GENERO