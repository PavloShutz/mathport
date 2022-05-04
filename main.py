"""Telegram Math Bot"""

from mathing import calc  # this is extended math method
from telegram.ext import Filters, MessageHandler, CommandHandler, Updater
from datetime import datetime
from data_configure import ConfigureData


data_config = ConfigureData()
TOKEN = '5252906753:AAEjVzkESABxH7PmU09dA4xhnXobAtWuvOQ'
updater = Updater(TOKEN)

# today's time
time = datetime.now().strftime('%A-%d-%B-%Y %H:%M:%S')


def start(update, context):
    chat = update.effective_chat
    first_name = update.message.chat.first_name
    context.bot.send_message(chat_id=chat.id,
                             text=f'Hello {first_name}! I\'m math bot. Type /help for more info 🧐. '
                                  f'PS: People, I see your messages, please type OPERATIONS, it is not so difficult...')


def helper(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='Type any operation you want, and that\'s all 😁')


def reply_message(update, context):
    chat = update.effective_chat
    message = update.message.text
    user_name = update.message.chat.first_name
    try:
        result = calc(message)
        text = f"{result}"
        context.bot.send_message(chat_id=chat.id, text=text)
        data_config.save_info(user_name, message, text, time)
    except ZeroDivisionError:
        text = 'Division by zero!'
        context.bot.send_message(chat_id=chat.id, text=text)
        data_config.save_info(user_name, message, text, time)
    except (IndexError, SyntaxError):
        text = 'Invalid input!!!'
        context.bot.send_message(chat_id=chat.id, text=text)
        data_config.save_info(user_name, message, text, time)


disp = updater.dispatcher
disp.add_handler(CommandHandler('start', start))
disp.add_handler(CommandHandler('help', helper))
disp.add_handler(MessageHandler(Filters.all, reply_message))

updater.start_polling()
updater.idle()
