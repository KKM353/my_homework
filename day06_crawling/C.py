from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.nate.com/")
source =  response.text

soup = BeautifulSoup(source, 'html.parser')
#result = soup.select('#olLiveIssueKeyword > li:nth-child(1) > a > span.txt_rank') #첫번째
result = soup.select('#olLiveIssueKeyword > li > a > span.txt_rank') #list 형식으로 전체 출력
print(result)
print()
#print(result[0]) 태그 포함
#print(result[0].string) #태그의 내용만
print(result[0].text) #태그의 내용만
print()

for top in result:
    print(top.text)