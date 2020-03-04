from sqlalchemy import create_engine, Column, String, Integer, Float, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from config import DATABASE


engine = create_engine(DATABASE,echo=True)
Session = sessionmaker(bind=engine)
base = declarative_base(engine)
session = Session()

class dbm:
    __slots__ = ['session']

    def __enter__(self):
        self.session = session()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.commit()
        self.session.close()


class User(base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, nullable=False)
    first_name = Column(String)
    last_name = Column(String, default='Инкогнито', nullable=True)


    def __str__(self, id, telegram_id, first_name, last_name):
        self.id = id
        self.telegram_id = telegram_id
        self.first_name = first_name
        self.last_name = last_name


    def __repr__(self):
        return "'%s','%s','%s','%s'" % (self.id, self.telegram_id, self.first_name, self.last_name)



class Members(base):
    __tablename__ = 'Members'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, nullable=False)
    username = Column(String)



    def __str__(self, id, telegram_id, username):
        self.id = id
        self.telegram_id = telegram_id
        self.username = username


    def __repr__(self):
        return "'%s','%s','%s'" % (self.id, self.telegram_id, self.username)


class Hero(base):
    __tablename__ = 'Hero'

    tgid = Column(Integer,primary_key=True)
    nickname = Column(String, nullable=False)
    frac = Column(String)
    otryad = Column(String,nullable=True)
    zvanie = Column(String,nullable=True)
    rang = Column(String)
    adena = Column(Integer)
    attack = Column(Integer)
    armor = Column(Integer)
    PSI = Column(Integer)
    RAD = Column(Integer)
    MAXHP = Column(Integer)
    last_update = Column(Integer)
    crit = Column(Integer)



    def __str__(self, tgid ,nickname, frac, otryad, zvanie, rang, adena, attack, armor, STR, PSI, RAD, INT, AGIL,MAXHP,last_update, crit):

        self.nickname = nickname
        self.tgid = tgid
        self.frac = frac
        self.otryad = otryad
        self.zvanie = zvanie
        self.rang = rang
        self.adena = adena
        self.attack = attack
        self.armor = armor
        self.PSI = PSI
        self.RAD = RAD
        self.MAXHP = MAXHP
        self.last_update = last_update
        self.crit = crit


    def __repr__(self):
        return "'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'" % \
               (self.tgid, self.nickname, self.frac, self.otryad,self.zvanie,self.rang,self.adena,self.attack,
                self.armor,self.PSI,self.RAD,self.MAXHP,self.last_update, self.crit)




class RockPaper(base):
    __tablename__ = 'RockPaper'

    tgid = Column(Integer, primary_key=True)
    win = Column(Integer)
    lose = Column(Integer)
    dead_heat = Column(Integer)
    total_game = Column(Integer)
    win_rate = Column(Integer)


    def __str__(self, tgid, win, lose, dead_heat, total_game, win_rate):
        self.tgid = tgid
        self.win = win
        self.lose = lose
        self.dead_heat = dead_heat
        self.total_game = total_game
        self.win_rate = win_rate

    def __repr__(self):
        return "'%s','%s','%s','%s','%s','%s'" % (self.tgid, self.win, self.lose, self.dead_heat,self.total_game, self.win_rate)
