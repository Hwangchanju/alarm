# token = 2019958870:AAFfhFkGhXcSCPAi9p8Zz4B2jCYNtshCXCo
# id = 1758525870
#      1725010456

def schedule_view():
    import telegram
    import requests
    from bs4 import BeautifulSoup
    from datetime import date, datetime
    
    weekday = datetime.today().weekday()
    week = ['월', '화', '수', '목', '금', '토', '일']
    
    Token = '2019958870:AAFfhFkGhXcSCPAi9p8Zz4B2jCYNtshCXCo'
    bot = telegram.Bot(Token)
    chat_id = 1758525870

    header = {'User-agent' : 'Mozila/2.0'}

    response = requests.get('https://m.newspim.com/search?searchword=정치일정')
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    url = soup.select_one('#vue-main > div > div.listgroup.mgin15 > article:nth-child(1) > a')

    search_weekday = soup.select_one('.thumb_h .subject')
    print(url("v-html"))

schedule_view()

# .div.listgroup.mgin15 > article:nth-child(1)
