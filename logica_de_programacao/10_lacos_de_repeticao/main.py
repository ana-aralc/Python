# Tratamento de exceção
try: 
    # Declaração de variáveis
    n = int(input("Informe um número positivo:"))

    # laço de repetição
    while n >= 0:
        print(n)
        n -= 1
except Exception as e:
        print(f"Não foi possível fazer a contagem. {e}.") 
finally:
     print("Programa encerrado")        