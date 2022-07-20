from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://finance.naver.com/news/mainnews.naver')

bsObject = BeautifulSoup(html, 'html.parser')

for link in bsObject.find_all('dd', {'class':'articleSubject'}):
    print(link.text.strip(), link.get('a'))
