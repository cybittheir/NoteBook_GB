from datetime import date

# TODO  сортировка данных по дате


main_menu='''
=====================================
| Главное меню                      |
|===================================|
| -> 1. Найти заметку               |
| -> 2. Изменить заметку            |
| -> 3. Удалить заметку             |
| -> 4. Показать все заметки        |
| -> 5. Сортировать по дате         |
| -> 6. Создать заметку             |
| -> 7. Сохранить файл книги        |
| -> 8. Перечитать файл книги       |
| -> 0. Выход                       |
=====================================
'''

file_menu='''
=====================================
| Файл книги                        |
|===================================|
| -> 7. Сохранить файл              |
| -> 8. Перечитать файл (Отмена)    |
| -> 0. Выход                       |
=====================================
'''

menu_choice = 'Выберите пункт меню: '
input_error = 'Некорректный ввод! Введите от 0 до 8 включительно'
input_fm_error = 'Некорректный ввод! Введите от 0, 7 или 8'
search_id_error = 'Некорректный ввод! Введите номер ID от 0 до '
book_error = 'Записная книга пуста или ошибка файла книги'


input_new_mess = "Введите данные новой записи"
input_change_mess = "Введите измененные данные записи"
empty_file = "Внимание!!!\nФайл записной книги пуст.\nДобавьте первую запись -> 5"
save_successful = "Файл книги успешно сохранен"
new_file = "Пустой файл книги успешно создан"
normal_exit = "Спасибо за использование записной книжки"

all_records = "Всего записей: "
search_query = "Введите дату записи: "
select_query = "Введите ID записи для "
select_change = "изменения: "
select_delete = "удаления: "

fields={}
fields['mess_body']='Введите текст записи: '
fields['mess_date'] = 'Введите дату записи (ДД/ММ/ГГ) или нажмите Enter если дата '
fields['tags'] = 'Введите ключевые слова: '
fields['comment'] = 'Введите комментарий: '

fields_name={}
fields_name['mess_body']='Записка'
fields_name['mess_date']='Дата'
fields_name['tags']='Тэги'
fields_name['comment']='Примечание'

fields_size={}
fields_size['mess_body']=110
fields_size['mess_date']=10
fields_size['tags']=30
fields_size['comment']=50

show_all = "Все записки"

def open_successful(note_book: list):
    return f'Файл книги успешно прочитан\nИндексы обновлены!!!\n{all_records}{len(note_book)}'

def message_saved(mess_body: str, mess_date: str):
    return f'Запись {mess_date}: {mess_body} добавлена.\nДля сохранения в файл -> 7\nДля отмены -> 8 (Перечитать файл книги)'

def message_changed(mess_body: str, mess_date: str):
    return f'Запись {mess_date}: {mess_body} изменена.\nДля сохранения изменений в файл -> 7\nДля отмены -> 8 (Перечитать файл книги)'

def message_deleted(mess_body: str, mess_date: str):
    return f'Запись {mess_date}: {mess_body} удалена.\nДля сохранения изменений в файл -> 7\nДля отмены -> 8 (Перечитать файл книги)'

def message_error(mess_body: str, mess_date: str):
    return f'Ошибка! Запись {mess_body} от {mess_date} не добавлена в справочник'
