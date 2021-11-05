import requests
from bs4 import BeautifulSoup
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler

# 검색 키워드
search_word = '초록뱀컴퍼니'

# 텔레그램 봇 생성
token = '2019958870:AAFfhFkGhXcSCPAi9p8Zz4B2jCYNtshCXCo'
bot = telegram.Bot(token = token)

# 스케줄러 생성
sched = BlockingScheduler()


old_links = []

# 링크 추출 함수
def extract_links(old_links=[]):
    url = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={search_word}'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    search_result = soup.select_one('.list_news')
    news_title = search_result.select('.bx > div.news_wrap.api_ani_send > div > a')

    links = []
    for news in news_title[:3]:
        link = news['href']
        links.append(link)

    new_links = []
    for link in links:
        if link not in old_links:
            new_links.append(link)

    return new_links

def send_links():
    chat_id = '1758525870'
    global old_links
    new_links = extract_links(old_links)
    if new_links:
        for link in new_links:
            bot.sendMessage(chat_id=chat_id, text=link)
    else:
        bot.sendMessage(chat_id=chat_id, text='새로운 뉴스 없음')
    old_links += new_links.copy()
    old_links = list(set(old_links))

# 최초 시작
send_links()

sched.add_job(send_links, 'cron', second='0')
sched.start()