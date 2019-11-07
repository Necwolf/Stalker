from sqlalchemy import create_engine, Column, String, Integer, Float, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session




engine = create_engine('postgresql+psycopg2://postgres:3365@localhost:5432/postgres',echo=True)
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


    #def __str__(self):
        #return self.telegram_id, self.first_name, self.last_name, self.count_buy, self.balance, self.last, self.last2
    #def __repr__(self):
        #return self.__str__()
    def __str__(self, id, telegram_id, first_name, last_name):
        self.id = id
        self.telegram_id = telegram_id
        self.first_name = first_name
        self.last_name = last_name


    def __repr__(self):
        return "'%s','%s','%s','%s'" % (self.id, self.telegram_id, self.first_name, self.last_name)


class Hero(base):
    __tablename__ = 'Hero'

    #id = Column(Integer, primary_key=True)
    tgid = Column(Integer,primary_key=True)
    nickname = Column(String, nullable=False)
    frac = Column(String)
    otryad = Column(String,nullable=True)
    zvanie = Column(String,nullable=True)
    lvl = Column(Integer)
    adena = Column(Integer)
    attack = Column(Integer)
    armor = Column(Integer)
    STR = Column(Integer)
    PSI = Column(Integer)
    RAD = Column(Integer)
    INT = Column(Integer)
    AGIL = Column(Integer)
    MAXHP = Column(Integer)
    last_update = Column(Integer)


    #def __str__(self):
        #return self.telegram_id, self.first_name, self.last_name, self.count_buy, self.balance, self.last, self.last2
    #def __repr__(self):
        #return self.__str__()
    def __str__(self, tgid ,nickname, frac, otryad, zvanie, lvl, adena, attack, armor, STR, PSI, RAD, INT, AGIL,MAXHP,last_update):

        self.nickname  = nickname
        self.tgid = tgid
        self.frac =frac
        self.otryad =otryad
        self.zvanie =zvanie
        self.lvl =lvl
        self.adena =adena
        self.attack =attack
        self.armor =armor
        self.STR =STR
        self.PSI =PSI
        self.RAD =RAD
        self.INT =INT
        self.AGIL =AGIL
        self.MAXHP = MAXHP
        self.last_update =last_update


    def __repr__(self):
        return "'%s','%s',%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'" % \
               (self.tgid, self.nickname, self.frac, self.otryad,self.zvanie,self.lvl,self.adena,self.attack,
                self.armor,self.STR,self.PSI,self.RAD,self.INT,self.AGIL,self.MAXHP,self.last_update)