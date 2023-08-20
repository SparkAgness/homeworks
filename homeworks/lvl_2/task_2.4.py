# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    scpy = ''
    for c in s:
        if '!' == c:
            pass
        else:
            scpy += c
    return scpy
        


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    if (s.rfind('!') == (len(s) - 1)):
        return s[:-1]
    else:
        return s
    



# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    s_list = s.split(' ') #creates list for splitted string
    remove_list = []      #creates list for strings with one "!"
    for i in range(len(s_list)):
        if (s_list[i].count('!') == 1):
            remove_list.append(s_list[i]) #appends to remove_list strings with one "!"
    for rem in remove_list:
        s_list.remove(rem) #removes the strings
    if (len(s_list) == 0):
        return ' ' #in case with empty s_list, returns empty string to cout
    else:            
        return ' '.join(s_list) 



str_list = ['Hi!', 'Hi! Hi!','Hi! Hi! Hi!', 'Hi Hi! Hi!', 'Hi! !Hi Hi!', 'Hi! Hi!! Hi!', 'Hi! !Hi! Hi!']
for str in str_list:
    print(f'remove_exclamation_marks - {remove_exclamation_marks(str)}')
for str in str_list:
    print(f'remove_last_em - {remove_last_em(str)}')
for str in str_list:
    print(f'remove_word_with_one_em - {remove_word_with_one_em(str)}')