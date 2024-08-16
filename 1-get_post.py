import requests

# API Jsonplaceholder
url = 'https://jsonplaceholder.typicode.com/posts/5'

# 2 - Requisição GET

response = requests.get(url)
print(response)
print(response.status_code)

# 3 - Exempolo de tratamento
if response.status_code == 200:
    print('Código de Sucesso foi retornado')
else:
    print('A requisição não foi processada corretamente')
    
# 4 - Pegar os dados
response_json = response.json()
print(response_json)
