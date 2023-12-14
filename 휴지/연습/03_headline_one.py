import requests
from bs4 import BeautifulSoup


header = {'User-agent' : 'Mozila/2.0'}
response = requests.get("https://news.naver.com/", headers = header)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
title = soup.select_one('.lnk_hdline_article')
print(title.text.strip())