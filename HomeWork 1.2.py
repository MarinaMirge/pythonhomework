n = int(input( 'Введите количество учащихся: \n'))
listname = []
listpol = []
listheight = []
listage = []
listweight = []
for i in range(n):
    name = input('Введите имя \n')
    s = input('Введите пол: m - муж/w - жен \n')
# try:
# s = str()
# except:
# print ('Вы ввели не то')
    h = int(input('Введите рост ребенка, см: \n'))
# try:
# h = int()
# except:
# print ('Вы ввели не целое число')
    b = int(input('Введите год рождения: \n'))
    age = 2021-b
    weight = int(input('Введите вес, кг: \n'))
    listname.append (name)
    listpol.append (s)
    listheight.append (h)
    listage.append (age)
    listweight.append (weight)
print (listname)
print (listpol)
print (listheight)
print (listage)
print (listweight)

mediumage = sum(listage)/n
print ('Средний возраст учеников составляет: ' + str(mediumage))

boy = listpol.count('m')
print ('количество мальчиков: ' + str(boy))

girl = listpol.count('w')
print ('количество девочек: ' + str(girl))


print ('Верно ли, что самый высокий мальчик весит больше всех?')
max_height = 0
max_height_index = 0
for i in range (0, len(listheight)):
    if listheight[i] > max_height and listpol[i] == 'm':
        max_height = listheight[i]
        max_height_index = i

max_weight = 0
max_weight_index = 0
for i in range (0, len(listweight)):
    if listweight[i] > max_weight and listpol[i] == 'm':
       max_weight = listweight[i]
       max_weight_index = i

if max_height == max_weight == 0:
    print('Мальчиков нет')
elif max_height_index == max_weight_index:
    print ('Верно!')
else:
    print('Не верно!')


print ('Верно ли, что самая маленькая девочка является самой юной среди девочек?')

min_height = 0
min_height_index = 0
for i in range (0, len(listheight)):
    if listheight[i] < min_height and listpol[i] == 'w':
        min_height = listheight[i]
        min_height_index = i

min_weight = 0
min_weight_index = 0
for i in range (0, len(listweight)):
    if listweight[i] < min_weight and listpol[i] == 'w':
        min_weight = listweight[i]
        min_weight_index = i

if min_height == min_weight == 0:
    print('Девочек нет')
elif min_height_index == min_weight_index:
    print ('Верно!')
else:
    print('Не верно!')

