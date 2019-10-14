from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from model import *
from sqlite3 import *
import re
from datetime import datetime

engine = create_engine('postgresql+psycopg2://postgres:3365@localhost:5432/postgres',echo=True)
Session = sessionmaker(bind=engine)
session = Session()





def add_new_member(telegram_id, first_name, last_name):
    new_member = User(telegram_id=telegram_id, first_name=first_name, last_name=last_name)
    session.add(new_member)
    session.commit()

def one_row_tgid(userid):
    one = session.query(User).filter_by(telegram_id=userid).all()
    two =[]
    for i in one:
        two.append(i)
    return two

def add_new_hero(tgid ,nickname, frac, otryad, zvanie, lvl, adena, attack, armor, STR, PSI, RAD, INT, AGIL,MAXHP,last_update):
    new_hero = Hero(tgid=tgid ,nickname=nickname, frac=frac, otryad=otryad, zvanie=zvanie, lvl=lvl, adena=adena, attack=attack, armor=armor, STR=STR, PSI=PSI, RAD=RAD, INT=INT, AGIL=AGIL,MAXHP=MAXHP,last_update=last_update)
    session.add(new_hero)
    session.commit()

def update_hero(tgid ,nickname, frac, lvl, adena, attack, armor, STR, PSI, RAD, INT, AGIL,MAXHP,last_update):
    hero = session.query(Hero).filter_by(tgid=tgid).first()
    hero.nickname=nickname
    hero.frac=frac
    hero.lvl=lvl
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
    session.commit()

def one_row_tgid_hero(userid):
    one = session.query(Hero).filter_by(tgid=userid).first()
    return one

def parse_kpk(msg):
    id = re.search(r'🆔(\d+)', msg.text).group(1)
    frac = re.search(r'(📯Группировка:) (.?)(.{1,125})', msg.text).group(3)
    try:
        otr = re.search(r'(🎗Отряд:) (.?)(.{1,125})', msg.text).group(3)
    except:
        otr = None
    nickname = re.search(r'\A(.{1,125})', msg.text).group(1)
    lvl = re.search(r'(📈Уровень:)(.?)(.{1,125})', msg.text).group(3)
    MAXHP = re.search(r'♥️Здоровье \d{1,4}/(\d{1,4})', msg.text).group(1)
    armor = re.search(r'🛡Броня:(.?)(\d+)', msg.text).group(2)
    adena = re.search(r'💰Рубли:(.?)(\d+)', msg.text).group(2)
    attack = re.search(r'💥Атака(.?)(\d+)', msg.text).group(2)
    Sila = re.search(r'💪🏻Сила:(.?)(\d+)', msg.text).group(2)
    psi = re.search(r'🌀Псизащита(.?)(\d+)', msg.text).group(2)
    rad = re.search(r'♻️Радзащита(.?)(\d+)', msg.text).group(2)
    intel = re.search(r'🔬Интеллект(.?)(.?)(\d+)', msg.text).group(3)  # 3 group
    lvk = re.search(r'🥏Ловкость (.?)(.?)(.?)(\d+)', msg.text).group(4)  # check
    if frac == 'Бандиты':
        try:
            userid = one_row_tgid_hero(id)
            print(userid.tgid)
            update_hero(tgid=id, nickname=nickname, frac=frac, lvl=lvl, adena=adena, attack=attack,
                        armor=armor,
                        STR=Sila, PSI=psi, RAD=rad, INT=intel, AGIL=lvk, MAXHP=MAXHP, last_update=msg.date)
        except:
            add_new_hero(tgid=id, nickname=nickname, zvanie=None, otryad=otr, frac=frac, lvl=lvl, adena=adena,
                         attack=attack, armor=armor, STR=Sila, PSI=psi, RAD=rad, INT=intel, AGIL=lvk, MAXHP=MAXHP,
                         last_update=msg.date)
    else:
        print('Ухади')
def profile(msg):
    data = one_row_tgid_hero(msg.chat.id)
    lastupdate = datetime.utcfromtimestamp(data.last_update).strftime('%Y-%m-%d %H:%M:%S')
    text = f'📁Профиль:🔪 {data.nickname}\n' \
        f'️├👤Юзернейм: @{msg.from_user.username}\n' \
        f'├🎫ID: {msg.chat.id}\n' \
        f'├📯 Группировка: 🔪{data.frac}\n' \
        f'├♠️ Банда: 🕷{data.otryad}\n' \
        f'└💬Погремуха: {data.zvanie}\n\n' \
        f'Общие данные:\n' \
        f'├📈Уровень: {data.lvl}\n' \
        f'└💰Рубли: {data.adena}\n\n' \
        f'Боевые характеристики:\n' \
        f'├♥️ {data.MAXHP} ' \
        f'🛡 {data.armor}\n' \
        f'└💥 {data.attack} ' \
        f'⚡️ 20 (#todo не работает.)\n\n' \
        f'Основные статы:\n' \
        f'├💪🏻 {data.STR} 🥏 {data.AGIL}\n' \
        f'├🌀 {data.PSI} 🔬 {data.INT}\n' \
        f'└♻️ {data.RAD}\n' \
        f'📝Статистика pvp:\n\n' \
        f'├⚔️ 0 (0%)\n' \
        f'└☠️ 0 (0%)\n' \
           f'🕰Last update: {lastupdate}'
    #todo сделать компактный вид профиля
    return text

#todo ТОП по ЛВЛ. ТОП по деньгам. ТОП по победам в миниигры
