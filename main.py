class User:
    def __init__(self, name, email, phone_number, age = 0):
        self.name = name
        self.email = email
        self.age = age
        self.phone_number = phone_number
    def change_username(self):
        self.name = input('введите новое имя: ')
        print('ваше имя изменено на', self.name)

    def change_num(self):
        self.phone_number = int(input())
        print('ваш номер был успешно изменён на', self.phone_number)

    def change_email(self):
        self.email = input('введите новую почту: ')
        print('ваша почта была успешно сменена на', self.email)

    def change_age(self):
        self.age = int(input('введите новый возраст: '))
        print('ваш возраст был успешно изменён на', self.age)

    def function(self):
        print('😀😁😂😄')
        print('ฅ(^◕ᴥ◕^)ฅ')

Account = User(name = input('введите имя: '), age = int(input('введите возраст: ')), email = input('введите почту: '), phone_number = int(input('введите номер для связи: ')))
while True:
    a = input('опции: '
              'сменить_имя => name, '
              'сменить_возраст => age, '
              'сменить_почту => email, '
              'сменить_номер => number, '
              'показать_прикол => -_-           ')
    if a == 'name':
        Account.change_username()
    elif a == 'age':
        Account.change_age()
    elif a == 'email':
        Account.change_email()
    elif a == 'number':
        Account.change_num()
    elif a == '-_-':
        Account.function()
    elif a == 'full_stop 1':
        break
    else:
        print('ERROR')







