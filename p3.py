# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

s1 = "one"
s2 = "onetwonine"

for i in range(0,len(s1)):
    count = 0
    for x in range(0,len(s2)):
        if s1[i] == s2[x:x+1]:
            count+=1
    print(f"{s1[i]} - {count}")          