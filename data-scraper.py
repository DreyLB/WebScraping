import requests
from bs4 import BeautifulSoup

url = 'https://www.fundsexplorer.com.br/wp-json/funds/v1/get-ranking'
response = requests.get(url)
html_page = response.text
'''soup = BeautifulSoup(html_page, 'html.parser')
print(soup.prettify())'''

print(html_page)

'''with open('resumo.html', 'w+') as arquivo:
    arquivo.write(html1)
'''
