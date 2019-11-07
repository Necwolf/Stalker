from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from sqlalchemy import desc
from model import *
from sqlite3 import *
import re
from datetime import datetime
import random

engine = create_engine('postgresql+psycopg2://postgres:3365@localhost:5432/postgres',echo=True)
Session = sessionmaker(bind=engine)
session = Session()





def add_new_member(telegram_id, first_name, last_name):
    new_member = User(telegram_id=telegram_id, first_name=first_name, last_name=last_name)
    session.add(new_member)
    session.commit()

def check_in_db(tgid):
    one = session.query(Hero).filter_by(tgid=tgid).first()
    text = f'ID: {one.tgid}'
    return text



def one_row_tgid_hero(tgid):
    try:
        session.query(Hero).filter_by(tgid=tgid).first()
        text = 'Ok'
        print('Ok')
        return text
    except:
        text = 'NO'
        print('NO')
        return text

def add_new_hero(tgid ,nickname, frac, otryad, zvanie, rang, adena, attack, armor, STR, PSI, RAD, INT, AGIL,MAXHP,last_update, crit):
    new_hero = Hero(tgid=tgid ,nickname=nickname, frac=frac, otryad=otryad, zvanie=zvanie, rang=rang, adena=adena, attack=attack, armor=armor, STR=STR, PSI=PSI, RAD=RAD, INT=INT, AGIL=AGIL,MAXHP=MAXHP,last_update=last_update, crit=crit)
    session.add(new_hero)
    session.commit()

def update_hero(tgid ,nickname, frac, rang, adena, otryad, attack, armor, STR, PSI, RAD, INT, AGIL,MAXHP,last_update,crit):
    hero = session.query(Hero).filter_by(tgid=tgid).first()
    hero.nickname=nickname
    hero.otryad =otryad
    hero.frac=frac
    hero.rang=rang
    hero.adena=adena
    hero.attack=attack
    hero.armor=armor
    hero.STR=STR
    hero.PSI=PSI
    hero.RAD=RAD
    hero.INT=INT
    hero.AGIL=AGIL
    hero.MAXHP=MAXHP
    hero.last_update=last_update
    hero.crit=crit
    session.commit()

def one_row_tgid_hero(userid):
    one = session.query(Hero).filter_by(tgid=userid).first()
    return one

def parse_kpk(msg):
    id = re.search(r'🆔(\d+)', msg.text).group(1)
    frac = re.search(r'(📯Группировка:) (.?)(.{1,125})', msg.text).group(3)
    try:
        otr = re.search(r'🎗Отряд:(.{1,125})(/squad)', msg.text).group(1)
    except:
        otr = None
    nickname = re.search(r'\A(.{1,125})', msg.text).group(1)
    rang = re.search(r'⚜️Ранг: (.{1,125})', msg.text).group(1)
    MAXHP = re.search(r'♥️Здоровье \d{1,4}/(\d{1,4})', msg.text).group(1)
    armor = re.search(r'🛡Броня:(.?)(\d+)', msg.text).group(2)
    adena = re.search(r'💰Рубли:(.?)(.{1,125})', msg.text).group(2)
    attack = re.search(r'💥Атака(.?)(\d+)', msg.text).group(2)
    Sila = re.search(r'💪🏻Сила:(.?)(\d+)', msg.text).group(2)
    psi = re.search(r'🌀Псизащита(.?)(\d+)', msg.text).group(2)
    rad = re.search(r'♻️Радзащита(.?)(\d+)', msg.text).group(2)
    intel = re.search(r'🔬Интеллект(.?)(.?)(\d+)', msg.text).group(3)  # 3 group
    lvk = re.search(r'🥏Ловкость (.?)(.?)(.?)(\d+)', msg.text).group(4)  # check
    crit = re.search(r'⚡️Крит (\d+)',msg.text).group(1)
    if frac == 'Бандиты':
        try:
            userid = one_row_tgid_hero(id)
            print(userid.tgid)
            print(crit)
            update_hero(tgid=id, nickname=nickname, frac=frac, otryad=otr, rang=rang, adena=adena, attack=attack,
                        armor=armor,
                        STR=Sila, PSI=psi, RAD=rad, INT=intel, AGIL=lvk, MAXHP=MAXHP, last_update=msg.date, crit=crit)
        except:
            add_new_hero(tgid=id, nickname=nickname, zvanie=None, otryad=otr, frac=frac, rang=rang, adena=adena,
                         attack=attack, armor=armor, STR=Sila, PSI=psi, RAD=rad, INT=intel, AGIL=lvk, MAXHP=MAXHP,
                         last_update=msg.date, crit=crit)
    else:
        print('Ухади')


