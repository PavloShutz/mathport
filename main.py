from mathing import calc  # this method also works, but it's funny that you can't do like 20/5...
from telegram.ext import Filters, MessageHandler, CommandHandler, Updater
import json
from datetime import datetime

TOKEN = '5252906753:AAEjVzkESABxH7PmU09dA4xhnXobAtWuvOQ'
updater = Updater(TOKEN)


def start(update, context):
    chat = update.effective_chat
    first_name = update.message.chat.first_name
    context.bot.send_message(chat_id=chat.id,
                             text=f'Hello {first_name}! I\'m math bot. Type /help for more info 🧐.')


def helper(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='Type any operation you want, and that\'s all 😁')


def load_file_data(data):
    with open('new.json', encoding='utf-8') as f:
        file_data = json.load(f)
        file_data['info'].append(data)
        with open('new.json', 'w', encoding='utf-8') as outfile:
            json.dump(file_data, outfile, ensure_ascii=False, indent=2)


def save_info(user_name, user_message, bot_message, time):
    new_data = {'user_name': user_name,
                'user_message': user_message,
                'bot_message': bot_message,
                'time_added': time}
    load_file_data(new_data)


def reply_message(update, context):
    chat = update.effective_chat
    message = update.message.text
    user_name = update.message.chat.first_name
    try:
        result = calc(message)
        text = f"{result}"
        context.bot.send_message(chat_id=chat.id, text=text)
        save_info(user_name, message, text, datetime.today().strftime('%A-%d-%B-%Y %H:%M:%S'))
    except ZeroDivisionError:
        text = 'Division by zero!'
        context.bot.send_message(chat_id=chat.id, text=text)
        save_info(user_name, message, text, datetime.today().strftime('%A-%d-%B-%Y %H:%M:%S'))
    except (IndexError, SyntaxError):
        text = 'Invalid input!!!'
        context.bot.send_message(chat_id=chat.id, text=text)
        save_info(user_name, message, text, datetime.today().strftime('%A-%d-%B-%Y %H:%M:%S'))


disp = updater.dispatcher
disp.add_handler(CommandHandler('start', start))
disp.add_handler(CommandHandler('help', helper))
disp.add_handler(MessageHandler(Filters.all, reply_message))

updater.start_polling()
updater.idle()
