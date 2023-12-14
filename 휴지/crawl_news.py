
# token = 2019958870:AAFfhFkGhXcSCPAi9p8Zz4B2jCYNtshCXCo

# id = 1758525870  #찬주
#      1725010456

import requests
from bs4 import BeautifulSoup
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler

old_links = []
# 검색 키워드
search_word = '[단독]'

def alram_on(update, context):
    # 텔레그램 봇 생성
    TOKEN = '2019958870:AAFfhFkGhXcSCPAi9p8Zz4B2jCYNtshCXCo'
    bot = telegram.Bot(token = TOKEN)

    chat_id = '1758525870'

    # 스케줄러 생성
    sched = BlockingScheduler()

    # 링크 추출 함수
    def extract_links(old_links=[]):
        url = f'https://search.naver.com/search.naver?where=news&query={search_word}&sm=tab_opt&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3Aall&is_sug_officeid=0'
        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        search_result = soup.select_one('.list_news')
        news_title = search_result.select('.bx > div.news_wrap.api_ani_send > div > a')

        links = []
        for news in news_title[:1]:
            link = news['href']
            links.append(link)

        new_links = []
        for link in links:
            if link not in old_links:
                new_links.append(link)

        return new_links

    def send_links():
            
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

    sched.add_job(send_links, 'cron', second='30')
    sched.start()

