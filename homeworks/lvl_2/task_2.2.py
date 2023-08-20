# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

month = {
#just dict
    1 : 'январь',
    2 : 'февраль',
    3 : 'март',
    4 : 'апрель',
    5 : 'май',
    6 : 'июнь',
    7 : 'июль',
    8 : 'август',
    9 : 'сентябрь',
    10 : 'октябрь',
    11 : 'ноябрь',
    12 : 'декабрь'
} 

def quarter_of(month):
    number = int(input('Enter the month\'s number '))
    match number:
        case 1:
            print(f'месяц {number} ({month[number]}) является частью первого квартала')
        case 2:
            print(f'месяц {number} ({month[number]}) является частью первого квартала')
        case 3:
            print(f'месяц {number} ({month[number]}) является частью первого квартала')
        case 4:
            print(f'месяц {number} ({month[number]}) является частью второго квартала')
        case 5:
            print(f'месяц {number} ({month[number]}) является частью второго квартала')
        case 6:
            print(f'месяц {number} ({month[number]}) является частью второго квартала')
        case 7:
            print(f'месяц {number} ({month[number]}) является частью третьего квартала')
        case 8:
            print(f'месяц {number} ({month[number]}) является частью третьего квартала')
        case 9:
            print(f'месяц {number} ({month[number]}) является частью третьего квартала')
        case 10:
            print(f'месяц {number} ({month[number]}) является частью четвертого квартала')
        case 11:
            print(f'месяц {number} ({month[number]}) является частью четвертого квартала')
        case 12:
            print(f'месяц {number} ({month[number]}) является частью четвертого квартала')
        case _:
            print('You entered incorrect number! Try again, please...')
            quarter_of(month)



quarter_of(month)

