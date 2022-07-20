from selenium import webdriver

path = "C:/SOO/PyAdvanced/day06_crawling/자료실/chromedriver.exe"
driver = webdriver.Chrome(path)

url = "http://google.com"
driver.get(url)
search_box = driver.find_element("name", "q") #다른예 driver.find_element(By.XPATH, " ")
search_box.send_keys("테슬라")
search_box.submit()