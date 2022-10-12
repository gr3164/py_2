# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

N = int(input())
mylist = []
mylist2 = []
count = 0

for i in range(-N, N+1):
    mylist.insert(count, i)
    count+=1

for i in range(0, len(mylist)):
    mylist2.insert(i, mylist[i-2])
      
print(f"{N} -> {mylist2}")
