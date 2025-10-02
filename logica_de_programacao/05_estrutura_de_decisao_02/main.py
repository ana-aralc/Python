
# Crie um programa que receba o nome, a idade e a altura do usuário 
# e que verifique se o usuário tem a idade e altura mínima para 
# entrar no brinquedo. Caso não tenha, o programa deverá barrar a entrada do usuário.
 
# Variáveis
nome = input("Informe o nome do usuário: ")
idade = int(input("Informe a idade do usuário: "))
altura = float(input("Informe a altura do usuário: ").replace(",","."))

# saída de dados
if idade >= 12 and altura >= 1.10:
    print(f"A entrada de {nome} foi autorizada.")
else:
    print(f"A entrada de{nome}) foi negada.")
