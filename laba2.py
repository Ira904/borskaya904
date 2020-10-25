class money:
    def __init__(self, amount ):
        self.amount  = amount 

print('Введите сумму денег:')

money = money(amount =input())
print('Вы: ', money.amount)

class Bank:
   def __init__(self, namebankOne, namebankTwo, namebankThree):
       self.namebankOne = namebankOne
       self.namebankTwo = namebankTwo
       self.namebankThree = namebankThree


bank = Bank("Сбер", "ВТБ", "Росбанк")
one, two, three = 1, 2, 3


print('Доступные банки:')

print(one, ':', bank.namebankOne)
print(two, ':', bank.namebankTwo)
print(three, ':', bank.namebankThree)

print('В каком банке вы бы хотели приобрести валюту?')
myBan = input()


class Bid:
    def __init__(self, bidOne, bidTwo, bidThree):
        self.bidOne = bidOne
        self.bidTwo = bidTwo
        self.bidThree = bidThree

bid = Bid("65", "68", "65.8")


if myBan == '1':
    print('Вы выбрали', bank.namebankOne, 'стоимость 1 единицы: ', bid.bidOne)
elif myBan == '2':
    print('Вы выбрали', bank.namebankTwo, 'стоимость 1 единицы ', bid.bidTwo)
elif myBan == '3':
    print('Вы выбрали', bank.namebankThree, 'стоимость 1 единицы ', bid.bidThree)
else:
    print('Выбранного вами банка не существует')