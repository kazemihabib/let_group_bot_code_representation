#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler,Filters ,MessageHandler,CallbackQueryHandler 
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import api

id_storage = {}

def start(bot, update):
    update.message.reply_text('Hi!')

def error(bot, update, error):
    print('error',error)

def  checkMessageType(bot,update):
    txt = update.message.text
    if(txt.isnumeric()): 
        sendLyric(bot,update)
    else :
        findLyrics(bot,update)

def sendLyric(bot,update):
    print('sendLyric')
    global id_storage    
    #****************************
    query = update.callback_query
    # chatId = update.message.chat_id
    chatId = query.message.chat_id
    # choice = int(update.message.text)
    choice = int(query.data) 

    #****************************
    print('choice', choice)

    if chatId in id_storage:
        try:
            links = id_storage[chatId] 
            link = links[choice] 

            lyric = api.lyric(link)
            bot.sendMessage(chat_id=chatId, text= str(lyric))
        except IndexError as indexerror:
            print('IndexError: ',indexerror)
            bot.sendMessage(chat_id=chatId,text = "Oops!\n No previous song with this number is found.")

        except Exception as error:
            print('error: ',error)
            bot.sendMessage(chat_id=chatId,text = "Oops! i\'m sorry!\n Something went wrong.")
            
def findLyrics(bot,update):
    global id_storage
    links = api.search(update.message.text)
    id_storage[update.message.chat_id]=links

    lyrics=[]
    for index,link in enumerate(links):
        lyric = link.replace('http://www.metrolyrics.com/','').replace('.html','').replace('-lyrics-',' ').replace('-', ' ')
        lyrics.append(str(index)+' - ' + lyric)
      
    sendInlineKeyBoard(bot,update,lyrics) 

def sendInlineKeyBoard(bot,update,lyrics):
    chatId = update.message.chat_id
    keyboard = [[InlineKeyboardButton(text, callback_data=str(index))] for index,text in enumerate(lyrics)] 

    reply_markup = InlineKeyboardMarkup(keyboard)

    bot.sendMessage(chat_id=chatId,text='please choose:',reply_markup=reply_markup)

def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("266267518:AAFW2y2drcXVaJr0NgIlA6nYwgzSWohvepo")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(MessageHandler(Filters.text,findLyrics))
    dp.add_handler(CallbackQueryHandler(sendLyric))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    updater.idle()


if __name__ == '__main__':
    main()