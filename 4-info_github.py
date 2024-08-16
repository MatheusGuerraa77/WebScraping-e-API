import requests

# 1 - API Events Github
url = 'https://api.github.com/events'
response = requests.get(url)
print(response.status_code)
print(response.json())

# 2 - Verificar versão da API
url2 = 'https://api.github.com/versions'
response2 = requests.get(url2)
print(response2.json())

# 3 - Realizando requisição com versão específica
headers = {'X-GitHub-API-Version':'2022-11-28'}
response3 = requests.get(url, headers=headers)
print(response3.json())