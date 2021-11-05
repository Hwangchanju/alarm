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
from telegram.ext import Updater, Filters
from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler
 
BOT_TOKEN='2019958870:AAFfhFkGhXcSCPAi9p8Zz4B2jCYNtshCXCo'
 
updater = Updater( token=BOT_TOKEN, use_context=True )
dispatcher = updater.dispatcher
 
def cmd_task_buttons(update, context):
    task_buttons = [[
        InlineKeyboardButton( '1.네이버 뉴스', callback_data=1 )
        , InlineKeyboardButton( '2.직방 매물', callback_data=2 )
    ], [
        InlineKeyboardButton( '3.취소', callback_data=3 )
    ]]
    
    reply_markup = InlineKeyboardMarkup( task_buttons )
    
    context.bot.send_message(
        chat_id=update.message.chat_id
        , text='작업을 선택해주세요.'
        , reply_markup=reply_markup
    )
    
def cb_button(update, context):
    query = update.callback_query
    data = query.data
    
    context.bot.send_chat_action(
        chat_id=update.effective_user.id
        , action=ChatAction.TYPING
    )
    
    if data == '3':
        context.bot.edit_message_text(
            text='작업이 취소되었습니다.'
            , chat_id=query.message.chat_id
            , message_id=query.message.message_id
        )
    else:
        context.bot.edit_message_text(
            text='[{}] 작업이 진행중입니다.'.format( data )
            , chat_id=query.message.chat_id
            , message_id=query.message.message_id
        )
        
        if data == '1':
            crawl_navernews()
        elif data == '2':
            crawl_zigbang()
        
        context.bot.send_message(
            chat_id=update.effective_chat.id
            , text='[{}] 작업을 완료하였습니다.'.format( data )
        )
    
def crawl_navernews():
    time.sleep( 5 )
    print( '네이버에서 뉴스를 수집했다.' )
    
def crawl_zigbang():
    time.sleep( 5 )
    print( '직방에서 매물을 수집했다.' )
    
task_buttons_handler = CommandHandler( 'tasks', cmd_task_buttons )
button_callback_handler = CallbackQueryHandler( cb_button )    
 
dispatcher.add_handler( task_buttons_handler )
dispatcher.add_handler( button_callback_handler )
 
updater.start_polling()
updater.idle()