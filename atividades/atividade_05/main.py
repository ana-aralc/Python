'''
# TODO - atividade Crie um programa que receba os seguintes dados:
- Nome
- CPF
- Data de nascimento
- Email 
- genero 
- telefone
- endereço
- altura em metros
- peso em kg
- tipo sanguineo
Ao final, o programa exibe esses dados
#NOTE - deve ser feito utilizando o conceito de dicionario.
'''
dados = {}

# inserindo a idade da pessoa
try:    
    dados['nome'] = (input("Informe a nome:"))
    dados['idade'] = int(input("Informe a idade:"))
    dados['cpf'] = int(input("Informe o cpf:"))
    dados['data'] = int(input("Informe sua data de nascimento:"))
    dados['email'] = (input("Informe seu e-mail:"))
    dados['genero'] = (input("Informe seu genero:"))
    dados['numero'] = int(input("Informe seu telefone:"))
    dados['altura'] = int(input("Informe sua altura:"))
    dados['peso'] = int(input("Informe seu peso:"))
    dados['sangue'] = (input("Informe seu tipo sanguíneo:"))

except Exception as e:
    print(f"Não foi possível inserir o novo valor. {e}.")
finally:    
  
    # print(f"E-mail: {dados.get('email')}")
    print(f"Nome: {dados.get('nome')}")
    print(f"Idade: {dados.get('idade')}")
    print(f"CPF: {dados.get('cpf')}")
    print(f"Data de nascimento: {dados.get('data')}")
    print(f"E-mail: {dados.get('email')}")
    print(f"Genero: {dados.get('genero')}")
    print(f"Telefone: {dados.get('numero')}")
    print(f"altura: {dados.get('altura')}")
    print(f"peso: {dados.get('peso')}")
    print(f"sangue: {dados.get('sangue')}")

