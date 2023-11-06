from .text import *
from .console import print_message,date_to_intstr,str_to_datestr,check_date

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
                print(f'| {record.uid:>3} | {str_to_datestr(record.mess_date):<{fields_size["mess_date"]}}| {record.mess_body:<{fields_size["mess_body"]}}| {record.tags:<{fields_size["tags"]}}| {record.comment:<{fields_size["comment"]}}|')
            print('='*tab_size)
            print(f'{all_records} {len(book)}')
        else:
            print (book_error)

    def sort_by_date(self,book: list[dict[str,str]]):
        # вариант сделать сортировку в show_records рассматривался (добавление входного параметра и т.д.), но в данном случае пожалел время.
        if book:
            tab_size = int(fields_size["mess_date"]) + int(fields_size["mess_body"]) + int(fields_size["tags"]) + int(fields_size["comment"]) + 15
            print('='*tab_size)
            print(f'| {"ID":>3} | {fields_name["mess_date"]:<{fields_size["mess_date"]}}| {fields_name["mess_body"]:<{fields_size["mess_body"]}}| {fields_name["tags"]:<{fields_size["tags"]}}| {fields_name["comment"]:<{fields_size["comment"]}}|')
            print('='*tab_size)
            tmp_book= {}
            for record in book:
                old_index = str(record.uid)
                while len(old_index) < len(str(Record.count_uid)):
                    old_index = "0" + old_index
                index = str(record.mess_date) + "." + old_index
                list_tmp = (f'| {record.uid:>3} | {str_to_datestr(record.mess_date):<{fields_size["mess_date"]}}| {record.mess_body:<{fields_size["mess_body"]}}| {record.tags:<{fields_size["tags"]}}| {record.comment:<{fields_size["comment"]}}|')
                tmp_book[index] = str(list_tmp)
            sorted_book = dict(sorted(tmp_book.items()))
            for rec in sorted_book:
                print(sorted_book[rec])
            print('='*tab_size)
            print(f'{all_records} {len(book)}')


    def input_message(self,message: str) -> dict[str,str]:
        print_message(message)
        today = date.today().strftime("%d/%m/%y")
        right_date = False
        while right_date == False:
            mess_date_in = input (fields['mess_date'] + today + ' : ')
            if mess_date_in == "":
                mess_date_in = today
            right_date = check_date(mess_date_in)
        mess_date = date_to_intstr(mess_date_in)
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
        while right_date == False:
            mess_date_in = input (fields['mess_date'] + "не изменилась:")
            if mess_date_in == "":
                right_date = True
            else:
             right_date = check_date(mess_date_in)
        mess_date = date_to_intstr(mess_date_in)
        mess_body = input (fields['mess_body'])
        tags = input (fields['tags'])
        comment = input (fields['comment'])
        uid = uid
        return {'uid':uid,'mess_date':mess_date, 'mess_body':mess_body, 'tags':tags,'comment':comment}


