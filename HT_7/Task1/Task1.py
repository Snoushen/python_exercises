"""
1. Програма-банкомат.
   Створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.data>);
      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>) та історію транзакцій (файл <{username}_transactions.data>);
      - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено число; знімається не більше, ніж є на рахунку).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
      - файл з користувачами: тільки читається. Якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
      - спочатку - логін користувача - програма запитує ім'я/пароль. Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :) )
      - потім - елементарне меню типа:
        Введіть дію:
           1. Продивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив :)
"""
import json
from datetime import datetime


"""
Alex 123a
Roma 456b
Yarik 789c
Sveta 123AbC
Oleg 999abc
"""
def start():

    while True:
        print(20 * "=")

        name = input("Введіть імя: ")
        password = input("Введіть пароль: ")
        confirm_user(name, password)
        while True:
            print("Виберіть дію: ")
            print("1.Зняти з балансу\n2.Поповнити баланса\n3.Переглянути баланс\n4.Вихід з аккаунту")
            try:
                choise = int(input("Ваш вибір: "))
            except ValueError:
                choise = 0
            if choise == 1:
                try:
                    cash = int(input('Веедіть сумму для зняття: '))

                except ValueError:
                    cash = 0
                    print("Помилка вводу")
                get_money(name, cash)
                print('Ваш баланс: ', check_balance(name))
            elif choise == 2:
                try:
                    cash = int(input('Веедіть сумму для поповнення: '))

                except ValueError:
                    cash = 0
                    print("Помилка вводу")
                add_money(name, cash)
                print('Ваш баланс: ', check_balance(name))

            elif choise == 3:
                print('Ваш баланс: ', check_balance(name))
            elif choise == 4:
                print(20 * '=')
                break
            else:
                print("Введено недопустиму дію")
            print(20*'=')

def transaction(name,name_trans,sum_of_trans,before_trans):
    now = datetime.now()
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")

    data = { 'Name': name,
             'transaction': str(name_trans),
             'balance before ': before_trans,
             'sum of trans': sum_of_trans,
             'balance after': check_balance(name),
             'date': current_time
            }
    with open(f"transaction/{name}_transactions.data", "a+") as file:
        json.dump(data,file)
        file.write('\n')


def check_balance(name):
    with open(f"balance/{name}_balance.data", "r") as file:
        data = int(file.read())
    return data

def add_money(name,cash):
    current_balance = check_balance(name)
    new_balance = current_balance + cash
    a = str(new_balance)
    with open(f"balance/{name}_balance.data", "w") as file:
        file.write(a)
    transaction(name,add_money.__name__,cash,current_balance)

def get_money(name,cash):
    current_balance = check_balance(name)
    if current_balance < cash:
        print('У вас недостатньо коштів на рахунку')
    else:
        new_balance = int(current_balance) - cash
        with open(f"Task1/balance/{name}_balance.data", "w") as file:
            file.write(str(new_balance))
    transaction(name,get_money.__name__, cash, current_balance)

def confirm_user(name,password):
    with open("users.data", "r") as file_check_user:
        confirmation = False
        for line in file_check_user:
            a = line.split()
            if a[0] == name and a[1] == password:
                print(f'Пароль підтверджено!')
                print(20 * '=')
                confirmation = True
        if confirmation == False:
            print("error: Пароль або логін не є корректними")
            raise PermissionError
    return



start()