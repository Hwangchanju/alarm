from typing import Text
import telegram
import requests
from bs4 import BeautifulSoup
from requests.api import head

telegram_token = '2019958870:AAFfhFkGhXcSCPAi9p8Zz4B2jCYNtshCXCo'

bot = telegram.Bot(telegram_token)
chat_id = 1758525870

header = {'User-agent' : 'Mozila/2.0'}
# 컨텐츠 순위 
response = requests.get('https://flixpatrol.com/', headers=header)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

ranking_title1 = soup.select('body > div.content.mt-10.mb-20 > div.grid.sm\:gap-x-4.gap-y-8.grid-cols-2.md\:grid-cols-4.lg\:grid-cols-6.lg\:grid-rows-2.lg\:grid-flow-col.-mx-content > div:nth-child(1)')
img = soup.select('body > div.content.mt-10.mb-20 > div.grid.sm\:gap-x-4.gap-y-8.grid-cols-2.md\:grid-cols-4.lg\:grid-cols-6.lg\:grid-rows-2.lg\:grid-flow-col.-mx-content > div:nth-child(2) > div.card-body.p-0.group > a > div > picture > img')
bot.sendPhoto(chat_id=chat_id, photo='img', caption="텍스트", reply_markup={})

