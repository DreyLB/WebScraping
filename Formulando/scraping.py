import requests
from bs4 import BeautifulSoup

url = 'https://www.fundsexplorer.com.br/funds/xplg11'
response = requests.get(url)
html_page = response.text
soup = BeautifulSoup(html_page, 'html.parser')
print(soup.prettify())

'''with open('resumo.html', 'w+') as arquivo:
    arquivo.write(html1)
'''