def profile(msg,tgid):
    try:
        #print(msg)
        data = one_row_tgid_hero(tgid)
        try:
            lastupdate = datetime.utcfromtimestamp(data.last_update).strftime('%Y-%m-%d %H:%M:%S')
        except:
            lastupdate = '31536001'
        text = f'📁Профиль:🔪 {data.nickname}\n' \
            f'️├👤Юзернейм: @{msg.from_user.username}\n' \
            f'├🎫ID: {data.tgid}\n' \
            f'├📯 Группировка: 🔪{data.frac}\n' \
            f'├♠️ Банда: {data.otryad}\n' \
            f'└💬Погремуха: {data.zvanie}\n\n' \
            f'Общие данные:\n' \
            f'├⚜️Ранг: {data.rang}\n' \
            f'└💰Рубли: {data.adena}\n\n' \
            f'Боевые характеристики:\n' \
            f'├♥️ {data.MAXHP} ' \
            f'🛡 {data.armor}\n' \
            f'└💥 {data.attack} ' \
            f'⚡️ {data.crit}\n\n' \
            f'Основные статы:\n' \
            f'├💪🏻 {data.STR} 🥏 {data.AGIL}\n' \
            f'├🌀 {data.PSI} 🔬 {data.INT}\n' \
            f'└♻️ {data.RAD}\n\n' \
            f'📝Статистика pvp:\n' \
            f'├⚔️ 0 (0%)\n' \
            f'└☠️ 0 (0%)\n' \
               f'🕰Last update: {lastupdate}'
    except:
        text = "что то пошло не так"
        print('Ошибка в def profile / func.py')
        return text
        #todo сделать компактный вид профиля
    return text

def mini_profile(tgid):
    try:
        data = one_row_tgid_hero(tgid)
        text = f'''📁Профиль:🔪 {data.nickname}
├♠️ Банда: {data.otryad}
└💬Погремуха: {data.zvanie}

├⚜️Ранг: {data.rang}   
└💰Рубли: {data.adena}

├♥️ {data.MAXHP} 🛡 {data.armor} 💥 {data.attack}
├💪🏻 {data.STR} 🥏 {data.AGIL} 
├🌀 {data.PSI} 🔬 {data.INT}
└♻️ {data.RAD} ⚡️ {data.crit}
Полный вид /full
        '''
    except:
        text = "что то пошло не так"
        print('Ошибка в def mini_profile / func.py')
        return text
    return text
#todo ТОП по победам в миниигры


def top_attack(tgid):
    mas = []
    indmas = []
    two = session.query(Hero).order_by(desc(Hero.attack)).all()
    for bar in two:
        indmas.append(bar.tgid)
    one = session.query(Hero).order_by(desc(Hero.attack)).all()
    blist = ["#" + str(i + 1) + ". " + f'🔪***{one[i].nickname}***    💥***{one[i].attack}***' for i in range(len(one))]
    mas.append(blist)
    youindex = indmas.index(tgid)
    if youindex <= 10:
        text = f'{mas[0][0]}\n{mas[0][1]}\n{mas[0][2]}\n{mas[0][3]}\n{mas[0][4]}\n{mas[0][5]}\n{mas[0][6]}\n{mas[0][7]}\n{mas[0][8]}\n{mas[0][9]}\n\n'
        return text
    else:
        text = f'{mas[0][0]}\n{mas[0][1]}\n{mas[0][2]}\n{mas[0][3]}\n{mas[0][4]}\n{mas[0][5]}\n{mas[0][6]}\n{mas[0][7]}\n{mas[0][8]}\n{mas[0][9]}\n ...\n{mas[0][youindex]} '
        return text

