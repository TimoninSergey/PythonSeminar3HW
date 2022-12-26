""" Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
для k = 8 список будет выглядеть так: 
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

 """

def fibonacci_num (n):
    if n == 0:
        return 0
    elif n in (1,2):
        return 1
    else:
        return (fibonacci_num(n-1) + fibonacci_num(n-2))

def fibonacci_list (number):
    fib_list = []
    k = 0
    while (k < number+1):
        fib_list.append(fibonacci_num(k))
        if (k!= 0):
            fib_list.insert(0, (-1)*fibonacci_num(k))
        k = k+1
    print(fib_list)


num = int(input('Введите число: '))
fibonacci_list(num)