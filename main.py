from config import *
import re
from datetime import *
import telebot
from func import *
from telebot.types import *
from key import *
import minigame
from flask import Flask, request
from Drop import parse_kuski

IDGamebot = 738720259
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)
# future_in_half_hour = datetime.utcnow() + timedelta(hours=2)
# local_time = future_in_half_hour.replace(microsecond=0, second=0)


@bot.message_handler(commands=['start'])
def start_message(msg):
    bot.send_message(msg.chat.id, f'Даров Бандитос {msg.from_user.first_name}\n'
                                  f'Пришли мне /full из бота')
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
@bot.message_handler(commands=['map'])
def atop(msg):
    try:
        if str(msg.chat.id)[0] == '-':
            bot.send_document(msg.chat.id, 'BQADAgAD6AQAAt4d4UoKF5uxlSmpuhYE')
        else:
            bot.send_document(msg.chat.id, 'BQADAgAD6AQAAt4d4UoKF5uxlSmpuhYE')
    except:
        bot.send_message(msg.chat.id, 'Не могу тебе выдать карту, прости',
                         reply_to_message_id=msg.message_id)

@bot.message_handler(content_types=['document'])
def msg_doc(msg):
    print(msg.document.file_id)


# @bot.message_handler(content_types=['new_chat_members'])
# def check_in_bd(msg):
#     try:
#         if str(msg.chat.id)[0] == '-':
#             one = check_in_db(msg.new_chat_member.id)
#             text = f'Проверяем есть ли новый член группы {msg.new_chat_member.id} в базе данных\n' \
#                    f'\nСвои!'
#             bot.send_message(msg.chat.id, text=text, parse_mode='markdown', reply_to_message_id=msg.message_id)
#     except:
#         text = f'Ты блять кто такой?? а ну ухади!'
#         bot.send_message(msg.chat.id, text=text, parse_mode='markdown', reply_to_message_id=msg.message_id)
#         bot.kick_chat_member(msg.chat.id,msg.new_chat_member.id)

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
        text = otryad_list(sq=' Тряси Шатай ')
        bot.send_message(msg.chat.id, text)
    elif msg.chat.id == suicide:
        text = otryad_list(sq='  Курень "Отряд самоубийц"🌚 ')
        bot.send_message(msg.chat.id, text)
    else:
        pass

# @bot.message_handler(commands=['arabtop'])
# def arab(msg):
#     text = """ТОП Арабов фраки:
# НАМБАВАН : 🔪علة العربية"""
#     try:
#         if str(msg.chat.id)[0] == '-':
#             bot.send_message(msg.chat.id, text=text,parse_mode='markdown')
#         else:
#             bot.send_message(msg.chat.id, text=text, parse_mode='markdown')
#     except:
#         bot.send_message(msg.chat.id,'Сначала отправь боту /full из игрового бота', reply_to_message_id=msg.message_id)
#     names = '🔪علة العربية'

@bot.message_handler(commands=['add'])
def add_memb_to_db(msg):
    try:
        # result = []
        # for Members in one_row_tgid_members(telegram_id=msg.reply_to_message.from_user.id):
        #     result.append(Members.telegram_id)
        #     print(result)
        #     if msg.reply_to_message.from_user.id not in result:
                if str(msg.chat.id)[0] == '-':
                    if msg.from_user.id in operators:
                        print(msg)
                        add_new_memb(msg.reply_to_message.from_user.id, msg.reply_to_message.from_user.username)
                        bot.reply_to(msg, "Братишка добавлен!")
                    else:
                        print()
                else:
                    print('только в группах')
            # else:
            #     print('уже есть!')
    except:
        bot.reply_to(msg, 'А выбрать объект?')


@bot.message_handler(commands=['del'])
def del_memb_in_to_db(msg):
    try:
        if str(msg.chat.id)[0] == '-':
            if msg.from_user.id in operators:
                del_new_memb(msg.reply_to_message.from_user.id)
                bot.reply_to(msg, "Ухади, тебе тут не рады!")
            else:
                pass
        else:
            print('только в группах')
    except:
        bot.reply_to(msg,'А выбрать объект?')



# @bot.message_handler(commands=['test'])
# def tell(msg):
#     data = check_in_db_enemy_test()
#     print(data.nickname)


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
    if '💷Фунты:'in msg.text:
        try:
            try:
                print(check_in_db_member(msg.from_user.id).id)
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
            except:
                bot.reply_to(msg, "Я тебя незнаю, нас должны познакомить!!")
        except:
            bot.send_message(msg.chat.id, 'Странный форвард, не находишь?')
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
    elif '🔪Части мутантов:'in msg.text:
        try:
            if msg.forward_from.id == 738720259:

                bot.delete_message(msg.chat.id, msg.message_id)
                if str(msg.chat.id)[0] == '-':
                    result = []
                    for Members in one_row_tgid_members(telegram_id=msg.from_user.id):
                        result.append(Members.telegram_id)
                    if msg.from_user.id in result:
                        text = parse_kuski(msg)
                        bot.send_message(msg.chat.id, text)
                    else:
                        bot.send_message(msg.chat.id, 'Что то ты на пидора похож, а ну пшёл вон !')
                else:
                    result = []
                    for Members in one_row_tgid_members(telegram_id=msg.from_user.id):
                        result.append(Members.telegram_id)
                    if msg.from_user.id in result:
                        text = parse_kuski(msg)
                        bot.send_message(msg.chat.id, text, reply_markup=key)
                    else:
                        bot.send_message(msg.chat.id, 'Что то ты на пидора похож, а ну пшёл вон !')
            else:
                bot.send_message(msg.chat.id, 'Странный форвард, не находишь?')

        except:
            print('Ошибка в парсинге 🔪Части мутантов: main.py')
            pass

    elif "Вы встретили" in msg.text:
        enemynick = re.search(r'Вы встретили (.{1,125}) из', msg.text).group(1)
        print(enemynick)
        if enemynick[0] == '☢':
            print((enemynick).split('/'))
            data = check_in_db_enemy(enemynick[2:])
        else:
            data = check_in_db_enemy(enemynick)
        try:
            bot.reply_to(msg,f'Оо это {data.nickname}, свой!')
        except:
            bot.reply_to(msg, f'Бей {enemynick}, а то смотри на него! ')





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



@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route('/', methods=["GET"])
def index():
    return "Hello, i`m webhook", 200

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url='https://banditos.herokuapp.com/' + TOKEN)
    print(bot.get_webhook_info().__dict__)
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
    # bot.send_message(chat_id=188539449, text=text)
    # bot.polling(none_stop=True)


