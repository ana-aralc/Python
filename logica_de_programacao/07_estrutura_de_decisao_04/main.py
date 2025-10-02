"""
Programa receberá do usuário dois números reais e o usuário irá escolher uma das quatros
operações básicas de matemática e o programa irá calcular com base na escolha do usuário e 
informar o resultado.
"""
#TODO
# DECLARAÇÃO DE VARIÁVEIS
x = float(input("Infrome o valor de x: ").replace(",","."))
y = float(input("Infrome o valor de y: ").replace(",","."))

# menu
print(f"{'-'*20} Calculadora Python {'-'*20}")
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



        






