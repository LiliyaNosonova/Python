# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

money = int(input('Введите количество монет: '))

count_1 = 0
count_0 = 0

for n in range(money):
    y = 1
    while y == 1:
        x = int(input(f'Монета {n+1} Орел или решка (0 или 1)?: '))
        if x != 0 and x != 1:
            print('Значение введено неверно')
        else:
            y = 0


   
    if x == 1:
        count_1 += 1
    else:
        count_0 += 1
# print(count_1, count_0)
        


if count_1 < count_0:
    print(count_1)
else:
    print(count_0)


