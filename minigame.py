#todo сделать мини игру камень ножници бумага
import random
from datetime import datetime , timedelta
import time
from func import *
from main import *

def knb(call, y):
    future_in_half_hour = datetime.utcnow() + timedelta(hours=3)
    local_time = future_in_half_hour.replace(microsecond=0)
    x = random.randint (1, 5)
    list = {1: 'Камень', 2: 'ножницы', 3:'бумага', 4:'ящерица', 5:'спок'}
    x = list.get(x)

    time.sleep(2)
    if y == x:
      print ("Ничья!")
      minigame_rockpaper_update_gamer_nichiya(call.from_user.id)
      return f'Ничья!\n{local_time}'
    elif y == 'Камень' and x == 'ножницы' or y == 'спок' and x == 'ножницы':
      print ("Вы победили! Ваш противник выбрал ножницы")
      minigame_rockpaper_update_gamer_win(call.from_user.id)
      return f'Вы победили! Ваш противник выбрал ножницы\n{local_time}'
    elif y == 'бумага' and x == 'ножницы' or y == 'ящерица' and x == 'ножницы':
      print ("Вы проиграли! Ваш противник выбрал ножницы")
      minigame_rockpaper_update_gamer_lose(call.from_user.id)
      return f'Вы проиграли! Ваш противник выбрал ножницы\n{local_time}'
    elif y == 'Камень' and x == 'бумага' or y == 'спок' and x == 'бумага':
      print ("Вы проиграли! Ваш противник выбрал бумагу")
      minigame_rockpaper_update_gamer_lose(call.from_user.id)
      return f'Вы проиграли! Ваш противник выбрал бумагу\n{local_time}'
    elif y == 'ящерица' and x == 'бумага' or y == 'ножницы' and x == 'бумага':
      print ("Вы победили! Ваш противник выбрал бумагу")
      minigame_rockpaper_update_gamer_win(call.from_user.id)
      return f'Вы победили! Ваш противник выбрал бумагу\n{local_time}'
    elif y == 'Камень' and x == 'ящерица' or y == 'ножницы' and x == 'ящерица':
      print ("Вы победили! Ваш противник выбрал ящерицу")
      minigame_rockpaper_update_gamer_win(call.from_user.id)
      return f'Вы победили! Ваш противник выбрал ящерицу\n{local_time}'
    elif y == 'бумага' and x == 'ящерица' or y == 'спок' and x == 'ящерица':
      print ("Вы проиграли! Ваш противник выбрал ящерицу")
      minigame_rockpaper_update_gamer_lose(call.from_user.id)
      return f'Вы проиграли! Ваш противник выбрал ящерицу\n{local_time}'
    elif y == 'Камень' and x == 'спок' or y == 'ножницы' and x == 'спок':
      print ("Вы проиграли! Ваш противник выбрал спок")
      minigame_rockpaper_update_gamer_lose(call.from_user.id)
      return f'Вы проиграли! Ваш противник выбрал спок\n{local_time}'
    elif y == 'бумага' and x == 'спок' or y == 'ящерица' and x == 'спок':
      print ("Вы победили! Ваш противник выбрал спок")
      minigame_rockpaper_update_gamer_win(call.from_user.id)
      return f'Вы победили! Ваш противник выбрал спок\n{local_time}'
    elif y == 'ножницы' and x == 'Камень' or y == 'ящерица' and x == 'Камень':
      print ("Вы проиграли! Ваш противник выбрал камень")
      minigame_rockpaper_update_gamer_lose(call.from_user.id)
      return f'Вы проиграли! Ваш противник выбрал камень\n{local_time}'
    elif y == 'бумага' and x == 'Камень':
      print ("Вы победили! Ваш противник выбрал камень")
      minigame_rockpaper_update_gamer_win(call.from_user.id)
      return f'Вы победили! Ваш противник выбрал камень\n{local_time}'
    elif x == 'Камень' and y == 'спок':
      print("Вы проиграли! Ваш противник выбрал камень")
      minigame_rockpaper_update_gamer_lose(call.from_user.id)
      return f'Вы проиграли! Ваш противник выбрал камень\n{local_time}'
    else:
      print(f"Ошибка: Вырбал комп{x}, выбрал пользователь {y}")
      return f'Ошибка: Вырбал комп{x}, выбрал пользователь {y}\n{local_time}'
    #z = input ("Хотите сыграть еще раз (Да или Нет)? ")




text = f"""Привет давай сыграем в 
'🧱Камень ✂️Ножницы 📄Бумага 🦎Ящерица 🖖Спок'
Твоя статистика:
N Побед,
N Проигранно,
N Ничьих
N% Процент побед
#todo Схема игры!
Если первый раз:
/reg_minigame"""
