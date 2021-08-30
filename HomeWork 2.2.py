Matrica_x = [[i * j for i in range(0, 6)] for j in range(0, 5)]
print(Matrica_x)

sum_max = [sum(i) for i in Matrica_x]
print('Сумма чисел строк матрицы:')
print (sum_max)
print('Номер строки, сумма чисел в которой максимальна: \n ' + str(sum_max.index(max(sum_max)) + 1))