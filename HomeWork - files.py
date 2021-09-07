import os
import shutil
print(os.path.exists("D:\\Python\project1\doc.txt")) #False
print(os.path.exists("D:\\Python\project1\pythonProject\doc.txt")) #True
print(os.path.exists("D:\\Python\project1\doc000.txt")) #False

print(os.path.getsize("D:\\Python\project1\pythonProject\doc.txt")) #получение размера файла

shutil.copy("D:\\Python\project1\pythonProject\doc.txt", "D:\\Python\project1\doc.txt") # копирование только внутренних данных файла

shutil.copy2("D:\\Python\project1\pythonProject\doc1a.txt", "D:\\Python\project1\doc1a.txt") # копирование файла, с полными сведениями о нем

try:
    with open("D:\\Python\project1\doc.txt") as file:
        print('Документ открыт')
except:
    print('К сожалению, документ не найден')
try:
    with open("D:\\Python\project1\pythonProject\doc.txt") as file:
        print('Документ открыт')
except:
    print('К сожалению, документ не найден')

with open("doc.txt", "w") as somefile:
    somefile.write("Привет! \n")
    somefile.write("Привет, мир! \n")
    somefile.write("Это текст для дз! \n")

'''
file = open ('open.txt', 'a')
file.write ('Дописываем текст в сущесвтующий файл.')
file.close ()
'''