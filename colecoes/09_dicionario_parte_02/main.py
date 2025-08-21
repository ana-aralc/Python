#  dicionário
pessoa = {
   'nome': "Alex",
   'email': "alex@gmail.com",
   'idade': 23
}
# exibe dados
print(f"Nome: {pessoa['nome']}")
print(f"E-mail: {pessoa.get('email')}") # melhor usar ele
# print(f"idade: {pessoa.get('idade')}") # m

# exibe dados inexistentes
print(f"idade: {pessoa.get('idade')}")

# inserindo a idade da pessoa
try:
    pessoa['idade'] = int(input("Informe a idade:"))

except Exception as e:
    print(f"Não foi possível inserir o novo valor. {e}.")
finally:    
    print(f"Nome: {pessoa.get('nome')}")
    print(f"E-mail: {pessoa.get('email')}")
    print(f"Idade: {pessoa.get('idade')}")

