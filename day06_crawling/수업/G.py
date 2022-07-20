from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = "C:/SOO/PyAdvanced/day06_crawling/자료실/chromedriver.exe"
driver = webdriver.Chrome(path)

url = "https://ko-kr.facebook.com/"
driver.get(url)

usr = "khsoo1128@nate.com"
pwd = "비밀번호"
el_email = driver.find_element("id", "email")
el_email.send_keys(usr)
el_pass = driver.find_element("id", "pass")
el_pass.send_keys(pwd)
el_pass.send_keys(Keys.ENTER) #바로 꺼진다면.. chromedriver.exe버젼과 크롬버젼이 맞지 않는 거임 


