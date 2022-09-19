# Задайте список из нескольких чисел. Напишите программу, которая найдёт 
# сумму элементов списка, стоящих на нечётной позиции.

# list = [2, 3, 5, 9, 3]
# sum = 0
# for i in range(0, len(list)):
#     if i%2 == 1:
#         sum += list[i]
# print(sum)
# #или
# summ = 0
# for i in range(1, len(list), 2):
#     summ += list[i]
# print(summ)


# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# list1 = [2, 3, 4, 5, 6]
# list2 = [2, 3, 5, 6]
# def multyply(list):
#     for i in range((len(list)+1)//2):
#         print(list[i]*list[len(list)-1-i])
# multyply(list1)
# print()
# multyply(list2)


# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.

# list = [1.1, 1.2, 3.1, 5, 10.01]

# for i in range(len(list)):
#     list[i] = round((list[i] - int(list[i])), 3)
# print(list)

# min_frac = list[0]
# max_frac = list[0]
# for n in list:
#     if n != 0:
#         if n < min_frac:
#             min_frac = n
#         if n > max_frac:
#             max_frac = n

# print('max: ', max_frac)
# print('min: ', min_frac)
# print(max_frac - min_frac)


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

dec = int(input())

bin = 0
i = 0
while dec//2 >= 1:
    bin += (dec%2) * (10**i)
    dec = dec // 2
    i += 1
bin += dec * (10**i)
print(bin)









# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
