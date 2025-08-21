#  Tuplas
estados = (
    "Distrito Federal",
    "Goiás",
    "Minas Gerais",
    "Tocantins",
    "Rio de Janeiro",
    "Ceará"
)

# Listar a tupla
for estado in estados:
    print(estado)

# pesquisando estados
estado_pesquisa = input("Informe um estado qu e deseja pesquisar: ").title().strip()
qtde_estados = estados.count(estado_pesquisa)

print(f"{estado_pesquisa} foi encontrado {qtde_estados} vezes na tuplas.")

# tentado organizar a tupla em ordem alfabética
try:
    estados.sort()
    for estado in estados:
      print(estado)
except Exception as e:
    print(f"Não foi possível ordenar a tupla. {e}.")
