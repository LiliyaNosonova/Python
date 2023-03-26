# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Введите N: '))

res = 0
k = 0

#1 вариант
while (res * 2) < n:
    res = 2 ** k
    k += 1
    print(res)


# 2 вариант
while res < n:
    res = 2 ** k
    k += 1
    if res < n:
        print(res)

