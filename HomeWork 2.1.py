import random
print ('1. Вывести общий список чисел; \n2. Посчитать сумму отрицательных элементов списка; \n3. Псчитать сумму элементов между двумя нулями, если нулей нет вывести ноль')
n = int(input('Введите длину элементов списка: \n'))
List_number = [random.randint (-4,4) for i in range (n)] #список всех чисел
List_negativnumber = [] #список отрицательных чисел
List_numberzero = [] #список чисел между двумя нулями
print ('Общий список чисел')
print (List_number)
# подсчет суммы отрицательных чисел
sum_negativnumber = 0
for i in List_number:
    if i < 0:
        sum_negativnumber += i
        List_negativnumber.append(i)
# выведем список отрицательных чисел
print ('Отрицательные числа данного списка:')
print (List_negativnumber)
# выведем сумму отрицательных чисел
print('Сумма отрицательных чисел списка составляет:' + str (sum_negativnumber))
# подсчет количества нулей
zero = List_number.count(0)
if zero == 2 or zero > 2:
    index_zero = [i for i,x in enumerate(List_number) if x == 0] # список индексов 0 от общего списка
    print ('Список элементов между первыми двумя нулями' + str(List_number[index_zero[0+1]:index_zero[1]]))
    print (List_number[index_zero[0]:index_zero[1]])
    sum_between_zero = sum(List_number[index_zero[0]:index_zero[1]])
    print ('Сумма между нулями: ' + str(sum_between_zero))

else:
    print('Количество нулей не удовлетворяет условию для подсчета суммы между ними: Выводим ноль')


