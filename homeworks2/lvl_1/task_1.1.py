# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
count = my_favorite_songs.find(',') #count for find()
rcount = my_favorite_songs.rfind(',') + 2 #count for rfind() (+2 is for stepping across ', ')
print(my_favorite_songs[:count]) #prints 1st song
print(my_favorite_songs[rcount:]) #prints last song
count2 = my_favorite_songs[count + 1:].find(',') #considers border of 2nd tittle
count += 2 #steps across ', '
count2 += count - 1 #steps across 1st tittle
print(my_favorite_songs[count:count2]) #prints 2nd tittle
rcount2 = my_favorite_songs[:rcount - 2].rfind(',') + 2 #finds border of next-to-last tittle
rcount -= 2 #steps across last ', '
print(my_favorite_songs[rcount2:rcount]) #prints next-to-last tittle


# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.
