""" Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
45 -> 101101
3 -> 11
2 -> 10 """

def number_binarization (number):
    binary_number = ''
    while (number > 0):
        binary_number = str(number%2) + binary_number
        number = number // 2
    print(binary_number)

num = int(input('Введите натуральное число: '))
number_binarization(num)