def top_adena(tgid):
    mas = []
    indmas = []
    two = session.query(Hero).order_by(desc(Hero.adena)).all()
    for bar in two:
        indmas.append(bar.tgid)
    one = session.query(Hero).order_by(desc(Hero.adena)).all()
    blist = ["#"+str(i+1)+". "+f'🔪***{one[i].nickname}***    💰***{one[i].adena}***'for i in range(len(one))]
    mas.append(blist)
    youindex = indmas.index(tgid)
    if youindex  <= 10 :
        text = f'{mas[0][0]}\n{mas[0][1]}\n{mas[0][2]}\n{mas[0][3]}\n{mas[0][4]}\n{mas[0][5]}\n{mas[0][6]}\n{mas[0][7]}\n{mas[0][8]}\n{mas[0][9]}\n'
        return text
    else:
        text = f'{mas[0][0]}\n{mas[0][1]}\n{mas[0][2]}\n{mas[0][3]}\n{mas[0][4]}\n{mas[0][5]}\n{mas[0][6]}\n{mas[0][7]}\n{mas[0][8]}\n{mas[0][9]}\n ...\n{mas[0][youindex]} '
        return text

def minigame_one_row_tgid(userid):
    try:
        one = session.query(RockPaper).filter_by(tgid=userid).first()
        return one
    except:
        text = 'NO'
        print('NO')
        return text


def win_rate(userid):
    data = minigame_one_row_tgid(userid)
    text = f'WinRate {data.win_rate}'
    return text


def minigame_rockpaper_new_gamer(tgid):
    new_gamer = RockPaper(tgid=tgid,win=0,lose=0,dead_heat=0,total_game=0,win_rate=0)
    session.add(new_gamer)
    session.commit()

def minigame_rockpaper_update_gamer_nichiya(tgid):
    gamer = session.query(RockPaper).filter_by(tgid=tgid).first()
    gamer.dead_heat += 1
    gamer.total_game += 1
    session.commit()

def minigame_rockpaper_update_gamer_win(tgid):
    gamer = session.query(RockPaper).filter_by(tgid=tgid).first()
    gamer.win += 1
    gamer.total_game += 1
    session.commit()

def minigame_rockpaper_update_gamer_lose(tgid):
    gamer = session.query(RockPaper).filter_by(tgid=tgid).first()
    gamer.lose += 1
    gamer.total_game += 1
    session.commit()

def minigame_rockpaper_update_gamer_win_rate(tgid):
    gamer = session.query(RockPaper).filter_by(tgid=tgid).first()
    gamer.win_rate = (gamer.total_game/ 100) * gamer.win
    print(gamer.win_rate)
    session.commit()
#todo Довести до ума мини игру!


def otryad_list(sq):
    lists =[]
    mas = 'Список данного отряда:\n\n'
    one = session.query(Hero).filter_by(otryad=sq).all()
    for bar in one:
        lists.append(bar.nickname)
    for i in lists:
        i +='\n'
        mas += i
    return mas

def roll(start=0, stop=100):
    num = random.randint(start,stop)
    return num


