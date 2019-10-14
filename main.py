from config import *
import re
from datetime import *
import telebot
from func import *
from telebot.types import *
from key import *

IDGamebot = 738720259
bot = telebot.TeleBot(TOKEN)
# future_in_half_hour = datetime.utcnow() + timedelta(hours=2)
# local_time = future_in_half_hour.replace(microsecond=0, second=0)


@bot.message_handler(commands=['start'])
def start_message(msg):
    bot.send_message(msg.chat.id, f'Даров Бандитос {msg.from_user.first_name}\n'
                                  f'Пришли мне /full из бота',reply_markup=key)
    print(f'Приветсвие {msg.from_user.first_name}')

# @bot.message_handler(commands=['reg'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, f'Так {message.from_user.first_name}, я проверяю есть ли ты в базеданных.')
#     query = one_row_tgid(message.chat.id)
#     result = []
#     for telegram in query:
#         result.append(telegram.telegram_id)
#     id = message.chat.id
#     if id in result:
#         print(f'есть такой!: {message.chat.id}')
#         bot.send_message(message.chat.id, f'Ты уже зарегестрирован')
#     else:
#         print(f'Нет такого, добавляем!: {message.chat.id}')
#         add_new_member(message.chat.id, message.chat.first_name, message.chat.last_name)
#         bot.send_message(message.chat.id, f'Оп, нет тебя, Регестрирую')



@bot.message_handler(content_types=['text'])
def parse_msg(msg):
    if 'Сеть'in msg.text:
        parse_kpk(msg)
        bot.send_message(msg.chat.id, 'Cпасибо за твой профиль', reply_markup=key)
    elif '📁Профиль'in msg.text:
        bot.send_message(msg.chat.id, text=profile(msg),reply_markup=key)
    elif 'text' in msg.text:
        print(msg.from_user.username)





if __name__ == '__main__':
    bot.polling(none_stop=True)


