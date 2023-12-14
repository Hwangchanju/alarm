import time
from telegram import ChatAction, chat, message, replymarkup
from telegram import InlineKeyboardButton as BTN
from telegram import InlineKeyboardMarkup as MARKUP
import telegram
from telegram.callbackquery import CallbackQuery
from telegram.ext import Updater, Filters, dispatcher
from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler

 
TOKEN='2019958870:AAFfhFkGhXcSCPAi9p8Zz4B2jCYNtshCXCo'

bot = telegram.Bot(TOKEN)

chat_id = '1758525870'

updater = Updater(token = TOKEN, use_context=True)
dispatcher = updater.dispatcher

keyword = []

def add_Keyword(update, context):
    add_buttons=[[
        BTN('추가', callback_data=1)
        , BTN('제거', callback_data=2)
    ]]

    add_markup = MARKUP(add_buttons)

    context.bot.send_message(
        chat_id = update.message.chat_id
        , text = '키워드 수정'
        , reply_markup = add_markup
    )

def cb_addKeyword(update, context):
    query = update.callback_query
    data = query.data

    context.bot.send_chat_action(
        chat_id = update.effective_user.id
        , action = ChatAction.TYPING
    )

    if data == '1':
        bot.sendMessage(chat_id=chat_id, text = '키워드 입력 : ')
        
    elif data == '2':
        print('키워드 목록\n')
        for key in keyword:
            print(key)

add_button_handler = CommandHandler('key', add_Keyword)
add_callback_handler = CallbackQueryHandler(cb_addKeyword)

dispatcher.add_handler(add_button_handler)
dispatcher.add_handler(add_callback_handler)

updater.start_polling()
updater.idle()