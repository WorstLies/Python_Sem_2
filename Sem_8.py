# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу\n")
    choice = int (input("Введите номер действия: "))
    return choice

def Work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phone.txt')
    while (choice != 7):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            name = get_search_name()
            print(find_by_name(phone_book, name))
        elif choice == 3:
            number = get_search_number()
            print(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_txt('phone.txt', phone_book)
        elif choice == 5:
            file_name = get_file_name()
            write_txt(file_name, phone_book)
        elif choice==6:
            new_data = del_user(phone_book)
            write_txt(new_data, phone_book)
        choice = show_menu()


def read_txt (filename):
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open (filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(",")))
            data.append(record)
    return data

def get_search_name():
    return input("Введите фамилию для поиска: ") 

def get_search_number():
    return input("Введите телефон для поиска: ")

def get_new_user():
    a = input("Введите фамилию нового абонента: ")
    b = input("Введите имя нового абонента: ")
    c = input("Введите номер нового абонента: ")
    d = input("Введите описание нового абонента: ")
    return f'{a},{b},{c},{d}'

def add_user(data: list, user_data: str):
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    record = dict(zip(fields, user_data.split(',')))
    data.append(record)

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as sfile:
        for i in range(len(phone_book)):
            s =''
            for v in phone_book[i].values():
                s += v + ','
            sfile.write(f'{s[:-1]}\n')
        print(phone_book, file=sfile)

def get_file_name():
    file_name = input("Введите название: ")
    return file_name

def print_result(data: list):
    for el in data:
        s =''
        for v, k in el.items():
            s += f'{v}: {k}\n'
        print(s)
    print(data)

def Write_txt(filename: str, data: list):
   with open(filename, "w", encoding="utf-8") as fout:
       for i in range(len(data)):
           s =''
           for v in data[i].values():
               s += v+','
           fout.write(f'{s[:-1]}\n')   

def find_by_name(data: list, name):
    for j in data:
        if j.get("Фамилия") == name:
            return j.get ("Телефон")
        else :
            return ("Такого абонента нет!")
        
def find_by_number(data: list, number):
    for j in data:
        if j.get("Фамилия") == number:
            return j.get ("Телефон")
        else:
            return ("Такого абонента нет!")

def del_user(data: list):
    print("Какую именно запись по счету Вы хотите удалить?")
    number_journal = int(input('Введите номер записи: '))
    data.pop(number_journal-1)
    print(data)

Work_with_phonebook()