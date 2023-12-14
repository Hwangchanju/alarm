
# 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler

# 크롤링 주기
sched_second = 10

# 텔레그램 봇 생성
token = '6428874186:AAGzAK9TqxPgiW7Zbw08GNvkSqAF4weCydY' # 단독
# token = '2019958870:AAFfhFkGhXcSCPAi9p8Zz4B2jCYNtshCXCo' # BrianChoi
bot = telegram.Bot(token=token)

# 스케쥴러 생성
sched = BlockingScheduler(timezone='Asia/Seoul')

# 기존에 보냈던 링크를 담아둘 리스트
old_links = []

### 텔레그램 ID(Seq)
## 개인 ID
chat_id = '1758525870' # 찬주
# chat_id = '1725010456'
## 채팅방
# chat_id = '-1001686955890'    # develop
# chat_id = '-1001855914048'    # master

# 검색 키워드
search_list = {'[단독]'}    # 2023-05-05 List로 조회 추가

# 제외 키워드
except_keyword_list = {
    '♥️', '인터뷰', 'SNL', '소속사',    # 연예
    '황영웅', '주호민',                # 인물
    '검찰', '경찰', '피해자', '피의자', '노조', '병무청', '뉴스룸', '잼버리', 'JMS', '해병대', '스토킹', '결혼', # 사회
    '퀴즈', '운세'                     # 기타
}

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
'newsen.com',
'sports.hankooki.com'
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

                for except_keyword in except_keyword_list:
                    
                    if except_keyword in title:
                        content_contain_yn = True
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

            # sendMessageYn = True    # 알림 여부 (검색키워드 포함 + 제외키워드 미포함)

            # for search_word in search_list:
            #     if search_word not in link.split('\n')[0]:
            #         sendMessageYn = False

            # # 기사 제목에 특정 키워드 포함 시 알림 제외
            # for exception_keyword in except_keyword_list:
            #     if exception_keyword in link.split('\n')[0]:
            #         sendMessageYn = False

            # if sendMessageYn:
                # bot.sendMessage(chat_id=chat_id, text=link)

    else:
        bot.sendMessage(chat_id=chat_id, text='없어씨발!')

    old_links += new_links.copy()
    old_links = list(set(old_links))


# 최초 시작
send_links()
# 스케쥴러 세팅 및 작동
sched.add_job(send_links, 'interval', seconds=sched_second)
sched.start()