
from class_notebook import NoteBook
from view import Record
from os.path import exists
import view

def start():
    view.clear()
    nb = NoteBook('notes.txt')
    nb.init_base(nb.db_path)
    message = Record()

    while True:
        choice = view.menu()
        match choice:
            case 1:
                message.show_contacts(nb.search_contact(view.input_search(view.search_query)))
            case 2:
                search_index = int(view.input_search_id(view.select_query + view.select_change).strip())
                old_lname = nb.contacts[search_index].last_name
                old_fname = nb.contacts[search_index].first_name

                message.show_contacts(nb.search_id(search_index))

                contact_change = message.input_changes(view.input_change_contact,search_index)
                nb.change_contact(search_index,contact_change)
 
                message.show_contacts(nb.search_id(search_index))
                view.print_message(view.contact_changed(contact_change.get('message') if contact_change.get('message') else old_lname, contact_change.get('first_name') if contact_change.get('first_name') else old_fname))

            case 3:
                search_index=int(view.input_search_id(view.select_query + view.select_delete).strip())
                old_lname = nb.contacts[search_index].last_name
                old_fname = nb.contacts[search_index].first_name

                message.show_contacts(nb.search_id(search_index))
                nb.contacts.pop(search_index)

                view.print_message(view.contact_deleted(old_lname, old_fname))
            case 4:
                view.print_title(view.show_all)
                message.show_contacts(nb.contacts)
            case 5:
                nb.add_contact(message.input_contact(view.input_new_contact))
            case 6:
                nb.write_file(nb.db_path)
                nb.init_base(nb.db_path)
            case 7:
                nb.init_base(nb.db_path)
            case 0:
                view.print_message(view.normal_exit)
                break