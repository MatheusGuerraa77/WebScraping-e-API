import requests

# API Jsonplaceholder
url = 'https://jsonplaceholder.typicode.com/posts/'

# 2 - Adicionando um payLoad
payload = {
    'id':[1, 2, 3, 4, 5, 7, 9, 10],
    'userId':1
}

# 3 - Realizando requisição
response = requests.get(url, params=payload)

print(response)
print(response.json())

# 4 - Melhorar a Legibilidade
response_json = response.json()
for i in response_json:
    print(i, '\n')