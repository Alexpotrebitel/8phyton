# №3.1[17]. Дан список чисел. Определите, сколько в нем встречается различных чисел.

# Примечание: Пользователь может вводить значения списка или список задан изначально.

# Примеры/Тесты:

# [1, 1, 2, 0, -1, 3, 4, 4] -> 6

# [1, 1, 2, 0, 1, 2, 1, 2] -> 3

# elements=[1, 1, 2, 0, 1, 2, 1, 2]
# num_el=len(elements)
#первое решение
# result=[elements[0]]
# for el in elements:
#     for el in elements:
#         for idx in range(num_el):
#             if el==elements[idx]:
#                 continue
#второе решение
# print(len(set(elements))) #преобразовали в множество, определили длнинну, отправили в печать
 

# №3.2[19]. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.

# Примечание: Пользователь может вводить значения списка или список задан изначально.

# Примеры/Тесты:

# Input: [1, 2, 3, 4, 5] k = 3

# # Output: [4, 5, 1, 2, 3] 
# elements=[1, 2, 3, 4, 5]
# k=3
# for i in range(k): 
    # elements.insert(-1,elements.pop(0)) #Данный код на Python является операцией циклического сдвига списка элементов на одну позицию вправо. 
# второй вариант
# elements=[1, 2, 3, 4, 5]
# k=3
# print(elements[2:-2:1])

#другой вариант
# elements=[1, 2, 3, 4, 5]
# k=3
# print (elements[k:]+elements[:k])

# №3.3[21]. Напишите программу для печати всех уникальных значений в списке словарей.

# Примечание: Список словарей задан изначально. Пользователь его не вводит

# Обратите внимание, что в словарях может быть один или несколько элементов

# Примеры/Тесты:

# Input: [{"V": "S001", "X": "D009"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005", "XI": "D011"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 ", "XII": "D001"}]

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# my_dict=[
#     {"V": "S001", "X": "D009"},
#     {"V": "S002"},
#     {"VI": "S001"}, 
#     {"VI": "S005", "XI": "D011"},
#     {"VII": " S005 "},
#     {" V ":" S009 "},
#     {" VIII ":" S007 ", "XII": "D001"}]

# my_set=set()
# for elements in my_dict:
#         for elem in elements.values():
#             my_set.add(elem.strip)
# print(my_set)
#
#print([elem for elem in[list(element.values())for element in my_dict]]) #другой вариант
#print([{elem.strip(): elem.strip() for element in my_dict for elem in element.values()}])
#print([{key: value.strip() for element in my_dict for elem in element.items()}])

#2
# my_list = [
# {"V": "S001", "X": "D009"},
# {"V": "S002"},
# {"VI": "S001"},
# {"VI": "S005", "XI": "D011"},
# {"VII": " S005 "},
# {" V ": " S009 "},
# {" VIII ": " S007 ", "XII": "D001"}
# ]

# # for element in my_list:
# # for elem in element.values():
# # my_set.add(elem.strip())
# #
# # print(my_set)

# # for key, val in {'a': 14}:
# # pass

# print({elem.strip(): elem.strip() for element in my_list for elem in element.values()})

# Дан список, состоящий из целых чисел. Напишите программу, которая сформирует список из тех элементов, которые больше предыдущего (элемента с предыдущим номером)
# Примечание: Пользователь может вводить значения списка или список задан изначально.
# Примеры/Тесты:
# Input: [0, -1, 5, 2, 1]
# Output: [5]

# Input: [-2, -1, 5, 2, 3]
# Output: [-1, 5, 3]
# [*] Усложнение: Запишите алгоритм в одну строку, используйте Comprehension
element=[0, -1, 5, 2, 1]
max_element=[]
# for index_element in range(len(element)):
#     if element[index_element]>element[index_element-1]:
#         max_element.append(element[index_element])
# print(max_element)
#
# в одну строчку
print (element for index_elements in range(len(element)) if element[index_elements] > element[index_elements -1])