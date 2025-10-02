"""
Crie um programa que receba o nome, o peso e a altura do usuário e informe seu IMC (Índice de Massa Corporal)
e informe seu diagnóstico de acordo com o valor de seu IMC:

- Magro demais
- Peso normal
- Obeso
- Obesidade nível 2
- Obesidade mórbida
"""
#NOTE 
#TODO 
# Variáveis
nome = input("Informe o nome do usuário: ")
peso = float(input("Informe a idade do usuário: "))
altura = float(input("Informe a altura do usuário: ").replace(",","."))
imc = peso/altura**2

# saída de dados

print(f"IMC de {nome} é maior ")

# if imc <= 18.5 Magreza
# if imc >= 18.5 <= 

#     print(f"A entrada de {nome} foi autorizada.")
# else:
#     print(f"A entrada de{nome}) foi negada.")


# O IMC (Índice de Massa Corporal) 
# é calculado dividindo o peso (em quilos) pela altura ao quadrado (em metros). 
# A fórmula é: IMC = peso (kg) / altura (m)². 

# Menor que 18,5	Magreza	0
# Entre 18,5 e 24,9	Normal	0
# Entre 25,0 e 29,9	Sobrepeso	I
# Entre 30,0 e 39,9	Obesidade	II
# Maior que 40,0	Obesidade Grave	III
