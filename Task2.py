""" Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
[2, 3, 4, 5, 6] => [12, 15, 16];
[2, 3, 5, 6] => [12, 15] """

def create_list_from_file (path):
    list = []
    data = open(path, 'r')
    for line in data:
        list.append(int(line))
    print(list)
    return list

def list_items_multiplication (list):
    multi_list = []
    number = 0
    while (number > -1 and number < len(list)/2):
        multi_list.append(list[number] * list[len(list)-1-number])
        number = number + 1
    print(multi_list)

list_items_multiplication(create_list_from_file('task2.txt'))