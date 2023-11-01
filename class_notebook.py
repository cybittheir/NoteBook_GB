import view
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
            data = file.readlines()
        if len(data)>0:
            self.records.clear()
            view.Record.count_uid = 0
            for contact in data:
                mess_date, mess_body, tags, comment, *_ = contact.strip().split('|')
                self.records.append(view.Record(mess_date, mess_body, tags, comment))

    def write_file(self, path):
        with open(path, "w", encoding = 'UTF-8') as file:
            if len(self.records)>0 :
                file.write(self.dict_to_str(self.records))
                view.print_message(view.save_successful)
            else:
                file.write('')
                view.print_message(view.new_file)

    def dict_to_str(self, book):
        result=""
        for record in book:
            result += record.mess_date.strip() + "|" + record.mess_body.strip() + "|" + record.tags.strip() + "|" + record.comment.strip() + "\n"
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
