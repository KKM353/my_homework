from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request


path = "C:/Users/Kosmo/Desktop/KKM/pyadvanced/day06_crawling/자료실/chromedriver.exe"
driver = webdriver.Chrome(path)

url = 'https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl'
driver.get(url)
el_search = driver.find_element("name", "q")
el_search.send_keys("아이유")
el_search.send_keys(Keys.RETURN) # == el_search.submit() == el_search.send_keys(Keys.RETURN)

el_imgs = driver.find_elements(By.CSS_SELECTOR, '.rg_i.Q4LuWd') # By.CSS_SELECTOR는 찾기만 하는것 같다 
el_img0 = el_imgs[5]
el_img0.click()

import time
time.sleep(3) # 3초동안 쓰레드가 진행을 멈춤

el_img0_big = driver.find_element(By.CSS_SELECTOR,'.n3VNCb.KAlRDb' )
el_img0_url = el_img0_big.get_attribute("src")
#print(el_img0_url)

import os
if not os.path.exists("download"):
    os.makedirs("download")

urllib.request.urlretrieve(el_img0_url, "download/first.png")

driver.close()