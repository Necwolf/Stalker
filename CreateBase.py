from sqlalchemy import create_engine, Column, String, Integer, Float, MetaData,ForeignKey,Table, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model import *


engine = create_engine('postgresql+psycopg2://postgres:3365@localhost:5432/postgres',echo=True)
Session = sessionmaker(bind=engine)
session = Session()



metadata = MetaData()
Hero = Table('Hero', metadata,
                        Column('tgid', Integer,primary_key=True),
                        Column('nickname', String),
                        Column('frac', String),
                        Column('otryad', String,nullable=True),
                        Column('zvanie', String, nullable=True),
                        Column('lvl',Integer),
                        Column('adena', Integer),
                        Column('attack', Integer),
                        Column('armor', Integer),
                        Column('STR', Integer),
                        Column('PSI', Integer),
                        Column('RAD', Integer),
                        Column('INT', Integer),
                        Column('AGIL', Integer),
                        Column('MAXHP',Integer),
                        Column('last_update',Integer))

metadata.create_all(engine)
