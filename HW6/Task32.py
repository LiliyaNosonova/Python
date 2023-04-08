# Задача 32: Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не
# больше заданного максимума)

arr = list(range(10,50))
# arr = [15, 25, 36, 48, 69, 20, 2, 5, 7, 6]
print(arr)

min = int(input('Введите нижнюю границу: '))
max = int(input('Введите верхнюю границу: '))
res = []

if min >= arr[0] and max <= len(arr): 
    for i in range(len(arr)):
        if min <= arr[i] <= max:
            vol = res.append(i)
        else:
            i += 1
    print(res)
else:
    print ('Одна из границ лежит вне диапазона списка!\nВведите корректные границы!')




# эталонное решение
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list_1)):
#     if min_number <= list_1[i] <= max_number:
#     print(i)