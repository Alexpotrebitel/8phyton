# №5.1[31]. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где

# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

# https://ru.wikipedia.org/wiki/Числа_Фибоначчи

# Требуется найти N-е число Фибоначчи. Напишите рекурсивную функцию. Обратите внимание, что функция должна возвращать число.

# Примеры/Тесты:

# <function_name>(0) -> 0

# <function_name>(2) -> 1

# <function_name>(9) -> 34
# def recursion(number):
#     if number==0:
#         return 0
#     if number in (1,2):
#         return 1
#     else:    
#         return recursion(number-1)+recursion(number-2)
# print(recursion(3))
# №5.2[33]. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.

# Напишите функцию, которая заменяет оценки, переданные в виде списка, но наоборот: все максимальные – на минимальные.

# Функция должна возвращать новый список оценок

# Примечание: Обратите внимание на side effects функции.

# Примеры/Тесты:

# <function_name>([1, 3, 3, 3, 4, 2, 5, 5, 2]) -> [1, 3, 3, 3, 4, 2, 1, 1, 2]

# [*] Усложненение: Если ни одна оценка не была заменена, функция должна вернуть None

# Примеры/Тесты:

# <function_name>([3, 3, 3, 3, 3, 3, 3, 3, 3]) -> None

# [**] Усложненение: Добавьте параметр в функцию, который определит как будут заменены оценки:

# Друзьям минимальные на максимальные, Врагам - наоборот.

# Примеры/Тесты:

# grades = [1, 3, 3, 3, 4, 2, 5, 5, 2]

# <function_name>(grades, "friend") -> [5, 3, 3, 3, 4, 2, 5, 5, 2]

# <function_name>(grades, "enemy") -> [1, 3, 3, 3, 4, 2, 1, 1, 2]
# def change(grades):
#     tmp_list=grades.copy()
#     min_grades=min(tmp_list)
#     max_grades=max(tmp_list)
#     if min_grades==max_grades:
#         return None
#     for i in range(len(tmp_list)):
#         if tmp_list[i]==max_grades:
#             tmp_list[i]=min_grades
#     return tmp_list
# new_list=[3, 3, 3, 3, 3, 3, 3, 3, 3]   
# print(new_list)
# print(change(new_list)) 
# print(new_list)   
 
# второй вариант:
# def change(grades: list, status: str = None) -> list:
# new_grades = []
# max_grade = max(grades)
# min_grade = min(grades)

# status_dict = {'friend': True, 'enemy': False}

# if min_grade == max_grade:
# return None


# for grade in grades:
# if grade == max_grade:
# grade = min_grade
# new_grades.append(grade)


# return new_grades



# grades_list_1 = [1, 3, 3, 3, 4, 2, 5, 5, 2]
# grades_list_2 = [3, 3, 3, 3, 3, 3, 3, 3, 3]

# print(change(grades_list_1))
# print(grades_list_1)
# print(change(grades_list_2))
# №5.3[35]. Напишите функцию, которая принимает число и проверяет, является ли оно простым

# Напоминание: Простое число - это число, которое имеет 2 делителя нацело: 1 и само число

# Если число простое - функция возвращает True, если нет - возвращает False

# Примеры/Тесты:

# <function_name>(13) -> True

# <function_name>(10) -> False

# def plain_num(n):
#     if not isinstance(n,int):
#         return None
#     for divider in range(2,n):
#         if n%divider==0:
#             return False
#     return True
# print(plain_num(3))
# №5.4[37] Напишите функцию, которая принимает натуральное число n, в теле функции считывает (input) последовательность из n элементов

# Возвращает эту последовательность в виде строки в обратном порядке

# Примеры/Тесты:

# <function_name>(5) 1 2 3 4 5 -> '5 4 3 2 1'

# <function_name>(3) 8 7 9 -> '9 7 8'

# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
def reverce_print(n):
    string=input()
    if n==1:
        return string

    return f"{reverce_print(n-1)} {string}"

print(reverce_print(5))
