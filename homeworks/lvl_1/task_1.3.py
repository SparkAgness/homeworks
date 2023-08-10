# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

m_number = int(input("Введите номер месяца: "))
match m_number:
    case 1: 
        month = "январь"
        days = 31
        flag = 1
    case 2:
        month = "февраль"
        days = 28
        flag = 0
    case 3:
        month = "март"
        days = 31
        flag = 1
    case 4:
        month = "апрель"
        days = 30
        flag = 0
    case 5:
        month = "май"
        days = 31
        flag = 1
    case 6:
        month = "июнь"
        days = 30
        flag = 0
    case 7:
        month = "июль"
        days = 31
        flag = 1
    case 8:
        month = "август"
        days = 31
        flag = 1
    case 9:
        month = "сентябрь"
        days = 30
        flag = 0
    case 10:
        month = "октябрь"
        days = 31
        flag = 1
    case 11:
        month = "ноябрь"
        days = 30
        flag = 0
    case 12:
        month = "декабрь"
        days = 31
        flag = 1
    case _:
        print('Такого месяца нет!')


if 13 > m_number > 0:
    if flag:
        print(f"Вы ввели {month}. {days} день")
    if not flag:
        print(f"Вы ввели {month}. {days} дней")
    










