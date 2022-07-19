from bs4 import BeautifulSoup
import requests

url = "https://finance.naver.com/item/sise_day.nhn?code=068270&page=1"
response = requests.get(url, headers={'User-agent':'Mozilla/5.0'})
source = response.text
#print(source)

#(0) 맛보기: 오늘의 종가 가져와 보기 
soup = BeautifulSoup(source, 'lxml') #body > table.type2 > tbody > tr:nth-child(3) > td:nth-child(2) > span.tah p11
span_today = soup.find('span', class_="tah p11")
#print(span_today) #<span class="tah p11">183,500</span>
#print(span_today.text) #183,500

#(1) 마지막 페이지 가져오기
td_pgRR = soup.find("td", class_="pgRR")#body > table.Nnavi > tbody > tr > td.pgRR > a
#print(td_pgRR) #td를 포함한 전체 내용
#print(td_pgRR.text) #맨뒤
a_href = td_pgRR.a['href']
#print(a_href) #/item/sise_day.nhn?code=068270&page=421
a_href_split_list = a_href.split("=")
#print(a_href_split_list) #['/item/sise_day.nhn?code', '068270&page', '421']
last_page = a_href_split_list[-1]
#print(last_page) #421

#(2) 전체페이지 읽어오기 
import pandas as pd
df = pd.DataFrame()
base_url = "https://finance.naver.com/item/sise_day.nhn?code=068270"
for page in range(1, int(last_page)+1): #for page in range(1, 10): #10페이지까지만 가져옴
    url = "{}&page={}".format(base_url, page)
    response = requests.get(url, headers={'User-agent':'Mozilla/5.0'})
    source = response.text
    html = pd.read_html(source, header=0)[0]
    #print(html)
    df = pd.concat([df, html])
#print(df.to_string())

#(3) DataFrame 가공
df = df.dropna()    
#print(df.to_string())
df = df.iloc[0:3000] # 0행 n까지의 row만을 가져옴
#print(df.to_string())
df = df.sort_values(by='날짜')  #날짜의 오름차순
print(df.to_string())

#(4) 차트 그리기
import matplotlib.pyplot as plt
plt.title("Celltrion Close")
plt.xticks(rotation=45)
plt.plot(df['날짜'], df['종가'], 'ro-')
plt.grid(color='gray', linestyle="--")
plt.show()
    