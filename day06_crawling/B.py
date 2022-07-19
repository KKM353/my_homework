from urllib import response
import requests

url = "http://naver.com/index.html" # index.html 숨겨져있음
response = requests.get(url)
print(response.text)