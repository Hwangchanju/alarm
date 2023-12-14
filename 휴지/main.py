# token = 2019958870:AAFfhFkGhXcSCPAi9p8Zz4B2jCYNtshCXCo
# id = 1758525870
#      1725010456

# "id" : "7552811101698946278" , "data" : "1" - 버튼 1
# "id" : "7552811102886748927" , "data" : "2" - 버튼 2
# "id" : "7552811100903521355" , "data" : "3" - 버튼 3

#buttons_bot.py
import telegram, requests
from bs4 import BeautifulSoup
from telegram.ext import Updater, dispatcher
from telegram.ext import CommandHandler
from apscheduler.schedulers.blocking import BlockingScheduler
 
TOKEN='2019958870:AAFfhFkGhXcSCPAi9p8Zz4B2jCYNtshCXCo'

updater = Updater(token = TOKEN, use_context=True)
dispatcher = updater.dispatcher

old_links = []

def alram_on(update, context):
    # 검색 키워드
    search_word = '초록뱀컴퍼니'

    # 텔레그램 봇 생성
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

    sched.add_job(send_links, 'cron', second='0')
    sched.start()

    def alarm_off(update, context):
        bot.sendMessage(chat_id=chat_id, text='크롤링 종료')
        updater.stop()

on_handler = CommandHandler('on', alram_on)
dispatcher.add_handler(on_handler)
off_handler = CommandHandler('off')
dispatcher.add_handler(off_handler)

updater.start_polling()
updater.idle()
