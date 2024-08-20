import requests

# 1 - Autenticção GitHub

acess_token = ' ' #Token gerado pelo GIthHub
headers = {
    'Authorization': 'Bearer' +acess_token,
    'X-GitHub-Api-Version': '2022-11-28'
}