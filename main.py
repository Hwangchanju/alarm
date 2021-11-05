# token = 2019958870:AAFfhFkGhXcSCPAi9p8Zz4B2jCYNtshCXCo
# id = 1758525870
#      1725010456

# "id" : "7552811101698946278" , "data" : "1" - 버튼 1
# "id" : "7552811102886748927" , "data" : "2" - 버튼 2
# "id" : "7552811100903521355" , "data" : "3" - 버튼 3

#buttons_bot.py
import time
from telegram import ChatAction
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, Filters, dispatcher
from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler
 
TOKEN='2019958870:AAFfhFkGhXcSCPAi9p8Zz4B2jCYNtshCXCo'

updater = Updater(token = TOKEN, use_context=True)
dispatcher = updater.dispatcher

def btn_show(update, context):
    task_buttons = [[
        InlineKeyboardButton('뉴스', callback_data=1)
        , InlineKeyboardButton('순위', callback_data=2)
        , InlineKeyboardButton('일정', callback_data=3)
    ], [
        InlineKeyboardButton('취소', callback_data=4)
    ]]

    reply_markup = InlineKeyboardMarkup(task_buttons)

    context.bot.send_message(
        chat_id = update.message.chat_id
        , text = '선택'
        , reply_markup = reply_markup
    )

def cb_button(update, context):
    query = update.callback_query
    data = query.data

    context.bot.send_chat_action(
        chat_id = update.effective_user.id
        , action = ChatAction.TYPING
    )

    if data == '4':
        context.bot.edit_message_text(
            text = '취소'
            , chat_id = query.message.chat_id
            , message_id = query.message.message_id
        )
    else:
        if data == '1':
            crawl_newspaper()
        elif data == '2':
            crawl_ranking()
        elif data == '3':
            import crawl_schedule
            crawl_schedule.schedule_view()
# 신문 지면 크롤링
def crawl_newspaper():
    print('뉴스')

# 컨텐츠 순위표 크롤링
def crawl_ranking():
    print('랭킹')

task_buttons_handler = CommandHandler('task', btn_show)
button_callback_handler = CallbackQueryHandler(cb_button)

dispatcher.add_handler(task_buttons_handler)
dispatcher.add_handler(button_callback_handler)

updater.start_polling()
updater.idle()