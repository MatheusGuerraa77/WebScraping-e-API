import requests

# 1 - Autenticção GitHub

acess_token = ' ' #Token gerado pelo GIthHub
headers = {
    'Authorization': 'Bearer' +acess_token,
    'X-GitHub-Api-Version': '2022-11-28'
}

# 2 - Mapeando informações
base_api = 'https://api.github.com'
user = 'matheusguerraa77'
url = f'{base_api}/users/{user}/repos'

# 3 - Organizando os dados
repo_list = []
for page_num in range (1, 3):
    try:
        url_page = f'{url}?page={page_num}'
        response = requests.get(url_page, headers=headers)
        repo_list.append(response.json())
    except:
        repo_list.append(None)
        
        
# 4 - Apresentar os Dados
print(len(repo_list))
print(repo_list[0][2]['name'])