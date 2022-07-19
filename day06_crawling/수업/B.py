import requests

url = "http://naver.com/"
response = requests.get(url)
print(response.text)