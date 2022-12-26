""" Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
стоящих на позиции с нечетным индексом.
Пример:
[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
 """

def create_list_from_file ():
    list = []
    path = 'task1.txt'
    data = open(path, 'r')
    for line in data:
        list.append(int(line))
    print(list)
    return list

def list_uneven_element_sum (list):
    sum = 0
    for item in range(1, len(list), 2):
        sum = sum + list[item]
    print(sum)

list_uneven_element_sum(create_list_from_file())
