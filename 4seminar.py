# №4.1[25]. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.

# Количество повторов добавляется к символам с помощью постфикса формата _n.

# Примеры/Тесты:

# Input: a a a b c a a d c d d

# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Input: a b c d a a a a a a a

# Output: a b c d a_1 a_2 a_3 a_4 a_5 a_6 a_7

# Строку не обязательно вводить с клавиатуры

# string_="a a a b c a a d c d d"
# new_list=string_.split(" ")
# new_set=set(new_list)
# dict_={}
# dict_=dict_.fromkeys(new_set,0)
# new_string=""
# for element in new_list:
#     if dict_[element]==0:
    
#         new_string+=f"{element} "
#     else :
#         new_string+=f"{element}_{dict_[element]} "
#     dict_[element]+=1    
    
        
# print(new_string)

# №4.2[27]. Дана строка, состоящая из слов. Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов.

# Слово не зависит от регистра написания букв.

# Определите, сколько различных слов содержится в этом тексте.

# Примеры/Тесты:

# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

# Output: 14

# Input: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur a tellus ut arcu gravida porta eget a lacus. Curabitur ornare varius turpis, ultricies mollis sem convallis in. Nunc scelerisque lacinia risus sit amet aliquam.

# Output: 31
# input_string1="She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# print(len(set(input_string1.lower().split())))


# [*] Усложнение. Выведите кол-во слов с учетом регистра и без учета регистра

# №4.3[29]. Для натурального n создать список, состоящий из элементов последовательности 3n + 1.

# Пример:

# - Для n = 6: [1, 4, 7, 10, 13, 16, 19]

# Усложнение:

# Создать список, где указанные числа будут стоять на соответствующих индексах, остальные элементы сделать нулевыми, т.е. для индекса 1, значение 1,

# для индекса 4, значение 4 и т.п.

# Пример:

# - Для n = 6: [0,1,0,0,4,0,0,7,0,0,10]
# n=6
# new_list=[]
# for i in range(0,n+1):
#         new_list.append(0)
#         new_list.append(i*3+1)
#         new_list.append(0)
# print(new_list)
# #компрехендшон
# n=6
# print([i*3+1 for i in range(0,n+1)])
#Усложнение
# new_list = []

# for i in range(n + 2):
#     new_list.append(0)
#     new_list.append(i * 3 + 1)
#     new_list.append(0)

# print(new_list)

# 2.Дан список:
# # ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# # Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
# # (добавить кавычку до и кавычку после элемента списка, являющегося числом)
# # и дополнить нулём до двух целочисленных разрядов:
# # Результат:
# # ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# # Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
# # Как модифицировать это условие для чисел со знаком?
# #
# # *Примечание:*
# # - Задача обычной сложности: создайте новый список и заполните его нужными значениями, включая элементы-кавычки
# # или измените существующий список, но не добавляйте элементы-кавычки.
my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

new_list = []

for idx, element in enumerate(my_list):
    if element.isdigit() or (element[0] in "+-" and element[1:].isdigit()):
        new_list.append('"')
        new_element = ""
        if element[0] in "+-":
            new_element += element[0]
            element = element[1:]
        if len(element) == 1:
            new_element += f'0{element}'
        else:
            new_element += element
            new_list.append(new_element)
            new_list.append('"')
    else:
        new_list.append(element)

print(new_list)
        
    
    
        

