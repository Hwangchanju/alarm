'''from datetime import date, datetime

today = datetime.today().strftime('%Y%m%d')

print(today)


weekday = datetime.today().weekday()
week = ['월', '화', '수', '목', '금', '토', '일']

print(week[weekday])


텔레그램 파일 전송
file = open('파일경로', 'rb')
bot.sendPhoto(chat_id = '아이디값', file)'''

'''import urllib.request
from bs4 import BeautifulSoup
 
url = "https://m.newspim.com/search?searchword=정치일정"
req = urllib.request.Request(url)
sourcecode = urllib.request.urlopen(url).read()
soup = BeautifulSoup(sourcecode, "html.parser")

article = soup.select_one('#vue-main > div > div.listgroup.mgin15 > article:nth-child(1) > a > div > span')

print(article)'''

#vue-main > div > div.listgroup.mgin15 > article:nth-child(1) > a > div > span

print('\uc57c\uc784\ub9c8')