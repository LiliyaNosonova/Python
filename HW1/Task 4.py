# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

total = int(input('Количество журавликов: '))
# total = (2 * p) + (2 * p) * 2
p = int(total / 6)
print(p, '- сделали Петя и Сережа каждый')
s = int(4 * p)
print(s, '- сделала Света')