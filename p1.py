# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import math

N = int(input())
mylist = []

for i in range(1, N+1):
    mylist.insert(i, math.factorial(i))
    # print(f"факториала числа({i}): {math.factorial(i)}")
print(mylist)