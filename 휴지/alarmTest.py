#
# telegram 2023-05-01
# linux(centOs 7)
# ip : 152.70.249.153(instance_last)
# id : opc/Rha~

# TODO
# 1. 기사제목 + 링크 형식으로 메시지 # 2023.05.01 완
# 2. 검색어 지정 기능 추가 ( DB? )
# 3. on/off 기능 추가 ( 특정 시간에만 작동)
#  >> 봇이랑 1:1 채팅으로 검색어 지정, on/off 기능 / 알림은 비공개방에서만?

# 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler
from telegram.ext import Updater, CommandHandler, ConversationHandler
from setAlarmText import user_data_manager

# chatId 알아내는 API
# https://api.telegram.org/bot2019958870:AAFfhFkGhXcSCPAi9p8Zz4B2jCYNtshCXCo/getUpdates  # getUpdates?

# 텔레그램 봇 생성
token = '2019958870:AAFfhFkGhXcSCPAi9p8Zz4B2jCYNtshCXCo'
bot = telegram.Bot(token=token)

# 스케쥴러 생성
sched = BlockingScheduler(timezone='Asia/Seoul')
# 기존에 보냈던 링크를 담아둘 리스트
old_links = []

### 텔레그램 ID(Seq)

# 개인 ID
# chat_id = '1758525870' # 찬주
# chat_id = '1725010456' # 혀선

# 채팅방 > 채팅방 id 는 -num 형식이네
chat_id = '-1001686955890' # test(박형식)   
# chat_id = '-1001686955890' # result

# 검색 키워드
search_list = {'[단독]'}

def received_keyword(update, context):
    keyword = update.message.text
    user_id = update.message.from_user.id

    user_data_manager.set_user_data(user_id, keyword)

    update.message.reply_text(f"검색할 키워드가 '{keyword}'로 설정되었습니다.")
    
    # 검색 키워드를 context에 저장한 뒤, 뉴스 검색 및 알림을 진행하는 함수 호출
    search_news(update, context)
    
    return ConversationHandler.END

def search_news(update, context):
    user_id = update.message.from_user.id
    keyword = user_data_manager.get_user_data(user_id)

# 링크 추출 함수
def extract_links(old_links=[]):

    links = []

    for search_word in search_list:
    # 정확도순
        # url = f'https://search.naver.com/search.naver?where=news&query={search_word}&sm=tab_opt&sort=0&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Ar%2Cp%3Aall&is_sug_officeid=0'

    # 최신순
        url = f'https://search.naver.com/search.naver?where=news&query={search_word}&sm=tab_opt&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3Aall&is_sug_officeid=0'

        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        search_result = soup.select_one('.list_news')
        # news_list = search_result.select('.bx > .news_wrap > a')          # 네이버 기사 태그 > 네이버 기사 태그엔 제목 따로 없음
        news_list = search_result.select('.bx > .news_wrap > .news_area > a')   # 원문 기사 태그

        for news in news_list[:5]:
            link = news['href']     # 기사 원문 링크
            title = news['title']   # 기사 제목 ( 네이버 기사 태그 사용 시 사용 불가 )

            links.append(title + '\n' + link)   # 뉴스제목 + 링크

    print(links)

    new_links=[]
    for link in links:
        if link not in old_links:
            new_links.append(link)
    
    return new_links
    
# 텔레그램 메시지 전송 함수
def send_links():
    global old_links
    new_links = extract_links(old_links)
    if new_links:
        for link in new_links:
            # bot.sendMessage(chat_id=chat_id, text=link)

            for search_word in search_list:
                if search_word in link.split('\n')[0]:
                    bot.sendMessage(chat_id=chat_id, text=link)

            # if search_word in link.split('\n')[0]:  # 기사 제목에 검색 키워드가 포함될 때 메시지 전송
                # bot.sendMessage(chat_id=chat_id, text=link)
            # else:
            #     print(link)

# 새로운 뉴스 없을 때
    else:
        bot.sendMessage(chat_id=chat_id, text='새로운 뉴스 없음')
    
    old_links += new_links.copy()
    old_links = list(set(old_links))

# 최초 시작
send_links()
# 스케쥴러 세팅 및 작동
sched.add_job(send_links, 'interval', seconds=10)
sched.start()