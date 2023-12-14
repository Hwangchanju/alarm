import requests
from bs4 import BeautifulSoup

# 서버에 대화 시도
response = requests.get("http://www.naver.com")

# 서버에서 html 을 줌
html = response.text

# html 번역 
soup = BeautifulSoup(html, 'html.parser')

# id 값 NM_set_home_btn 한개를 찾아냄
word = soup.select_one('#NM_set_home_btn')

# 텍스트 요소만 출력
print(word.text)