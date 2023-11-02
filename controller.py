
from class_notebook import NoteBook
from view import Record
from os.path import exists
import view

def start():
    view.clear()
    nb = NoteBook('notes.json')
    nb.init_base(nb.db_path)
    message = Record()

    while True:
        choice = view.menu()
        match choice:
            case 1:
                message.show_records(nb.search_record(view.input_search(view.search_query)))
            case 2:
                search_index = int(view.input_search_id(view.select_query + view.select_change).strip())
                old_mess = nb.records[search_index].mess_body
                old_date = nb.records[search_index].mess_date

                message.show_records(nb.search_id(search_index))

                message_change = message.input_changes(view.input_change_mess,search_index)
                nb.change_record(search_index,message_change)
 
                message.show_records(nb.search_id(search_index))
                view.print_message(view.message_changed(message_change.get('mess_body') if message_change.get('message') else old_mess, message_change.get('mess_date') if message_change.get('mess_date') else old_date))

            case 3:
                search_index=int(view.input_search_id(view.select_query + view.select_delete).strip())
                old_body = nb.records[search_index].mess_body
                old_date = nb.records[search_index].mess_date

                message.show_records(nb.search_id(search_index))
                nb.records.pop(search_index)

                view.print_message(view.message_deleted(old_body, old_date))
            case 4:
                view.print_title(view.show_all)
                message.show_records(nb.records)
            case 5: # TODO Сортировка по дате
                view.print_title(view.show_all)
                message.show_records(nb.records)
            case 6:
                nb.add_record(message.input_message(view.input_new_mess))
            case 7:
                nb.write_file(nb.db_path)
                nb.init_base(nb.db_path)
            case 8:
                nb.init_base(nb.db_path)
            case 0:
                view.print_message(view.normal_exit)
                break