import random
n = int(input("Введите размер списка: \n"))

A = []
for i in range (n):
    a = random.random()
    A.append(a)
for i in range (n):
    print (A[i])

