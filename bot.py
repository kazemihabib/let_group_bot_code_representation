#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler 

def start(bot, update):
    update.message.reply_text('Hi!')

def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("266267518:AAFW2y2drcXVaJr0NgIlA6nYwgzSWohvepo")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    updater.idle()


if __name__ == '__main__':
    main()