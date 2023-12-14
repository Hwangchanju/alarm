# token = 2019958870:AAFfhFkGhXcSCPAi9p8Zz4B2jCYNtshCXCo
# id = 1758525870
#      1725010456


import requests
from bs4 import BeautifulSoup
import telegram

TOKEN = '2019958870:AAFfhFkGhXcSCPAi9p8Zz4B2jCYNtshCXCo'
bot = telegram.Bot(token=TOKEN)
chat_id = '1758525870'

header = {'User-agent' : 'Mozila/2.0'}
response = requests.get("http://ncov.mohw.go.kr", headers = header)

html = response.text
soup = BeautifulSoup(html, 'html.parser')

coronic_crawl = soup.select_one('div.occur_graph > table > tbody > tr:nth-child(1) > td:nth-child(5) > span').text
critical_crawl = soup.select_one('div.occur_graph > table > tbody > tr:nth-child(1) > td:nth-child(3) > span').text

coronic = "확진자 : "+coronic_crawl+"명"
critical = "위중증 : "+critical_crawl+"명"

bot.sendMessage(chat_id = '1758525870', text=coronic)