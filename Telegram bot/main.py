import Constants as keys
from telegram.ext import *

import Responses as R

print('bot started')

def start_command(ubdate,context):
    ubdate.message.reply_text('Type Something random to start the bot')


def help_comand(ubdate,context):
    ubdate.message.reply_text('If you need help you should ask google')


def handle_message(update,context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    ubdate.message.reply_text(response)


def error(ubdate,context):
    print(f'Update {update} caused error {context.error}')



def main():
    updater = Updater(keys.API_KEY,use_context=True)
    dp = updater.dispatcher


    dp.add_handler(CommandHandler('start',start_command))
    dp.add_handler(CommandHandler('help',help_comand))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()