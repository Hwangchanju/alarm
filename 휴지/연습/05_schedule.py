import requests
from bs4 import BeautifulSoup
from datetime import date, datetime


year = str(datetime.today().year)
month = str(datetime.today().month)
day = str(datetime.today().day)
ssibal = year + '년 ' + month + '월 ' + day + '일 중앙당 일정입니다.'

today1 = '#schedule_'
today2 = datetime.today().strftime('%Y%m%d')
today3 = '.cnt'


today_text = today1 + today2 + ' ' + today3

header = {'User-agent' : 'Mozila/2.0'}

response1 = requests.get("http://www.peoplepowerparty.kr/renewal/news/schedule.do", headers = header)
response2 = requests.get("https://theminjoo.kr/schedule", headers = header)

html1 = response1.text
html2 = response2.text

soup1 = BeautifulSoup(html1, 'html.parser')
soup2 = BeautifulSoup(html2, 'html.parser')

poly_part1 = soup1.select_one('.sub-txt')
title1 = soup1.select_one('#schedule h1')
schedules1 = soup1.select('.txt-box')

schedules2 = soup2.select(today_text)

print()
print(poly_part1.text)
print(title1.text)
print()
for schedule1 in schedules1:
    print(schedule1.text.strip())


print()
print('더불어민주당에서 전해드리는 오늘의 일정 및 행사안내입니다.')
print(ssibal)
print()
for schedule2 in schedules2:
    print(schedule2.text.strip())