#создать справочник c возможжностью импорта и экспорта данных в формате .csv
#информация о человеке:
#Фамилия, имя, телефон, описание 
#корректность и уникальность данных не обязательны
#Функционал программы:
#1)телефонный справочник хранится в памяти в процессе выполнения кода
#выберите наиболее удобную структуру даннных для хранения справочника
#2) CRUD:Create, read,update, delete
#Create:создание новой записи в справочнике : ввод всех полей новой записи, занесение ее в справочник
#REad: он же select выбор записей, удовлетворяющих заданному фильтру:по первой части фамилии человека.Берем первое совпадение по фамилии.
#update:изменение полей выранной части. выбор записи как и read, заполнение новыми значениями
#delite:удаление записи из справочника. Выбор как в REad.
#3) экспорт данных в текстовый файл формата csv
#4) импорт данных в текстовый файл формата csv
#используйте функции для реализации значимых действий в программе

#1словарь из списка fio={'Иванов иван':[897897,'работник'], 'Петров Петр':[35346,'неработник']}

#2 список из словарей:
#fio=[{'Иванов иван':[897897,'работник']},{'Петров Петр':[35346,'неработник']}]

#3 список из словарей
#fio =[{1:["Иванов", "Иван","89234145", "работник"]}]

#4 словарь из словарей СО списком
#fio ={{1:["Иванов", "Иван","89234145", "работник"]}}

#5 список из словарей:
#fio=[{'surname':"Иванов", 'name':"Иван",'number':"89234145", 'discription':"работник"}]

#6 словарь из словарей
#1 вариант
# phonebook={}
# phonebook_last_id=0
# fio =[{1:{'surname':"Иванов", 'name':"Иван",'phone':"89234145", 'discription':"работник"}}] 
# def create (db:dict, id:int, surname:str, name:str, phone:str, discrip:str) ->tuple:#data_base
#     db[id]={'surname':surname,'name':name,'phone':phone,'discrip':discrip}
#     id+=1
#     return db,id
# def read(surname_filter:str)->int:
#     raise NotImplementedError 
# def get_user_data()->tuple():
#     surname=input("Введите фамилию-")
#     name=input("имя-")
#     phone=input("Введите телефон-")
#     discrip=input("Введите описание-")
#     return surname, name, phone, discrip

# def print_data(db:dict)->None:
#     for id, data in db.items():
#         print(f"[{id}:{data[surname]} | {data[name]}|{data[phone]}|{data[discrip]}|]")
 

# def menu(db:dict,last_id:int)->None:
#     print('введите действие')
#     print('1 создать аккаунт')
#     print('2 ввести имеющиеся данные')
#     print('3 выход')
#     while True:
#         user_input=input('Введите действие>')
#         if user_input=='1':
#             record=get_user_data()
#             db,last_id=create(db,last_id,*record)
#         elif user_input=='2':
#             print_data(db)
#         elif user_input=='3':
#             break
# menu(phonebook, phonebook_last_id)           

#код из чата gpt
phonebook = {}
phonebook_last_id = 0
fio =[{1:{'surname':"Иванов", 'name':"Иван",'phone':"89234145", 'discrip':"работник"}}] 
def create(db: dict, id: int, surname: str, name: str, phone: str, discrip: str) -> tuple:
    db[id] = {'surname': surname, 'name': name, 'phone': phone, 'discrip': discrip}
    id += 1
    return db, id

def read(db: dict, surname_filter: str) -> int:
    for _id in db:
        if surname_filter.lower() in db[_id]['surname'].lower():
            return _id
def print_record(db: dict, found_id: int):
    if found_id is not None:
        print(f'{db[found_id]}')
    else:
        print("Контакт не найден.")
# из урока
# def print_record(db:dict, _id:int):
    # print(f'{db[_id]}')

def get_user_data() -> tuple:
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    discrip = input("Введите описание: ")
    return surname, name, phone, discrip
def get_surname()->str:
    surname=input("Введите фамилию>")
    return surname

def print_data(db:dict)->None:
    for _id, data in db.items():
        print(f"[{_id}:{data['surname']} | {data['name']}|{data['phone']}|{data['discrip']}|]")
#3 экспорт данных в текстовой файл формата csv
def export_db(db:dict,filepath:str)->None:
    with open(filepath, "w",encoding='utf 8') as file:
        for _id, data in db.items():
           file.write(f"{data['surname']},{data['name']},{data['phone']},{data['discrip']}\n")
        #    Для #file.write(f"{data['surname']}{delimeter}{data['name']}{delimeter}{data['phone']}{delimeter}{data['discrip']}\n")
   
# 4 импорт данных из текстового формата csv по гикбрейнс 1 вариант
def import_db(db:dict, last_id:int, filepath:str)->tuple:
#Для #_ def import_db(db:dict, last_id:int, filepath:str, delimeter:str)->tuple:
    last_id=0
    with open(filepath, "r",encoding='utf 8') as file:
        for line in file:
            # Для #_data=line.strip().split(delimeter)
            _data=line.strip().split(',')
            db[last_id]={'surname':_data[0],'name':_data[1],'phone':_data[2],'discrip':_data[3]}
            last_id+=1
    return db,last_id
# 4 импорт данных из текстового формата csv по gpt 2 вариант
# def import_db(db: dict, filepath: str) -> tuple:
#     last_id = 0
#     with open(filepath, "r", encoding='utf-8') as file:
#         for line in file:
#             _data = line.split(',')
#             db[last_id] = {'surname': _data[0], 'name': _data[1], 'phone': _data[2], 'discrip': _data[3]}
#             last_id += 1
#     print("Данные импортированы успешно.")  # Добавьте этот вывод для отладки.
#     return db, last_id

def get_file_name()->str:
    return input('введите имя файла')

def menu(db: dict, last_id: int) -> None:
    
    while True:
        print('Введите действие: ')
        print('1 - создать аккаунт: ')
        print('2 - ввести имеющиеся данные: ')
        print('3 - экспортировать данные: ')
        print('4 - импортировать данные: ')
        print('5 - найти контакт: ')
        print('6 - выход: ')
        user_input = input('Введите действие: ')

        if user_input == '1':
            record = get_user_data()
            db, last_id = create(db, last_id, *record)
        elif user_input == '2':
            print(db)
        elif user_input == '3':
            export_db(db, get_file_name())
        elif user_input == '4':
            db,last_id=import_db(db, last_id, get_file_name())
            # для определенного файла
            # db,last_id=import_db(db, last_id,'data_08_1.txt')
        elif user_input == '5':
            #  found_id=read(db,get_surname) 
            #  чат gpt
            surname_to_search = get_surname()
            found_id = read(db, surname_to_search)
            print_record(db,found_id)          
        elif user_input == '6':
            break

menu(phonebook, phonebook_last_id)
# не могу сохранить