# classe
class Pessoa:
    # atributos
    nome = "Alex machado"
    idade = 40
    email = "alex@gmail.com"
    profissao = "programador"

# algoritmo principal
if __name__ == "__main__":
    # instanciar a classe Pessoa (cria objeto da classe)
    usuario = Pessoa()
    
    #  exibe na tela dados do usuário
    print(f"Nome: {usuario.nome}.")
    print(f"Idade: {usuario.idade}.")
    print(f"Email: {usuario.email}.")
    print(f"Profissão: {usuario.profissao}.")