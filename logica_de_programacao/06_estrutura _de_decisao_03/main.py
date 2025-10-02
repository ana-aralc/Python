'''
Crie um programa que receba o nome e a média final de um aluno e o programa 
retorne se o aluno foi aprovado, se ficou de recuperação ou se foi reprovado
 com base em sua média finsl                        
'''                                 
#NOTE - a média deverá ser entre 0 a 10.
#NOTE - me´dia para aprovação = 7. Recuperção = 5.

# DECLARAÇÃO DE VARIÁVEIS 
nome = input("Informe o nome do aluno:")
media = float(input("Informe a média do aluno:").replace(",", "."))

# VERIFICA A MÉDIA ESTÁ DENTRO DO INTERVALO
if media >= 0 and media <= 10:
    if media >= 7:
        print(f"{nome} está aprovado.")
    elif media >= 5:
         print(f"{nome} está de recuperação.")
    else:
         print(f"{nome} está reprovado.")
else:
    print("Valor da média inválida.")
