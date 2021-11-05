# token = 2019958870:AAFfhFkGhXcSCPAi9p8Zz4B2jCYNtshCXCo
# id = 1758525870
#      1725010456

# "id" : "7552811101698946278" , "data" : "1" - 버튼 1
# "id" : "7552811102886748927" , "data" : "2" - 버튼 2
# "id" : "7552811100903521355" , "data" : "3" - 버튼 3

import telepot
from telepot.loop import MessageLoop # 봇 구동
from telepot.namedtuple import InlineKeyboardMarkup as MU # 마크업
from telepot.namedtuple import InlineKeyboardButton as BT # 버튼

token = '2019958870:AAFfhFkGhXcSCPAi9p8Zz4B2jCYNtshCXCo'
mc = '1758525870'
bot = telepot.Bot(token)

def btn_show(msg):
    btn1 = BT(text="뉴스", callback_data = "1")
    btn2 = BT(text="중앙당 일정", callback_data = "2")
    btn3 = BT(text="컨텐츠 순위", callback_data = "3")
    mu = MU(inline_keyboard = [[btn1, btn2]])
    bot.sendMessage(mc, "선택하세요", reply_markup = mu)

def query_ans(msg):
    # query_id = msg["id"] # 버튼 메시지 id
    query_data = msg["data"] # 콜백 데이터
    
    if query_data == "1":
        bot.sendMessage(mc, text="씨발!")
    elif query_data == "2":
        """import requests
        from bs4 import BeautifulSoup
        from datetime import date, datetime

        header = {'User-agent' : 'Mozila/2.0'}

        # 국민의힘{
        response1 = requests.get("http://www.peoplepowerparty.kr/renewal/news/schedule.do", headers = header)
        html1 = response1.text
        soup1 = BeautifulSoup(html1, 'html.parser')

        poly_part1 = soup1.select_one('.sub-txt').text
        title1 = soup1.select_one('#schedule h1').text
        schedules1 = soup1.select('.txt-box')

        schedule1 = poly_part1 + "\n\n" + title1 + "\n\n"

        for schedules1 in schedules1:
            schedule1 += schedules1.text.strip()

        schedule1 += "\n\n" + "http://www.peoplepowerparty.kr/renewal/news/schedule.do"
        # } 국민의힘

        # 더불어민주당 {
        year = str(datetime.today().year)
        month = str(datetime.today().month)
        day = str(datetime.today().day)
        ssibal = year + '년 ' + month + '월 ' + day + '일 중앙당 일정입니다.'

        today1 = '#schedule_'
        today2 = datetime.today().strftime('%Y%m%d')
        today3 = '.cnt'

        today_text = today1 + today2 + ' ' + today3

        response2 = requests.get("https://theminjoo.kr/schedule", headers = header)
        html2 = response2.text
        soup2 = BeautifulSoup(html2, 'html.parser')

        schedules2 = soup2.select(today_text)

        schedule2 = "더불어민주당에서 전해드리는 오늘의 일정 및 행사안내입니다.\n\n"

        for schedules2 in schedules2:
            schedule2 += schedules2.text.strip()

        schedule2 += "\n\nhttps://theminjoo.kr/schedule"
        # } 더불어민주당


        # 텔레그램 메시지 전송
        bot.sendMessage(mc, text=schedule1)
        bot.sendMessage(mc, text=schedule2)"""

        bot.sendMessage(mc, "뭐씨발!")
    elif query_data == "3":
        bot.sendMessage(mc, "개씨발!")

MessageLoop(bot, {'chat': btn_show, "callback_query" : query_ans}).run_as_thread()