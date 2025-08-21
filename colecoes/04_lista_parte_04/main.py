# lista de cidades
cidades = [
    "Brasília", 
    "Rio de Janeiro", 
    "Goiânia", 
    "São Paulo", 
    "Palmas",
    "São Luis",
    "Belém",
    "Fortaleza",
    "Salvador",
    "Cuiabá",
    "Porto Alegre",
    "Belo Horizonte",
    "Maceió",
    "Brasília", 
    "Goiânia", 
    "Porto Alegre",
    "Belo Horizonte",
    "Maceió",
]

# usuário faz a pesquisa 
pesquisa = input("Informe o nome da cidade a ser pesquisada: ").title().strip()

# if pesquisa in cidades:
#     print(f"{pesquisa} encontrado.")
# else:
#     print(f"{pesquisa} não encontrado.")

# infroma quantas vezes a cidade foi citada na lista
quantidade = cidades.count(pesquisa)
print(f"{pesquisa} foi encontrado {quantidade} vezes na lista!")
