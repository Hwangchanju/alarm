# token = 2019958870:AAFfhFkGhXcSCPAi9p8Zz4B2jCYNtshCXCo
# id = 1758525870
#      1725010456

def schedule_view():
    import telegram
    import requests
    from bs4 import BeautifulSoup
    from datetime import date, datetime
    
    telegram_token = '2019958870:AAFfhFkGhXcSCPAi9p8Zz4B2jCYNtshCXCo'

    bot = telegram.Bot(telegram_token)
    chat_id = 1758525870

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
    bot.sendMessage(chat_id=chat_id, text=schedule1)
    bot.sendMessage(chat_id=chat_id, text=schedule2)