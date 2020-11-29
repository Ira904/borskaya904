import csv
class peolpe:
    def __init__(self, firsname, lastname, age):
         
        self.firsname = firsname
        self.lastname = lastname
        self.age = age

class SberBank:
    def __init__(self, name, cent):
       self.name = name
       self.cent = cent

    def WriterPeolpe(self, peolpe):
        myData = [["FirstName", "LastName", "Age", "NameCredit", "Cent"], 
            [peolpe.firsname, peolpe.lastname, peolpe.age, self.name, self.cent]] 
            
        myFile = open('WriterPeolpe.csv', 'w')
        with myFile:
            writer = csv.writer(myFile, delimiter=';')
            writer.writerows(myData)
     
    def DictWriterPeolpe(self, peolpe):
        with open('DictWriterPeolpe.csv', 'w') as csvfile:
            fieldnames = ['FirstName', 'LastName', 'Age', 'NameCredit', 'Cent' ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
 
            writer.writeheader()
            writer.writerow({'FirstName': peolpe.firsname, 'LastName': peolpe.lastname, 'Age': peolpe.age, 'NameCredit': self.name, 'Cent': self.cent}) 

print('Приветствуем Вас в Сбербанк!')
print('Введите Ваше имя, фамилию, возраст:')

peolpe = peolpe(firsname=input(), lastname=input(), age=input())

print('Вы: ', peolpe.firsname, peolpe.lastname, peolpe.age)

if peolpe.age < '18':
    print('Извините, но в нашем банке вы можете получить кредит только с 18 лет')
    exit(0)

cr1 = SberBank("Потребительский кредит","9,9%")
cr2 = SberBank("Кредит для бизнеса","17%")
cr3 = SberBank("Кредит на образование","3%")
cr4 = SberBank("Ипотека","6,6%")

print('Наш банк предлагает следующие возможности кредитования:')
print('1', cr1.name)
print('2', cr2.name)
print('3', cr3.name)
print('4', cr4.name)

print('Какой кредит вам нужен?')
credit = input()

if credit == '1':
    print('Вы выбрали', cr1.name, 'условия кредитования:', cr1.cent)
elif credit == '2':
    print('Вы выбрали', cr2.name, 'условия кредитования:', cr2.cent)
elif credit == '3':
    print('Вы выбрали', cr3.name, 'условия кредитования:', cr3.cent)
elif credit == '4':
     print('Вы выбрали', cr4.name, 'условия кредитования:', cr4.cent)
else: 
    print('Данный вариант кредитования требует особых условий, вы можете оформить заявку на сайте')
    
print('Просмотреть другие возможности кредитования? Y/N')
answer = input()

while answer != 'N': 
    print('Доступные услуги:')

    print(cr1.name, ':', cr1.cent)
    print(cr2.name, ':', cr2.cent)
    print(cr3.name, ':', cr3.cent)
    print(cr4.name, ':', cr4.cent)

    print('Какой вид кредитования вам нужен?')
    credit = input()

    if credit == '1':
        print('Вы выбрали', cr1.name, 'стоимость услуги:', cr1.cent)
    elif credit == '2':
        print('Вы выбрали', cr2.name, 'пстоимость услуги:', cr2.cent)
    elif credit == '3':
        print('Вы выбрали', cr3.name, 'стоимость услуги:', cr3.cent)
    elif credit == '4':
        print('Вы выбрали', cr4.name, 'стоимость услуги:', cr4.cent)
    else:
        print('Данный вариант кредитования требует особых условий, вы можете оформить заявку на сайте')
    
    print('Просмотреть другие возможности кредитования? Y/N')
    answer = input()

if answer == 'N': 

    print('Спасибо, что доверяете нам!')
    if credit == '1':
        print('Запись Ваших данных с помощью csv.writer  .......')
        cr1.WriterPeolpe(peolpe)
        print("Заявка на кредит заполненна успешно!")

    elif credit == '2':
        print('Запись Ваших данных с помощью csv.writer  .......')
        cr2.WriterPeolpe(peolpe)
        print("Заявка на кредит заполненна успешно!")

    elif credit == '3':
        print('Запись Ваших данных с помощью csv.DictWriter  .......')
        cr3.DictWriterPeolpe(peolpe)
        print("Заявка на кредит заполненна успешно!")

    elif credit == '4':
        print('Запись Ваших данных с помощью csv.DictWriter  .......')
        cr4.DictWriterPeolpe(peolpe) 
        print("Заявка на кредит заполненна успешно!")        

    print('Спасибо, что вы с нами!')

print('Для вас у нас есть доп. услуги со специальным предложением')
print('Выберите удобный для Вас формат представления данных: 1. Вывод в колонках 2. Вывод в строках ')

myReaderCSV = input()

if myReaderCSV == '1': 
    with open('Dop.csv') as File: 
        reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            print(row)
elif myReaderCSV == '2': 
    results = []
    with open('Dop.csv') as File:
        reader = csv.DictReader(File)
        for row in reader:
            results.append(row)
    print (results)
else:
    exit(0)