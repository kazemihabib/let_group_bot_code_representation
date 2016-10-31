#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler,Filters ,MessageHandler
#***********************************************
import api
#***********************************************

def start(bot, update):
    update.message.reply_text('Hi!')

def error(bot, update, error):
    print('error',error)

#****************************************
def sendLyric(bot,update):
    choice = int(update.message.text)
    try:
        link = links[choice] 

        lyric = api.lyric(link)
        update.message.reply_text(str(lyric))
    except Exception as error:
        print('error: ',error)
        update.message.reply_text("Oops! i\'m sorry!\n Something went wrong.")
#****************************************
            
def findLyrics(bot,update):
    links = api.search(update.message.text)

    lyrics=[]
    for index,link in enumerate(links):
        lyric = link.replace('http://www.metrolyrics.com/','').replace('.html','').replace('-lyrics-',' ').replace('-', ' ')
        lyrics.append(str(index)+' - ' + lyric)
      
    lyrics = '\n'.join(lyrics)
    update.message.reply_text(lyrics)

    print('links',links)

def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("266267518:AAFW2y2drcXVaJr0NgIlA6nYwgzSWohvepo")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))

#***********************************************
    dp.add_handler(MessageHandler(Filters.text,findLyrics))
#***********************************************

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    updater.idle()


if __name__ == '__main__':
    main()