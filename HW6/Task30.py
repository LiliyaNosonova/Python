# Задача 30:  Заполните массив элементами арифметической прогрессии. Её
# первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input('Введите первый элемент арифметической прогрессии: '))
d = int(input('Введите шаг прогрессии: '))
n = int(input('Введите количество элементов прогрессии: '))
arr = list(range(n))


i = 0
arr[0] = a1
while i < len(arr):
    arr[0] = a1
    arr[i] = arr[i-1] + d
    i += 1
print(arr)


#эталонный вариант
# for i in range(n):
#     print(a1 + i * d)



