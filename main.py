from config import *
import re
from datetime import *
import telebot
from func import *
from telebot.types import *
from key import *
import minigame

IDGamebot = 738720259
bot = telebot.TeleBot(TOKEN)
# future_in_half_hour = datetime.utcnow() + timedelta(hours=2)
# local_time = future_in_half_hour.replace(microsecond=0, second=0)


@bot.message_handler(commands=['start'])
def start_message(msg):
    bot.send_message(msg.chat.id, f'Даров Бандитос {msg.from_user.first_name}\n'
                                  f'Пришли мне /full из бота',reply_markup=key)
    print(f'Приветсвие {msg.from_user.first_name}')


@bot.message_handler(commands=['mtop'])
def mtop(msg):
    try:
        if str(msg.chat.id)[0] == '-':
            bot.send_message(msg.chat.id, text=top_adena(msg.from_user.id),parse_mode='markdown')
        else:
            bot.send_message(msg.chat.id, text=top_adena(msg.chat.id), parse_mode='markdown')
    except:
        bot.send_message(msg.chat.id,'Сначала отправь боту /full из игрового бота')

@bot.message_handler(commands=['atop'])
def atop(msg):
    try:
        if str(msg.chat.id)[0] == '-':
            bot.send_message(msg.chat.id, text=top_attack(msg.from_user.id),parse_mode='markdown')
        else:
            bot.send_message(msg.chat.id, text=top_attack(msg.chat.id), parse_mode='markdown')
    except:
        bot.send_message(msg.chat.id,'Сначала отправь боту /full из игрового бота', reply_to_message_id=msg.message_id)

@bot.message_handler(commands=['kpkf'])
@bot.message_handler(commands=['fkpk'])
@bot.message_handler(commands=['full'])
def atop(msg):
    try:
        if str(msg.chat.id)[0] == '-':
            bot.send_message(msg.chat.id, text=profile(msg, msg.from_user.id))
        else:
            bot.send_message(msg.chat.id, text=profile(msg, msg.chat.id))
    except:
        bot.send_message(msg.chat.id, 'Сначала отправь боту /full из игрового бота',
                         reply_to_message_id=msg.message_id)

@bot.message_handler(commands=['kpk'])
def atop(msg):
    try:
        if str(msg.chat.id)[0] == '-':
            bot.send_message(msg.chat.id, text=mini_profile(msg.from_user.id))
        else:
            bot.send_message(msg.chat.id, text=mini_profile(msg.chat.id))
    except:

        bot.send_message(msg.chat.id, 'Сначала отправь боту /full из игрового бота',
                         reply_to_message_id=msg.message_id)


@bot.message_handler(commands=['say'])
def say_func(msg):
    if msg.chat.type == 'private':
        if msg.chat.id in operators:
            one = (msg.text).split()
            if one[1] == '1': #Отправка в тряси шатай
                text = msg.text[7:] + f'\n\n©@{msg.chat.username}'
                bot.send_message(tryasi, text=text)
            elif one[1] == '2':#Отправка в Волчий отряд
                text = msg.text[7:] + f'\n\n©@{msg.chat.username}'
                bot.send_message(wolf, text=text)
            elif one[1] == '9': #Отправка всем отрядам
                text = msg.text[7:] + f'\n\n©@{msg.chat.username}'
                bot.send_message(wolf, text=text)
                #bot.pin_chat_message(chat_id=wolf,message_id=msg.message_id,disable_notification=False)
                bot.send_message(tryasi, text=text)
                #bot.pin_chat_message(chat_id=tryasi, message_id=msg.message_id, disable_notification=False)
            else:
                bot.send_message(msg.chat.id,
                                 'Забыл указать отряд куда слать\nПример: /say 1 Текст сообшения\n1 - Тряси шатай\n'
                                 '2 - Волчий отряд\n9 - Все отряды')
        else:
            bot.send_message(msg.chat.id, 'ты не оператор!')

    else:
        pass

@bot.message_handler(content_types=['new_chat_members'])
def check_in_bd(msg):
    try:
        if str(msg.chat.id)[0] == '-':
            one = check_in_db(msg.new_chat_member.id)
            text = f'Проверяем есть ли новый член группы {msg.new_chat_member.id} в базе данных\n' \
                   f'\nСвои!'
            bot.send_message(msg.chat.id, text=text, parse_mode='markdown', reply_to_message_id=msg.message_id)
    except:
        text = f'Ты блять кто такой?? а ну ухади!'
        bot.send_message(msg.chat.id, text=text, parse_mode='markdown', reply_to_message_id=msg.message_id)
        bot.kick_chat_member(msg.chat.id,msg.new_chat_member.id)

@bot.message_handler(commands=['reg_minigame'])
def mini_game(msg):
    if msg.chat.type == "private":
        try:
            minigame_rockpaper_new_gamer(msg.chat.id)
            bot.send_message(msg.chat.id, text=minigame.text, reply_markup=KNB)
        except:
            bot.send_message(msg.chat.id, text='Уже зарегестрирован', reply_markup=KNB)

@bot.message_handler(commands=['minigame'])
def mini_game(msg):
    if msg.chat.type == "private":
        try:
            bot.send_message(msg.chat.id, text=minigame.text, reply_markup=KNB)
        except:
            minigame_rockpaper_new_gamer(msg.chat.id)
            print('зарегали')
            bot.send_message(msg.chat.id, text=minigame.text, reply_markup=KNB)

    else:
        pass

