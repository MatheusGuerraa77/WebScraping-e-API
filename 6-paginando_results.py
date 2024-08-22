import requests
from collections import Counter
import pandas

# 1 - Autenticção GitHub

acess_token = ' ' #Token gerado pelo GIthHub
headers = {
    'Authorization': 'Bearer ' +acess_token,
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

# 5 - pegando o Nome de cada repositório
name_repos = []
for page in repo_list:
    for repo in page:
        # print(repo['name'])
        name_repos.append(repo['name'])
print(len(name_repos))
print(name_repos[:10])

# 6 - Pegando a linguagem de cada repositório
lang_repos = []
for page in repo_list:
    for repo in page:
        # print(repo['language'])
        lang_repos.append(repo['language'])
print(len(lang_repos))
print(lang_repos[:10])

# 7 - Contando as ocorrências das linguagens
print(Counter(lang_repos))

# 8 - Criando Dataframe
dados_mt = pandas.DataFrame()
dados_mt['repo_name'] = name_repos
dados_mt['repo_lang'] = lang_repos
print(dados_mt)

# 9 - Exportando para CSV
dados_mt.to_csv('mt.csv')

