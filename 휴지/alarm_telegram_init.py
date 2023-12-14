#
# telegram 2023-05-01
# 리눅스 
# ip : 152.70.249.153(instance_last)
# id : opc/Rha~

# TODO
# 1. on/off 기능 추가 ( 특정 시간에만 작동)
# 2. 검색어 지정 기능 추가 ( DB? )

# token = 2019958870:AAFfhFkGhXcSCPAi9p8Zz4B2jCYNtshCXCo  #BrianChoi

# id = 1758525870  #찬주
#      1725010456

# 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler

# 검색 키워드
search_word = '[단독]'

# 텔레그램 봇 생성
token = '2019958870:AAFfhFkGhXcSCPAi9p8Zz4B2jCYNtshCXCo'
bot = telegram.Bot(token=token)
# 텔레그램 ID(Seq)
chat_id = '1758525870' # 찬주
# chat_id = '1725010456'

# 스케쥴러 생성
sched = BlockingScheduler(timezone='Asia/Seoul')
# 기존에 보냈던 링크를 담아둘 리스트
old_links = []

# 링크 추출 함수
def extract_links(old_links=[]):
    # 정확도순
    # url = f'https://m.search.naver.com/search.naver?where=m_news&sm=mtb_jum&query={search_word}' # 모바일
    url = f'https://search.naver.com/search.naver?where=news&query={search_word}&sm=tab_opt&sort=0&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Ar%2Cp%3Aall&is_sug_officeid=0'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    search_result = soup.select_one('#news_result_list')
    news_list = search_result.select('.bx > .news_wrap > a')

    links = []
    for news in news_list[:5]:
        link = news['href']
        links.append(link)
    
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
            bot.sendMessage(chat_id=chat_id, text=link)

# 새로운 뉴스 없을 때
    # else:
    #     bot.sendMessage(chat_id=chat_id, text='새로운 뉴스 없음')
    
    old_links += new_links.copy()
    old_links = list(set(old_links))

# 최초 시작
send_links()
# 스케쥴러 세팅 및 작동
sched.add_job(send_links, 'interval', seconds=10)
sched.start()