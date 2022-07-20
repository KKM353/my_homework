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
        time.sleep(3)
        el_img_big = driver.find_element(By.CSS_SELECTOR, ".n3VNCb.KAlRDb")
        el_img_url = el_img_big.get_attribute("src")
        urllib.request.urlretrieve(el_img_url, "downloads/"+str(count)+".jpg")
        count = count + 1
    except: #다운로드가 안되는 경우는 패스
        pass

driver.close()

#결과: 총45개 이미지 다운로드 됨