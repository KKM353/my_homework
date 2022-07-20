from selenium import webdriver

path = "C:/Users/Kosmo/Desktop/KKM/pyadvanced/day06_crawling/자료실/chromedriver.exe"
driver = webdriver.Chrome(path)
url = 'http://google.com'
driver.get(url)
search_box = driver.find_element("name","q")
search_box.send_keys("블로그")
search_box.submit()
print(search_box)