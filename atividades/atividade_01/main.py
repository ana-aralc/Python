"""Crie um programa que receba do usuário dois números reais, e uma das
4 operações da matemática informada pelo usuário e faça o cálculo correspondente.
"""
#NOTE - O programa só encerrará caso o usuário informe isso.
#TODO 

#Números 
x = int(input("Infrome o valor de x: "))
y = int(input("Infrome o valor de y: "))

# menu
print(f" Calculadora Python")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão\n")

operador = input("Informe a opção desejada")



#verifica a operação escolhida e faz o cálculo
match operador:
    case "1":
        print(f"O resultado da soma é: {x+y}.")
    case "2":    
        print(f"O resultado da Subtração é: {x-y}.")
    case "3":     
        print(f"O resultado da Multiplicação é: {x*y}.")
    case "2":     
        print(f"O resultado da Divisão é: {x/y}.")
    case _:
         print("Operador inválido.")

