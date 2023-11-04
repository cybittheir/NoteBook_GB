from .text import *
import os
import view

clear = lambda: os.system('cls')

def menu() -> int:

    print(main_menu)

    while True:
        choice = input(menu_choice)
        clear()
        if choice.isdigit() and 0 <= int(choice) <= 8:
            return int(choice)
        print (input_error)
        print (main_menu)

def f_menu() -> int:
    print(file_menu)
    while True:
        choice = input(menu_choice)
        clear()
        if choice.isdigit() and (7 <= int(choice) <= 8 or int(choice) == 0):
            return int(choice)
        print (input_fm_error)
        print (file_menu)


def input_search(message: str) -> str:
    return input(message)

def input_search_id(message: str) -> str:
    while True:
        choice = input(message)
        clear()
        if choice.isdigit() and 0 <= int(choice) < view.Record.count_uid:
            return choice
        print (search_id_error + str(view.Record.count_uid - 1) + '!')

def get_message_width(message: str) -> int:
    mess_list=message.split('\n')
    max = 0
    for st in mess_list:
        if max < len(st):
            max = len(st)
    return max

def print_message(message: str):
    length = get_message_width(message) + 1
    print ('\n' + '='*length)
    print (message)
    print ('='*length)

def print_title(message: str):
    length = get_message_width(message) + 1
    print ('\n' + '='*90)
    print ('| ' + message +  ' '*(90 - length - 2) + '|')
    
def date_to_intstr(rec_date: str) -> int:
    dates = rec_date.split('/')
    if len(dates[2]) == 1:
        dates[2] = "0" + dates[2]
    if len(dates[1]) == 1:
        dates[1] = "0" + dates[1]
    if len(dates[0]) == 1:
        dates[0] = "0" + dates[0]
    result = int(dates[2] + dates[1] + dates[0])
    return str(result)

def str_to_datestr(rec_date: str) -> str:
    d_year = int(rec_date)//10000
    d_month = (int(rec_date)//100)%100
    d_date = int(rec_date)%100
    if d_date <10:
        str_date = "0" + str(d_date)
    else:
        str_date = str(d_date)
    if d_month <10:
        str_month = "0" + str(d_month)
    else:
        str_month = str(d_month)
    if d_year <10:
        str_year = "0" + str(d_year)
    else:
        str_year = str(d_year)

    result = str_date + "/" + str_month + "/" + str_year
    return result

def check_date(date:str):
    date_list=date.split('/')
    if len(date_list) == 3 and date_list[0].isdigit() and date_list[1].isdigit() and date_list[2].isdigit():
        if (int(date_list[2]) > 0 and int(date_list[2]) < 100 and int(date_list[1]) > 0 and int(date_list[1]) < 13 and int(date_list[0]) > 0 and int(date_list[0]) < 32):
            if int(date_list[1]) == 2 and (2000 + int(date_list[2]))%4 == 0 and int(date_list[0]) < 30:
                return True
            elif int(date_list[1]) == 2 and (2000 + int(date_list[2]))%4 > 0 and int(date_list[0]) < 29:
                return True
            elif (int(date_list[1]) == 1 or int(date_list[1]) == 3 or int(date_list[1]) == 5 or int(date_list[1]) == 7 or int(date_list[1]) == 8 or int(date_list[1]) == 10 or int(date_list[1]) == 12) and int(date_list[0]) < 31:
                return True
            elif (int(date_list[1]) == 4 or int(date_list[1]) == 6 or int(date_list[1]) == 9 or int(date_list[1]) == 11) and int(date_list[0]) < 31:
                return True
    print ("Ошибка вводы даты. Используйте формат ДД/ММ/ГГ")
    return False
