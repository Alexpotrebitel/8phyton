# №6.1[39]. Даны два списка чисел. Требуется вывести те элементы первого списка , которых нет во втором списке.

# Создайте функцию.

# Аргументы: два списка целых чисел

# Возвращает: список элементов (смотри условие)

# Примеры/Тесты:

# <function_name>([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1] ) -> [2, 3, 12]

# <function_name>([3, 4, 1, 5, 1, 3, 10, 4, 9, 5], [9, 6, 6, 5, 10, 1, 10, 9, 1, 5] ) -> [3,4]

# [*] Усложнение. Элементы необходимо возвращать в том порядке, в котором они находятся в первом списке, с учетом повторений

# Примеры/Тесты:

# <function_name>([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1] ) -> [3, 3, 2, 12]

# <function_name>([3, 4, 1, 5, 1, 3, 10, 4, 9, 5], [9, 6, 6, 5, 10, 1, 10, 9, 1, 5] ) -> [3, 4, 3, 4]
# def func(list1,list2):
   
#     return list(set(list1).difference(set(list2)))
# print (func([3, 1, 3, 4, 2, 4, 12],[3, 4, 1, 5, 1, 3, 10, 4, 9, 5]))
# def funk2 (list1, list2):
        
#     new_list = list()
#     for i in list1:
#         if i not in list2 and i not in new_list:
#             new_list.append(i)
            
  
#     return new_list
# print(funk2([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1]))

# def funk_set(list1, list2):
#     t1 = perf_counter()
#     rez = list(set(list1).difference(set(list2)))
#     t2 = perf_counter()
#     return rez, t2 - t1


# def funk_list(list1, list2):
#     t1 = perf_counter()
#     new_list = list()
#     for i in list1:
#         if i not in list2 and i not in new_list:
#             new_list.append(i)
#             t2 = perf_counter()
#             return new_list, t2 - t1


# n = 10000
# lst1 = [randint(0, int(n)) for _ in range(n)]
# lst2 = [randint(0, int(n)) for _ in range(n)]

# print(funk_set(lst1, lst2)[1])
# print(funk_list(lst1, lst2)[1])
# №6.2[41] Дан список, целых чисел.

# Напишите функцию, которая определит те элементы списка, у которых два соседних и, при этом, оба соседних элемента меньше данного.

# Функция

# Аргументы: список целых чисел

# Возвращает: список элементов (смотри условие)

# Примеры/Тесты:

# <function_name>([1, 3, 3, 3, 5]) -> [5]

# <function_name>([1, 5, 1, 6, 1]) -> [5,6]

# <function_name>([7, 5, 1, 6, 8]) -> [8]

# <function_name>([8, 1, 5, 4, 5]) -> [8,5]
# def super_func(numbers: list) -> list:
#     result = list()
#     for idx, element in enumerate(numbers):
#         prev_idx = idx - 1
#         next_idx = idx + 1 if idx < len(numbers)-1 else 0
#         if numbers[prev_idx] < element and numbers[next_idx] < element:
#             result.append(element)
#         return result


# data_list = [8, 1, 5, 4, 5]

# print(super_func(data_list))
# №6.3[43] Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.

# Считается, что любые два элемента, равные друг другу, образуют одну пару, которую необходимо посчитать.

# Напишите функцию

# Аргументы: список целых чисел

# Возвращает: кол-во пар

# Примеры/Тесты:

# <function_name>([1, 2, 3, 2, 3]) -> 2

# <function_name>([1, 2, 3, 2, 3, 3, 2, 4]) -> 6
# list_1 =[1, 2, 3, 2, 3, 3, 2, 4]
# def get_list (list_1):
#     count = 0
#     for idx in range (len(list_1)):
#         el = list_1[idx]
#         for idx_2 in range (idx + 1, len(list_1)):
#             if el == list_1[idx_2]:
#                 count += 1
#     return count

# print(get_list(list_1))
# №64.4[45] Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.

# Например, 220 и 284 – дружественные числа.

# 220: 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110, — их сумма равна 284.

# 284: 1, 2, 4, 71 и 142, — их сумма равна 220.

# Первые пары дружественных чисел:

# 220, 284; 1184, 1210; 2620, 2924; 5020, 5564; 6232, 6368

# Для заданного числа number выведите все пары дружественных чисел, каждое из которых не превосходит number.

# Напишите функцию:

# Аргументы: целое число

# Печатает все пары дружественных чисел, не превосходящих аргумент.

# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

# Примечание:

# 1. Выделите значимые куски алгоритма и оформите их в виде функций

# 2. Задокументируйте созданные функции

# 3. Используйте type hinting

# Примеры/Тесты:

# <function_name>(300)

# 220 284

# <function_name>(10000)

# 220 284

# 1184 1210

# 2620 2924

# 5020 5564

# 6232 6368        
# def get_dividers(number:int)-> list:
#     result=list()
#     i=1
#     while i<=number//2:
#         if number%i==0:
#             result.append(i)
#         i+=1
#     return result
# input_number=500
# j=0
# while j<input_number:
#     pair_number=sum(get_dividers(j))
#     if pair_number<input_number and j==sum(get_dividers(pair_number)) and j<pair_number:
#         print(j, sum(get_dividers(j)))
#     j+=1
            
            
    
# def get_dividers(number: int):
# """
# Красивое описание функции
# :param number: int
# :return: generator
# """
# return (x for x in range(1, (number // 2) + 1) if number % x == 0)

# input_number = 10000

# j = 1
# while j < input_number:
# pair_number = sum(get_dividers(j))
# if pair_number < input_number and j == sum(get_dividers(pair_number)) and j < pair_number:
# print(j, sum(get_dividers(j)))
# j += 1       