import requests # > pip install requests
import pymysql  # > pip install pymysql

def banco(sql):
    conexao = pymysql.connect(
        host='localhost',
        database='espetaria',
        user='root',
        password='senai@123'
    )
    cursor = conexao.cursor()
    cursor.execute(sql)
    conexao.commit()
    cursor.close()
    conexao.close()

# Endereço de onde vamos pegar os dados
url = 'https://api.anota.ai/clientauth/nm-category/menu-merchant?displaySources=DIGITAL_MENU'
# token de autorização
headers = {
    'Authorization':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZHBhZ2UiOiI2NGY4ZTUwZGRlYTRkNDAwMTI2OTlmMzMiLCJpYXQiOjE3NDk2ODMzMzN9.7pbJIsjpZTzbHqVzEhY3ri5sLqVwDIYta3LVkyxApqI'
}
# executa a requisição como se fosse um navegador
response = requests.get(url,headers=headers)
#print(response.json()) # vai mostrar o retorno da requisição
obj = response.json()
lista = obj['data']['menu']['menu'][1]['itens']
i = 0
while i < len(lista):
    nome = lista[i]['title']
    descricao = lista[i]['description']
    preco = lista[i]['price']
    i = i + 1
    banco(f"INSERT INTO produto (nome, descricao, preco) VALUES ('{nome}', '{descricao}', {preco})")

# print('Olá Mundo')