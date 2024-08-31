from bs4 import BeautifulSoup
import requests

# 1 - Coletando vagas em Python
response = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=Python&txtLocation=')
print(response.status_code)
# print(response.text)
soup = BeautifulSoup(response.text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
print(len(jobs))
print(jobs[:3])