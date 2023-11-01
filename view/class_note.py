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
        mess_date = input (fields['mess_date'])
        mess_body = input (fields['mess_body'])
        tags = input (fields['tags'])
        comment = input (fields['comment'])
        return Record(mess_date, mess_body, tags,comment)

    def input_changes(self,message: str,uid:int) -> dict[str,str]:
        print_message(message)
        mess_date = input (fields['mess_date'])
        mess_body = input (fields['mess_body'])
        tags = input (fields['tags'])
        comment = input (fields['comment'])
        uid = uid
        return {'uid':uid,'mess_date':mess_date, 'mess_body':mess_body, 'tags':tags,'comment':comment}

