from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.nate.com/")
source = response.text
#print(source)

soup = BeautifulSoup(source, 'html.parser')
#result = soup.select("#olLiveIssueKeyword > li:nth-child(1) > a > span.txt_rank") #첫번째 
result = soup.select("#olLiveIssueKeyword > li > a > span.txt_rank") #list형식 
print(result)
print()
 
#print(result[0]) #태그포함 
#print(result[0].string)
print(result[0].text) #태그안의 내용 
print() 

for top in result:
    print(top.text)
