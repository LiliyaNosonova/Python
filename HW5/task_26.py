# Задача 26:  Напишите программу, которая на вход принимает два числа 
# A и B, и возводит число А в целую степень B с помощью рекурсии.

a = int(input('Введите число: '))
b = int(input('Введите степень: '))


#1 вариант
def my_pow (x, y):
    if y == 0:
        return int(1)
    return my_pow(x, y - 1) * x
print(f"{a} в степени {b} = {my_pow(a,b)}")

#2 Вариант
# def my_pow(a, b):
#     return 1 if b == 0 else my_pow(a, b - 1) * a

# print(my_pow(a, b))

# print(pow(0, 0)) - пример
