# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
import random
from datetime import timedelta

duration = timedelta(minutes=0, seconds=0)

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

for i in range(3):
    random.shuffle(my_favorite_songs)
    min_duration = int(my_favorite_songs[0][1])
    sec_duration = int(100*(my_favorite_songs[0][1] - float(min_duration)))
    song_duration = timedelta(minutes=min_duration, seconds=sec_duration)    
    duration += song_duration    
print(f'Three songs\' duration is {duration.seconds//60}')

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

duration = timedelta(minutes=0, seconds=0)
song_dur = []
for value in my_favorite_songs_dict.values():
    song_dur.append(value)
for i in range(3):
    random.shuffle(song_dur)
    min_duration = int(song_dur[1])
    sec_duration = int(100*(song_dur[1] - float(min_duration)))
    song_duration = timedelta(minutes=min_duration, seconds=sec_duration)    
    duration += song_duration    
print(f'Three songs\' duration is {duration.seconds//60}')
# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 


#3d edition without datetime
min_duration = 0
sec_duration = 0
min_value = 0
sec_value = 0
for cou in range(3):
    i = random.randint(0, len(song_dur)- 1)
    min_duration = int(song_dur[i])
    sec_duration = int(song_dur[i] - float(min_duration))*100
    min_value += min_duration
    sec_value += sec_duration
    if sec_value >= 60:
        min_value += 1
        sec_value -= 60
print(f'Any random three songs duration is {min_value}')
 