# Задача 4:
# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов
# сделал каждый ребенок, если известно, что Петя и Сережа
# сделали одинаковое количество журавликов, а Катя сделала
# в два раза больше журавликов, чем Петя и Сережа вместе.

n = int(input('Введите количество сделанных журавликов: '))
n1 = n/6
n2 = n/6
n3 = (n1 + n2) * 2

print(f'Петя сделал журавликов ->', n1, 'Сережа ->', n2, 'Катя ->', n3)