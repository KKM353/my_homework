from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request

path = "C:/SOO/PyAdvanced/day06_crawling/자료실/chromedriver.exe"
driver = webdriver.Chrome(path)

url = "https://www.google.co.kr/imghp?hl=ko&ogbl"
driver.get(url)
el_search = driver.find_element("name", "q")
el_search.send_keys("아이유")
el_search.send_keys(Keys.RETURN) #Keys.ENTER 차이는 ? 결과는 같은 것 같음

el_imgs = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
#print(el_imgs)
el_img0 = el_imgs[0]
el_img0.click()

import time
time.sleep(3) #3초동안 진행 멈춤

el_img0_big = driver.find_element(By.CSS_SELECTOR, ".n3VNCb.KAlRDb")
el_img0_url = el_img0_big.get_attribute("src")
#print(el_img0_url)

import os
if not os.path.exists("download"): #디렉토리 생성
    os.makedirs("download")
    
urllib.request.urlretrieve(el_img0_url, "download/test.png") #이미지 다운로드 

driver.close()