def parse_detali_group(msg):
    if '⬜️Лёгкие бронепластины' in msg.text:
        light_plast = re.search(r'⬜️Лёгкие бронепластины.?(.\d+)', msg.text).group(1)
    else:
        light_plast = 0
    if '🔶Микросхема Z' in msg.text:
        micro_z = re.search(r'🔶Микросхема Z.?(.\d+)', msg.text).group(1)
    else:
        micro_z = 0
    if '🔹Микросхема X' in msg.text:
        micro_x = re.search(r'🔹Микросхема X.?(.\d+)', msg.text).group(1)
    else:
        micro_x = 0
    if '🔸Микросхема L' in msg.text:
        micro_l = re.search(r'🔸Микросхема L.?(.\d+)', msg.text).group(1)
    else:
        micro_l = 0
    if '🔋Аккумулятор (неисправный)' in msg.text:
        acc_non = re.search(r'🔋Аккумулятор \(неисправный\).?(.\d+)', msg.text).group(1)
    else:
        acc_non = 0
    if '🎛Фреоновый охладитель' in msg.text:
        fer_cold = re.search(r'🎛Фреоновый охладитель.?(.\d+)', msg.text).group(1)
    else:
        fer_cold = 0
    if '📿Медная проволка' in msg.text:
        cooprum = re.search(r'📿Медная проволка.?(.\d+)', msg.text).group(1)
    else:
        cooprum = 0
    if 'Провод' in msg.text:
        provod = re.search(r'🧵Провод.?(.\d+)', msg.text).group(1)
    else:
        provod = 0
    if '🗜Крепежные детали' in msg.text:
        crepej = re.search(r'🗜Крепежные детали.?(.\d+)', msg.text).group(1)
    else:
        crepej = 0
    if '⛑Сфера' in msg.text:
        sphere = re.search(r'⛑Сфера.?(.\d+)', msg.text).group(1)
    else:
        sphere = 0

    r_text = f"""Ваши @{msg.from_user.username} успехи в фарме ПСИ шлема:
    
⬜️Лёгкие бронепластины {light_plast} / 2
🔶Микросхема Z {micro_z} / 2
🔹Микросхема X {micro_x} / 3
🔸Микросхема L {micro_l} / 1
🔋Аккумулятор (неисправный) {acc_non} / 2
🎛Фреоновый охладитель {fer_cold} / 2
📿Медная проволка {cooprum} / 3
🧵Провод {provod} / 10
🗜Крепежные детали {crepej} / 4
⛑Сфера {sphere} / 1 
    """
    return r_text


def parse_detali(msg):
    if '⬜️Лёгкие бронепластины' in msg.text:
        light_plast = re.search(r'⬜️Лёгкие бронепластины.?(.\d+)', msg.text).group(1)
    else:
        light_plast = 0
    if '🔶Микросхема Z' in msg.text:
        micro_z = re.search(r'🔶Микросхема Z.?(.\d+)', msg.text).group(1)
    else:
        micro_z = 0
    if '🔹Микросхема X' in msg.text:
        micro_x = re.search(r'🔹Микросхема X.?(.\d+)', msg.text).group(1)
    else:
        micro_x = 0
    if '🔸Микросхема L' in msg.text:
        micro_l = re.search(r'🔸Микросхема L.?(.\d+)', msg.text).group(1)
    else:
        micro_l = 0
    if '🔋Аккумулятор (неисправный)' in msg.text:
        acc_non = re.search(r'🔋Аккумулятор \(неисправный\).?(.\d+)', msg.text).group(1)
    else:
        acc_non = 0
    if '🎛Фреоновый охладитель' in msg.text:
        fer_cold = re.search(r'🎛Фреоновый охладитель.?(.\d+)', msg.text).group(1)
    else:
        fer_cold = 0
    if '📿Медная проволка' in msg.text:
        cooprum = re.search(r'📿Медная проволка.?(.\d+)', msg.text).group(1)
    else:
        cooprum = 0
    if 'Провод' in msg.text:
        provod = re.search(r'🧵Провод.?(.\d+)', msg.text).group(1)
    else:
        provod = 0
    if '🗜Крепежные детали' in msg.text:
        crepej = re.search(r'🗜Крепежные детали.?(.\d+)', msg.text).group(1)
    else:
        crepej = 0
    if '⛑Сфера' in msg.text:
        sphere = re.search(r'⛑Сфера.?(.\d+)', msg.text).group(1)
    else:
        sphere = 0

    r_text = f"""Ваши успехи в фарме ПСИ шлема:

⬜️Лёгкие бронепластины {light_plast} / 2
🔶Микросхема Z {micro_z} / 2
🔹Микросхема X {micro_x} / 3
🔸Микросхема L {micro_l} / 1
🔋Аккумулятор (неисправный) {acc_non} / 2
🎛Фреоновый охладитель {fer_cold} / 2
📿Медная проволка {cooprum} / 3
🧵Провод {provod} / 10
🗜Крепежные детали {crepej} / 4
⛑Сфера {sphere} / 1 
    """
    return r_text
