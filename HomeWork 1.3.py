
import random
n = int(input('Введите длину списку: \n'))
A = [random.randint(0,99) for i in range (n)]

print (A)
newA = [ ]

for index in range (0, len(A)):
    if (index+1) % 7 != 0:
        newA.append(A[index])

print('Удаляем каждый 7-й элемент списка:')
print (newA)
# if index % 7 == 0
# print (index)
# A.pop(index)
# print (A)