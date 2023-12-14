# token = 2019958870:AAFfhFkGhXcSCPAi9p8Zz4B2jCYNtshCXCo
# id = 1758525870
#      1725010456

# "id" : "7552811101698946278" , "data" : "1" - 버튼 1
# "id" : "7552811102886748927" , "data" : "2" - 버튼 2
# "id" : "7552811100903521355" , "data" : "3" - 버튼 3

#buttons_bot.py
import time
from telegram import ChatAction
from telegram import InlineKeyboardButton as BTN
from telegram import InlineKeyboardMarkup as MARKUP
from telegram.ext import Updater, Filters, dispatcher
from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler
 
TOKEN='2019958870:AAFfhFkGhXcSCPAi9p8Zz4B2jCYNtshCXCo'


updater = Updater(token = TOKEN, use_context=True)
dispatcher = updater.dispatcher

def switch_btn(update, context):
    switch_buttons = [[
        BTN('ON', callback_data=1)
        , BTN('OFF', callback_data=2)
    ]]

    reply_markup = MARKUP(switch_buttons)

    context.bot.send_message(
        chat_id = update.message.chat_id
        , text = 'ON/OFF 설정'
        , reply_markup = reply_markup
    )

def cb_switch(update, context):
    query = update.callback_query
    data = query.data

    context.bot.send_chat_action(
        chat_id = update.effective_user.id
        , action = ChatAction.TYPING
    )
    crawl_news_copy.alram(data)

onoff_handler = CommandHandler('switch', switch_btn)
onoff_callback = CallbackQueryHandler(cb_switch)

dispatcher.add_handler(onoff_handler)
dispatcher.add_handler(onoff_callback)

updater.start_polling()
updater.idle()