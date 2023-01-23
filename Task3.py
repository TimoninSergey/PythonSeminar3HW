""" Задайте список из вещественных чисел. 
Напишите программу, которая найдёт разницу между максимальным и минимальным значением 
дробной части элементов, отличной от 0.
Пример:
[1.1, 1.2, 3.1, 5, 10.01] => 0.19 """


def create_list_from_file (path):
    data = open(path, 'r')
    list = [int(line) for line in data]
#    for line in data:
#        list.append(int(line))
    print(list)
    return list

def min_max_fractional_difference (list):
    frac_min = 10
    frac_max = 0
    for item in list:
        if (item%1 > frac_max):
            frac_max = round(item%1,2)
        elif (0 < item%1 < frac_min):
            frac_min = round(item%1,2)
    print(frac_min, frac_max)
    print(frac_max - frac_min)

min_max_fractional_difference(create_list_from_file('task3.txt'))