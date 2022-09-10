# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# n = float(input('Введите число '))
# x = str(n)
# sum = 0
# for i in x:
#     if i != '.':
#         j = int(i)
#         sum += j
# print(sum)

# 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# N = int(input('Введите число '))
# comp = 1
# i = 2
# while i <= N:
#     comp *= i
#     i += 1
# print (comp)

# 3.Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

# k = int(input('Введите число '))
# sum = 0
# i = 1
# if k != 0:
#     while i <= k:
#         find = (1+1/i)**i
#         sum += find
#         i += 1
#     print(sum)
# else:
#     print('Делить на 0 нельзя!')

# 4.Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

# N = int(input('Введите число '))
# find = str(input('Введите позиции элементов через пробел '))
# list = range(-N,N+1)
# comp = list[int(find.split(' ')[0])]*list[int(find.split(' ')[1])]
# print(comp)

# 5.Реализуйте алгоритм перемешивания списка.

# list = [5,8,2,3,15,90,52,0]
# import random
# random.shuffle(list)
# print(list)

# list = [5,8,2,3,15,90,52,0]
# import random
# i = 0
# while i < len(list):
#     second_pos = random.randint(0,7)
#     help = list[i]
#     list[i] = list[second_pos]
#     list[second_pos] = help
#     i += 1
# print(list)