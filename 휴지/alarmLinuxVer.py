
# TODO
# 2. 검색어 지정 기능 추가 ( DB? )
# 3. on/off 기능 추가 ( 특정 시간에만 작동)
#  >> 봇이랑 1:1 채팅으로 검색어 지정, on/off 기능 / 알림은 비공개방에서만?

# 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler

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
# chat_id = '-1001686955890'    # develop - 박형식
chat_id = '-1001855914048'      # master

# 검색 키워드
search_list = {'[단독]'}    # 2023-05-05 List로 조회 추가

# 알림 제외 키워드(연예)
except_keyword_entertain = {'♥️', '인터뷰', 'SNL', '소속사'}

# 알림 제외 키워드(인물)
except_keyword_person = {'황영웅', '주호민'}

# 알림 제외 키워드(사회)
except_keyword_social = {'검찰', '경찰', '피해자', '피의자', '노조', '병무청', '뉴스룸', '잼버리', 'JMS', '해병대', '스토킹', '흉기'}

# 알림 제외 키워드(기타)
except_keyword_etc = {'퀴즈', '운세'}

# 알림 제외 키워드
except_keyword_list = []
# except_keyword_list.append(except_keyword_entertain)
# except_keyword_list.append(except_keyword_person)
# except_keyword_list.append(except_keyword_social)
# except_keyword_list.append(except_keyword_etc)

# 알림 제외 뉴스 회사 주소
except_url_list = {
'spotvnews.co.kr',
'sportsseoul.com',
'sports.chosun.com',
'sports.donga.com',
'starnewskorea.com',
'osen.co.kr',
'raonnews.com',
'tvreport.co.kr',
'xportsnews.com',
'vegannews.co.kr',
'labortoday.co.kr',
'tenasia.hankyung.com',
'enews.imbc.com',
'isplus.com',
'heraldpop.com',
'footballist.co.kr',
'sports.khan.co.kr',
'ent.sbs.co.kr',
'tvdaily.co.kr',
'star.ytn.co.kr',
'biz.heraldcorp.com',
'bntnews.co.kr',
'newsen.com'
}

# 링크 추출 함수
def extract_links(old_links=[]):

    links = []

    for search_word in search_list:

        # 최신순
        url = f'https://search.naver.com/search.naver?where=news&query={search_word}&sm=tab_opt&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3Aall&is_sug_officeid=0'

        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        search_result = soup.select_one('.list_news')
        news_list = search_result.select('.bx > .news_wrap > .news_area > a')   # 원문 기사 태그

        for news in news_list[:10]:
            link = news['href']     # 기사 원문 링크
            title = news['title']   # 기사 제목 ( 네이버 기사 태그 사용 시 사용 불가 )

            url_contain_yn = False  # 특정 회사 URL 제외 Flag

            for except_url in except_url_list:
                if except_url in link:
                    url_contain_yn = True
                    break
            
            if url_contain_yn:
                continue

            content_contain_yn = False  # 특정 문구 포함 여부 Flag

            if except_keyword_list: # 제외 키워드 없는 경우 skip

                for except_list_index in except_keyword_list:
                    
                    for except_keyword in except_list_index:
                        if except_keyword in title:
                            content_contain_yn = True
                            break

                    if content_contain_yn:
                        break

                if content_contain_yn:
                    continue

            links.append(title + '\n' + link)   # 뉴스제목 + 링크

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

            for search_keyword in search_list:
                if search_keyword in link.split('\n')[0]:
                    bot.sendMessage(chat_id=chat_id, text=link)

    old_links += new_links.copy()
    old_links = list(set(old_links))
        

# 최초 시작
send_links()
# 스케쥴러 세팅 및 작동
sched.add_job(send_links, 'interval', seconds=60)
sched.start()

# TODO
