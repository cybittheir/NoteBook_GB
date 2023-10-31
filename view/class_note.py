from .text import *
from .console import print_message

class Record:

    count_uid = 0

    def __init__(self,lastname: str="", firstname: str="", phone:str="", memo:str=""):
        if len(lastname)>0 or len(firstname)>0:
            self.last_name = lastname
            self.first_name = firstname
            self.phone = phone
            self.comment = memo
            self.uid = Record.count_uid
            Record.count_uid += 1

    def __str__(self) -> str:
        return f'{self.uid} {self.last_name} {self.first_name} {self.phone} {self.comment} '
    
    def show_contacts(self,book: list[dict[str,str]]):
        if book:
            print('='*90)
            print(f'| {"ID":>3} | {fields_name["last_name"]:<{fields_size["last_name"]}}| {fields_name["first_name"]:<{fields_size["first_name"]}}| {fields_name["phone"]:<{fields_size["phone"]}}| {fields_name["comment"]:<{fields_size["comment"]}}|')
            print('='*90)
            for record in book:
                print(f'| {record.uid:>3} | {record.last_name:<{fields_size["last_name"]}}| {record.first_name:<{fields_size["first_name"]}}| {record.phone:<{fields_size["phone"]}}| {record.comment:<{fields_size["comment"]}}|')
            print('='*90)
            print(f'{all_records} {len(book)}')
        else:
            print (book_error)

    def input_contact(self,message: str) -> dict[str,str]:
        print_message(message)
        last_name = input (fields['last_name'])
        first_name = input (fields['first_name'])
        phone = input (fields['phone'])
        comment = input (fields['comment'])
        return Record(last_name, first_name, phone,comment)

    def input_changes(self,message: str,uid:int) -> dict[str,str]:
        print_message(message)
        last_name = input (fields['last_name'])
        first_name = input (fields['first_name'])
        phone = input (fields['phone'])
        comment = input (fields['comment'])
        uid = uid
        return {'uid':uid,'last_name':last_name, 'first_name':first_name, 'phone':phone,'comment':comment}

