from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = "C:/Users/Kosmo/Desktop/KKM/pyadvanced/day06_crawling/자료실/chromedriver.exe"
driver = webdriver.Chrome(path)

url = 'https://ko-kr.facebook.com/'
driver.get(url)


usr = "01094330681"
pwd = "비밀번호"
el_email = driver.find_element("id","email") # key , value
el_email.send_keys(usr)
el_pass = driver.find_element("id","pass") # key , value
el_pass.send_keys(pwd)
el_pass.send_keys(Keys.ENTER)