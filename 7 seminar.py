# a,b,c = (int(el) for el in input("Три числа").split())
# №7.1[###]. Дан текстовый csv файл. Разделитель данных #.

# Каждая строка файла представляет собой запись вида ФИО

# Например:

# Иванов#Иван#Иванович

# Петров#Петр#Петрович

# Соколов#Илья#Григорьевич

# 1) Необходимо вывести эти данные на экран построчно в виде:

# Иванов Иван Иванович

# Петров Петр Петрович
#со слешами
# file=open('7seminar.txt',mode='r',encoding='utf 8')
# for el in file:
#     print(el.strip())
# file.close()
#верный
# file = open('7seminar.txt', mode='r', encoding='utf-8')

# list_ = [el.strip().split('#') for el in file]
# print(list_[0][0])#[0] [0] иванов

# file.close()



# 2) записать эти данные в список вида: [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]

# [*] Усложнение. Файл находится в поддиретории data текущей директории. Сформировать путь к нему с использованием

# os.path и pathlib


# from os.path import join,abspath

# datapath=join(".", "семинары")
# filename=join(datapath,'data.txt')
# file = open (filename,mode='r',encoding='utf 8')

# list_ = [el.strip().split('#') for el in file]
# print(list_)

# file.close()
# №7.2[###]. Продолжение предыдущей задачи

# Данные в списке [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]

# необходимо преобразовать к виду:

# Иванов И.И.

# Петров П.П.

# Полученные строки записать в новый файл. Файл должен находиться в поддиретории rezults.
# from os.path import join
# datapath=join(".", "семинары")
# with open(join(datapath, "7seminar.csv"), mode='r', encoding='utf-8') as data_file:
#   data = [line.strip().split('#') for line in data_file]
#     for line in data_file:
#         data.append(line.strip().split('#'))
#         print(line.replace('#','').strip())
# print (data)
#не знаю что
# filename=join(datapath,'data.txt')
# file = open (filename,mode='r',encoding='utf 8')

# list_ = [el.strip().split('#') for el in file]
# print(list_)

# file.close()
#1 вариант
# from os.path import join
# datapath=join(".", "семинары")
# with open(join(datapath, "7seminar.csv"), mode='r', encoding='utf-8') as data_file:
#   data = [line.strip().split('#') for line in data_file]
# new_data=list()

# for fio in data:
#     new_fio=""
# #     for idx, el in enumerate(fio):
        
# #         if idx!=0:
# #             new_fio+=' '+el[0]+'.'
# #         else:
# #             new_fio+=el+' '
# #     new_data.append(new_fio) 
     
# # print (new_data)
# #2 вариант
# from os.path import join
# datapath=join(".", "семинары")
# with open(join(datapath, "7seminar.csv"), mode='r', encoding='utf-8') as data_file:
#   data = [line.strip().split('#') for line in data_file]
# new_data=list()

# for fio in data:
#         new_fio=f"{fio[0]},{fio[1][0]},{fio[2][0]}"
#         new_data.append(new_fio) 
# # new_data2=[f"{fio[0]},{fio[1][0]},{fio[2][0]}"for fio in data] #ниже уже есть оставить ковычки
# new_data2=[f"{surname}{name[0]},{parent[0]}"for surname, name, parent in data]
# # with open(join(datapath,"result","7seminar.csv"), mode='r', encoding='utf-8') as data_file:
# #   [data_file.write(el+"\n") for el in new_data2]
# print (*new_data2, sep="\n")

#vs code
# from pathlib import Path
# from os import getcwd
# from os.path import join, abspath, dirname

# MAIN_DIR_OP1 = abspath(dirname(__file__))
# MAIN_DIR_OP2 = abspath(dirname("."))

# MAIN_DIR_PL1 = Path(__file__).parent
# MAIN_DIR_PL2 = Path(".")

# print(f"текущая директория: {getcwd()}")
# print("PATHLIB")
# print(f"Через __file__: {MAIN_DIR_PL1.absolute()}")
# print(f"Через '.': {MAIN_DIR_PL2.absolute()}")
# print("OS.PATH")
# print(f"Через __file__: {MAIN_DIR_OP1}")
# print(f"Через '.': {MAIN_DIR_OP1}")

#чат сделал
# from os.path import join

# datapath = join(".", "семинары")

# with open(join(datapath, "7seminar.csv"), mode='r', encoding='utf-8') as data_file:
#     data = [line.strip().split('#') for line in data_file]

# new_data = []

# for fio in data:
#     new_fio = ""
#     for idx, el in enumerate(fio):
#         if el:  # Пропустить пустые поля
#             if idx != 0:
#                 new_fio += ' ' + el[0] + '.'
#             else:
#                 new_fio += el + ' '
#     new_data.append(new_fio.strip())  # Удалить начальные и конечные пробелы

# print(new_data)


# # [*] Усложнение. Данные необходимо записать в два разных файла:

# # В первый - в виде Иванов И.И.

# # Во второй - в виде Иванов-И-И

# # [*****] Усложнение. Вам известно, что (в перспективе) подобных спецификаций может быть много. Не две, а пять или десять

# from os.path import join

# datapath = join(".", "семинары")
# filename = join(datapath, "7seminar.csv")

# with open(filename, mode='r', encoding='utf-8') as file:
#    data = [el.strip().split('#') for el in file]
#    new_fio = [f'{surname}{name[0]}.{parent[0]}.' for surname, name, parent in data]

