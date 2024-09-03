from bs4 import BeautifulSoup
import requests
import pandas

# 1 - Coletando vagas em Python
response = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=Python&txtLocation=')
print(response.status_code)
# print(response.text)
soup = BeautifulSoup(response.text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
# print(len(jobs))
# print(jobs[:3])

companys = []
skills = []
published_date = []

# 2 - Estruturando informações para coleta
for job in jobs:
    name_company = job.find('h3', class_='joblist-comp-name').text.strip().replace(' ', '')
    # print(name_company)
    skill = job.find('span', class_='srp-skills').text.strip().replace(' ', '')
    # print(skill)
    pub_date = job.find('span', class_='sim-posted').span.text[7:]
    print(pub_date)
    
# 3 - Exportando informações para CSV
    companys.append(name_company)
    skills.append(skill)
    published_date.append(pub_date)
    
python_jobs = pandas.DataFrame()
python_jobs['companys'] = companys
python_jobs['skills'] = skills
python_jobs['pub_date'] = published_date
print(python_jobs)
python_jobs.to_csv('python_jobs.csv')