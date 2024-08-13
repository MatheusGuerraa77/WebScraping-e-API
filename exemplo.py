import requests


# 1 - Versão e métodos da biblioteca
print(requests.__version__)
print(dir(requests))

# 2 - Realizando requisição GET

link = 'https://www.google.com/search?q=S%C3%A3o%20Paulo%20FC#cobssid=s'

requisicao = requests.get(link)
print(requisicao)
print(requisicao.status_code)
print(requisicao.text)