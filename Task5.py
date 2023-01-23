""" Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
для k = 8 список будет выглядеть так: 
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

 """

#def fibonacci_num (n):
#    if n == 0:
#        return 0
#    elif n in (1,2):
#        return 1
#    else:
#        return (fibonacci_num(n-1) + fibonacci_num(n-2))

fibonacci = lambda n: fibonacci(n-1) + fibonacci(n-2) if n > 2 else (1 if n in (1,2) else 0)

def fibonacci_list (number):
    fib_list = [fibonacci(k) for k in range(0, number+1)]
    negafib_list = list(map(lambda x: x*(-1), fib_list))
    reversed_negafib_list = list(reversed(list(filter(lambda x: x != 0, negafib_list))))   #вероятно, пример того, как делать не надо, но работает
    final_list = reversed_negafib_list + fib_list
#    while (k < number+1):
#        fib_list.append(fibonacci_num(k))
#        if (k!= 0):
#            fib_list.insert(0, (-1)*fibonacci_num(k))
#        k = k+1
    print(final_list)


num = int(input('Введите число: '))
fibonacci_list(num)