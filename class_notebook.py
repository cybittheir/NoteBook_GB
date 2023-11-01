import view
import json
from os.path import exists

class NoteBook:

    def __init__(self, path: str):
        self.records: list[view.Record] = []
        self.db_path = path

    def init_base(self,db_path:str):
        if exists(db_path):
            self.open_file(db_path)
        else:
            self.write_file(db_path)
        if len(self.records)==0:
            view.print_message(view.empty_file)
        else:
            view.print_message(view.open_successful(self.records))

    def open_file(self, path):
        with open(path, "r+", encoding = 'UTF-8') as file:
            data = json.load(file)
        if len(data)>0:
            self.records.clear()
            view.Record.count_uid = 0
            for records in data:
                mess_date, mess_body, mess_tags, mess_comment, *_ = data[records]
                date = data[records][mess_date]
                body =  data[records][mess_body]
                tags = data[records][mess_tags]
                comment = data[records][mess_comment]
                self.records.append(view.Record(date, body, tags, comment))

    def write_file(self, path):
        with open(path, "w", encoding = 'UTF-8') as file:
            if len(self.records)>0 :
                print(type(self.rec_to_dict(self.records)))
                json.dump(self.rec_to_dict(self.records),file,indent=4)
                view.print_message(view.save_successful)
            else:
                file.write('')
                view.print_message(view.new_file)

    def dict_to_str(self, book):
        result=""
        for record in book:
            result += record.mess_date.strip() + "|" + record.mess_body.strip() + "|" + record.tags.strip() + "|" + record.comment.strip() + "\n"
        return result

    def rec_to_dict(self,book):
        result = {}
        i = 0
        for record in book:
            result[i] = {"date": record.mess_date.strip(), "message": record.mess_body.strip(), "tags": record.tags.strip(), "comment": record.comment.strip()}
            i += 1
        return result

    def add_record(self, new: dict):
        self.records.append(new)
        view.print_message(view.message_saved(new.mess_body,new.mess_date))

    def search_record(self, word: str) -> list[dict]:
        result=[]
        for record in self.records:
            if word.lower().strip() in str(record).lower().strip():
                result.append(record)
        return result

    def search_id(self, word: int) -> list[dict]:
        result=[]
        for record in self.records:
            if word == record.uid:
                result.append(record)
                break
        return result

    def change_record(self, index: int, new: dict[str,str]):
        print (new)
        for key,field in new.items():
            if field != '':
                match key:
                    case "mess_date":
                        self.records[index].mess_date = field
                    case "mess_body":
                        self.records[index].mess_body = field
                    case "tags":
                        self.records[index].tags = field
                    case "comment":
                        self.records[index].comment = field
