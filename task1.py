"""
1) Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно,
в программе.
"""
result_list = [5, 'text', True, 22.6, None]
def list_type(el):
    for el in range(len(result_list)):
        print(type(result_list[el]))
    return
list_type(result_list)