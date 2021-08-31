print ('Введите стороны прямоугольника:')
a = int(input('Сторона a: \n'))
b = int(input('Сторона b: \n'))
size_square = [] # стороны ребер полученных квадратов при нарезании
def square (a, b):
    if a < b:
        size_square.append(a)
        return square(a, b - a)
    elif b < a:
        size_square.append(b)
        return square(a-b, b)
    elif a == b:
        size_square.append(a)
        return a
square (a, b)
print ('Длины ребер полученных квадратов: ' + ''.join(str(size_square)))
print ('Количество полученных квадратов: ' + str(len(size_square)))


