from .text import *
from .console import print_message

class Record:

    count_uid = 0

    def __init__(self,mdate: str="", message: str="", tags:str="", memo:str=""):
        if len(mdate)>0 or len(message)>0:
            self.mess_date = mdate
            self.mess_body = message
            self.tags = tags
            self.comment = memo
            self.uid = Record.count_uid
            Record.count_uid += 1

    def __str__(self) -> str:
        return f'{self.uid} {self.mess_date} {self.mess_body} {self.tags} {self.comment} '
    
    def show_records(self,book: list[dict[str,str]]):
        if book:
            tab_size = int(fields_size["mess_date"]) + int(fields_size["mess_body"]) + int(fields_size["tags"]) + int(fields_size["comment"]) + 15
            print('='*tab_size)
            print(f'| {"ID":>3} | {fields_name["mess_date"]:<{fields_size["mess_date"]}}| {fields_name["mess_body"]:<{fields_size["mess_body"]}}| {fields_name["tags"]:<{fields_size["tags"]}}| {fields_name["comment"]:<{fields_size["comment"]}}|')
            print('='*tab_size)
            for record in book:
                print(f'| {record.uid:>3} | {record.mess_date:<{fields_size["mess_date"]}}| {record.mess_body:<{fields_size["mess_body"]}}| {record.tags:<{fields_size["tags"]}}| {record.comment:<{fields_size["comment"]}}|')
            print('='*tab_size)
            print(f'{all_records} {len(book)}')
        else:
            print (book_error)

    def input_message(self,message: str) -> dict[str,str]:
        print_message(message)
        today = date.today().strftime("%d/%m/%y")
        right_date = False
        while right_date == False:
            mess_date = input (fields['mess_date'] + today + ' : ')
            if mess_date == "":
                mess_date = today
            right_date = self.check_date(mess_date)
        mess_body = ""
        while len(mess_body) == 0:
            mess_body = input (fields['mess_body'])
            if len(mess_body) == 0:
                print ("Заметка с пустой записью недопустима. Повторите ввод.")
        tags = input (fields['tags'])
        comment = input (fields['comment'])
        return Record(mess_date, mess_body, tags,comment)

    def input_changes(self,message: str,uid:int) -> dict[str,str]:
        print_message(message)
        mess_date = input (fields['mess_date'] + "не изменилась:")
        mess_body = input (fields['mess_body'])
        tags = input (fields['tags'])
        comment = input (fields['comment'])
        uid = uid
        return {'uid':uid,'mess_date':mess_date, 'mess_body':mess_body, 'tags':tags,'comment':comment}

    def check_date(self,date:str):
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

