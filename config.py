import os

TOKEN = '<TOKEN>'
#данные для базы
dblogin = '<LOGIN>'
dbpsw = '<PASS>'
dbhost = '<HOST>'
db = "<DBNAME>"
#KEY_DATABASE = os.getenv("DATABASE_URL")
DATABASE = f'postgresql+psycopg2://{dblogin}:{dbpsw}@{dbhost}:5432/{db}'

#Операторы
operators =[188539449,657633129]

 #Чаты Банд

tryasi = -1001338670018  # Трячи Шатай!
wolf = -1001483645531  # Волчий отряд
suicide = -1001434598079  # Отряд самоубитц

 #Читаймые каналы

channel_read = [-1001360694345, -1001470701250, -1001171584711]
group_frwd_channel = [tryasi, wolf, suicide]


# URL webhookset
