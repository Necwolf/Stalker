from telebot.types import *




key = ReplyKeyboardMarkup(resize_keyboard=True)
key.row ('📁Профиль')



KNB = InlineKeyboardMarkup( )
KNB.add(InlineKeyboardButton('Камень', callback_data= 'Камень'),InlineKeyboardButton('ножницы', callback_data= 'ножницы'),InlineKeyboardButton('бумага', callback_data= 'бумага'),InlineKeyboardButton('ящерица', callback_data= 'ящерица'),InlineKeyboardButton('спок', callback_data= 'спок'))
KNB.add(InlineKeyboardButton('Статистика игр', callback_data= 'cb_stat'),InlineKeyboardButton('Выход', callback_data= 'cb_exit'))
