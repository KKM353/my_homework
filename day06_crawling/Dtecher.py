from bs4 import BeautifulSoup
import requests

url = "https://finance.naver.com/item/sise_day.nhn?code=068270&page=1"
response = requests.get(url, headers={'User-agent':'Mozilla/5.0'})
source = response.text
#print(source)

soup = BeautifulSoup(source, 'lxml') #body > table.type2 > tbody > tr:nth-child(3) > td:nth-child(4) > span
span = soup.find('span', class_="tah p11")
print(span.text)