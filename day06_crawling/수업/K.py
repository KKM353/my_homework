from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request
import time

path = "C:/SOO/PyAdvanced/day06_crawling/자료실/chromedriver.exe"
driver = webdriver.Chrome(path)

url = "https://www.google.co.kr/imghp?hl=ko&ogbl"
driver.get(url)
el_search = driver.find_element("name", "q")
el_search.send_keys("아이유")
el_search.send_keys(Keys.RETURN) 

#스크롤 내리는 코드 추가
SCROLL_PAUSE_TIME = 1
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click() #결과 더보기 버튼 
        except:
            break
    last_height = new_height
    
        
el_imgs = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")


import os
def createDirectory(dir):
    try:
        if not os.path.exists(dir): #디렉토리 생성
            os.makedirs(dir)
    except OSError:
        print("{} 디렉토리 생성 실패".format(dir))
createDirectory("downloads")

count = 1
for el_img in el_imgs:
    try:
        el_img.click()
        time.sleep(2)
        #el_img_big = driver.find_element(By.CSS_SELECTOR, ".n3VNCb.KAlRDb") #이전 방법 
        el_img_big = driver.find_element(By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img")
        el_img_url = el_img_big.get_attribute("src")
        
        # 추가 로직 
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        
        urllib.request.urlretrieve(el_img_url, "downloads/"+str(count)+".jpg")
        count = count + 1
    except: #다운로드가 안되는 경우는 패스
        pass

driver.close()

#결과: 총45개를 초과해서 다운로드 됨