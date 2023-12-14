# token = 2019958870:AAFfhFkGhXcSCPAi9p8Zz4B2jCYNtshCXCo
# id = 1758525870
#      1725010456

# "id" : "7552811101698946278" , "data" : "1" - 버튼 1
# "id" : "7552811102886748927" , "data" : "2" - 버튼 2
# "id" : "7552811100903521355" , "data" : "3" - 버튼 3

import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup as MARKUP
from telepot.namedtuple import InlineKeyboardButton as BTN

token = '2019958870:AAFfhFkGhXcSCPAi9p8Zz4B2jCYNtshCXCo'
ID = '1758525870'
bot = telepot.Bot(token)

def btn_show(msg):
    btn1 = BTN(text = "1. Hello", callback_data = "1")
    btn2 = BTN(text = "2. bye", callback_data = "2")
    mu = MARKUP(inline_keyboard = [btn1, btn2])
    bot.sendMessage(ID, "선택하세요", reply_markup = mu)

def query_ans(msg):
    query_id = msg["id"]
    query_data = msg["data"]

    if query_data == "1":
        bot.answerCallbackQuery(query_id, text="안녕!")
    elif query_data == "2":
        bot.answerCallbackQuery(query_id, text="잘가")

MessageLoop(bot,{'chat' : btn_show, 'callback_query' : query_ans}).run_as_thread()
