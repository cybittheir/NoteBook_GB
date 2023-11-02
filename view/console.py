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
    