# print(*new_fio)

# resultpath = join('.', 'семинары')
# resultfilename = join(resultpath, "7result.csv")

# with open(resultfilename, mode='w', encoding='utf-8') as file:
#    [file.write(el + '\n') for el in new_fio]
# # Как улучшить свой код в этом случае, сделать его легко расширяемым?
# 
# # №7.3[###]. Имея список вида [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]

# # преобразовать его в списки вида

# 1) ['Иванов-И-И', 'Петров-П-П', 'Соколов-И-Г'...]

# 2) ['Иванов И.И.', 'Петров П.П.', 'Соколов И.Г.'...]

# с использованием Comprehension; Comprehension + функция; Comprehension + lambda; map
# Comprehension
# from os.path import join
# def names():
#      pass
#   # raise NotImplementedError  для более красивого пропускания чем строчка выше
# datapath = join(".", "семинары")
# filename = join(datapath, "7seminar.csv")

# with open(filename, mode='r', encoding='utf-8') as file:
#    data = [el.strip().split('#') for el in file]
#    new_fio = [f'{surname}{name[0]}.{parent[0]}.' for surname, name, parent in data]
# print(*new_fio)

# Comprehension + функция
# from os.path import join
# def names(user_data:list)->str:
#    fio_string=user_data
#    surname,name,parent=user_data
#    return f'{surname}{name[0]}.{parent[0]}.'

   
   
# datapath = join(".", "семинары")
# filename = join(datapath, "7seminar.csv")

# with open(filename, mode='r', encoding='utf-8') as file:
#    data = [el.strip().split('#') for el in file]
#    new_fio = [names(list_data_user) for list_data_user in data]
# print(*new_fio)

# Comprehension + lambda

# from os.path import join

# def names(user_data: list) -> str:
#     fio_string = user_data
#     surname, name, parent = user_data
#     return f'{surname}{name[0]}.{parent[0]}.'

# def names_lambda(surname: str, name: str, parent: str) -> str:
#     return f'{surname}{name[0]}.{parent[0]}.'

# datapath = join(".", "семинары")
# filename = join(datapath, "7seminar.csv")

# with open(filename, mode='r', encoding='utf-8') as file:
    
#     data = [el.strip().split('#') for el in file]
#     new_fio=[(lambda surname,name,parent:f'{surname}{name[0]}.{parent[0]}.')(surname,name,parent) for surname,name,parent in data]
    
#    #  new_fio = [names_lambda(*list_data_user) for list_data_user in data] 1 вариант
   


# print(*new_fio)

# map
# from os.path import join

# def names_comprehention_one(user_data: list) -> str:
#     fio_string = user_data
#     surname, name, parent = user_data
#     return f'{surname}{name[0]}.{parent[0]}.'

# def names_comprehention_two(surname: str, name: str, parent: str) -> str:
#     return f'{surname}{name[0]}.{parent[0]}.'

# datapath = join(".", "семинары")
# filename = join(datapath, "7seminar.csv")

# with open(filename, mode='r', encoding='utf-8') as file:
    
#     data = [el.strip().split('#') for el in file]
#     new_fio = [*map (names_comprehention_one, data)]
    
#    #  new_fio = [names_lambda(*list_data_user) for list_data_user in data] 1 вариант
   


# print(*new_fio)
# print(type(new_fio))


# [**] Усложнение. Дополнить обработку списка условием: Выбираем только те элементы, в которых первая буква П

# №7.4[49]. Напишите функцию same_by(func, objects)

# которая проверяет, все ли элементы в objects дают одинаковое значение характеристики func

# Аргументы:

# func - функция одного аргумента.

# objects - список или кортеж

# Возвращаемое значение:

# - Если objects пустой, вернуть None

# - Если все элементы в objects дают одинаковое значение func, вернуть True, иначе вернуть False

# Примеры/Тесты:

# same_by(lambda x: x % 2, [1, 2, 10, 12]) -> False

# same_by(lambda x: x % 2, [0, 2, 10, 12]) -> True

# same_by(len, ["qw", "er", "ty", "ui", "op", "as", "df", "gh"]) -> True

# same_by(len, ["qw", "er1", "ty", "ui", "op", "as", "df", "gh"]) -> False

# same_by(max, ["qw", "er1", "ty", "ui", "op", "as", "df", "gh"]) -> False

# same_by(max, ["qz", "zr1", "tz", "zi", "oz", "zs", "dz", "zh"]) -> True

# same_by(lambda x: x[0], ["qz", "zr1", "tz", "zi", "oz", "zs", "dz", "zh"]) -> False

# same_by(lambda x: x[0], ["qz", "qr1", "qz", "qi", "qz", "qs", "qz", "qh"]) -> True

# [*] Усложнение. Не используйте цикл в функции

# def same_by(func, objects):
#    if len(objects)==0: return None
#    for idx in range(len(objects)):
#       if func(objects[idx])!=func(objects[idx-1]): return False
#    return True

# print(same_by(lambda x: x % 2, [0, 2, 10, 12]))


# [*] Усложнение. Не используйте цикл в функции
def same_by(func, objects):
   if len(objects)==0: return None
   if len(set(map(func,objects)))==1:return True
   return False

print(same_by(lambda x: x % 2, [1, 2, 10, 12]))