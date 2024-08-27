from bs4 import BeautifulSoup

# 1 - Importando página HTML
with open('pages/index.html', 'r', encoding='utf-8') as file_html:
    content = file_html.read()
    # print(content)
    soup = BeautifulSoup(content, 'lxml')
    print(soup.prettify())
    
# 2 - Recuperar Títulos das vagas
vagas = soup.find('h5')
# print(vagas)
cursos = soup.find_all('h5')
# print(cursos)
for curso in cursos:
    print(curso.text)