@bot.message_handler(commands=['sql'])
def sqfunc(msg):
    if msg.chat.id == wolf:
        text = otryad_list(sq=' Волчий Отряд🐺 ')
        bot.send_message(msg.chat.id,text)
    elif msg.chat.id == tryasi:
        text = otryad_list(sq=' Тряси-шатай ')
        bot.send_message(msg.chat.id, text)
    elif msg.chat.id == suiside:
        text = otryad_list(sq=' Курень "Отряд самоубийц"🌚 ')
        bot.send_message(msg.chat.id, text)
    else:
        pass

@bot.message_handler(commands=['roll'])
def def_roll(msg):
    try:
        param = (msg.text).split()
        if len(param) == 3:
            if int(param[1]) < int(param[2]):
                rnd = roll(int(param[1]), int(param[2]))
                text = f'Ты нароллил: {rnd}'
                bot.send_message(msg.chat.id, text=text)
            else:
                bot.send_message(msg.chat.id, 'Первый аргумент не может быть больше второго!')
        elif len(param) == 2:
            rnd = roll(0, int(param[1]))
            text = f'Ты нароллил: {rnd}'
            bot.send_message(msg.chat.id, text=text)
        elif len(param) == 1:
            rnd = roll()
            text = f'Ты нароллил: {rnd}'
            bot.send_message(msg.chat.id, text=text)
        else:
            bot.send_message(msg.chat.id,"Проверь входные данные")
    except:
        bot.send_message(msg.chat.id, "Проверь входные данные")


@bot.channel_post_handler()
def forwmes(msg):
    if msg.chat.id in channel_read:
        for chat in group_frwd_channel:
            bot.forward_message(chat, msg.chat.id, msg.message_id)


@bot.message_handler(content_types=['text'])
def parse_msg(msg):
    if 'Сеть'in msg.text:
        #try:
            if msg.forward_from.id == 738720259:
                parse_kpk(msg)
                if str(msg.chat.id)[0] == '-':
                    bot.reply_to(msg, f'Cпасибо за твой профиль {msg.from_user.first_name}')
                    bot.delete_message(msg.chat.id, msg.message_id)
                else:
                    bot.reply_to(msg, 'Cпасибо за твой профиль', reply_markup=key)
                    bot.delete_message(msg.chat.id, msg.message_id)
            else:
                bot.send_message(msg.chat.id, 'Странный форвард, не находишь?')
                bot.delete_message(msg.chat.id, msg.message_id)
        #except:
            #bot.send_message(msg.chat.id, 'Странный форвард, не находишь?')
    elif '🔧Запчасти:'in msg.text:
        try:
            if msg.forward_from.id == 738720259:

                bot.delete_message(msg.chat.id, msg.message_id)
                if str(msg.chat.id)[0] == '-':
                    text = parse_detali_group(msg)
                    bot.send_message(msg.chat.id, text)
                else:
                    text = parse_detali(msg)
                    bot.send_message(msg.chat.id, text, reply_markup=key)
            else:
                bot.send_message(msg.chat.id, 'Странный форвард, не находишь?')
        except:
            print('Ошибка в парсенге 🔧Запчасти: main.py')
            pass
    elif '📁Профиль'in msg.text:
        if str(msg.chat.id)[0] == '-':
           pass
        else:
            bot.send_message(msg.chat.id, text=profile(msg, msg.chat.id), reply_markup=key)
    elif 'text' in msg.text:
        print(msg)



@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'Камень':
        bot.edit_message_text(text=minigame.knb(call,'Камень'),chat_id=call.from_user.id,message_id=call.message.message_id,reply_markup=KNB)
        bot.answer_callback_query(call.id, "Камень")
    if call.data == 'ножницы':
        bot.edit_message_text(minigame.knb(call,'ножницы'),call.from_user.id,call.message.message_id,reply_markup=KNB)
        bot.answer_callback_query(call.id, "ножницы")
    if call.data == 'бумага':
        bot.edit_message_text(minigame.knb(call,'бумага'),call.from_user.id,call.message.message_id,reply_markup=KNB)
        bot.answer_callback_query(call.id, "бумага")
    if call.data == 'ящерица':
        bot.edit_message_text(minigame.knb(call,'ящерица'),call.from_user.id,call.message.message_id,reply_markup=KNB)
        bot.answer_callback_query(call.id, "ящерица")
    if call.data == 'спок':
        bot.edit_message_text(minigame.knb(call,'спок'),call.from_user.id,call.message.message_id,reply_markup=KNB)
        bot.answer_callback_query(call.id, "спок")
    if call.data == 'cb_exit':
        bot.delete_message(call.from_user.id,call.message.message_id)
        bot.answer_callback_query(call.id, "Exit")
    if call.data == 'cb_stat':
        minigame_rockpaper_update_gamer_win_rate(call.from_user.id)
        #bot.edit_message_text(win_rate(call.from_user.id),call.from_user.id,call.message.message_id,reply_markup=KNB)
        #bot.answer_callback_query(call.id, "Статистика")


if __name__ == '__main__':
    bot.polling(none_stop=True)


