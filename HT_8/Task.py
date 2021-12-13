"""
1. Доповніть програму-банкомат з попереднього завдання таким функціоналом, як використання банкнот.
   Отже, у банкомата повинен бути такий режим як "інкассація", за допомогою якого в нього
    можна "загрузити" деяку кількість банкнот (вибирається номінал і кількість).
   Зняття грошей з банкомату повинно відбуватись в межах наявних банкнот
   за наступним алгоритмом - видається мінімальна кількість банкнот наявного номіналу.
   P.S. Будьте обережні з використанням "жадібного" алгоритму (коли вибирається спочатку найбільша банкнота,
   а потім - наступна за розміром і т.д.) - в деяких випадках він працює неправильно або не працює взагалі.
   Наприклад, якщо треба видати 160 грн., а в наявності є банкноти номіналом 20, 50, 100, 500,  банкомат не зможе видати суму
   (бо спробує видати 100 + 50 + (невідомо), а потрібно було 100 + 20 + 20 + 20 ).
   Особливості реалізації:
   - перелік купюр: 10, 20, 50, 100, 200, 500, 1000;
   - у одного користувача повинні бути права "інкасатора". Відповідно і у нього буде своє власне меню із пунктами:
     - переглянути наявні купюри;
     - змінити кількість купюр;
   - видача грошей для користувачів відбувається в межах наявних купюр;
   - якщо гроші вносяться на рахунок - НЕ ТРЕБА їх розбивати і вносити в банкомат - не ускладнюйте собі життя,
    та й, наскільки я розумію, банкомати все, що в нього входить, відкладає в окрему касету.
2. Для кращого засвоєння - перед написанням коду із п.1 - видаліть код для старої програми-банкомату і напишіть весь код наново (завдання на самоконтроль).
   До того ж, скоріш за все, вам прийдеться і так багато чого переписати.

   Можливості банкомату:
        -Банкомат має
        -Меню (Один для користовуча один для Інкасатора)
            Меню користувача:
                -Переглядати баланс
                -Поповнювати рахунок
                -Знімати з рахунку
                -Вихід з аккаунту
            Меню інкасатора:
                - переглянути наявні купюри;
                - змінити кількість купюр;
        - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
        - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
        - файл з користувачами: тільки читається. Якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе
        - за кожен функціонал відповідає окрема функція;
        - кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>)
        та історію транзакцій (файл <{username}_transactions.data>);

[{"10"}:10,{"20"}:20,{"50"}:50,{"100"}:100,{"200"}:200,{"500"}:500,{"1000"}:1000]

"""

import json
from pathlib import Path
import datetime
import banknotes

def start():
    def user_confirm():
        for i in data:
            if i['name'] == name and i['password'] == password:
                menu()
                usr_type = ''.join([i["type"] for i in data if i['name'] == name])
                return
        raise PermissionError("password or name is wrong")

    def menu():
        while True:
            menu_user = '====Меню===\n1.Переглянути баланс\n2.Поповнити рахунок\n3.Зняти з рахунку\n4.Вихід з аккаунту'
            collector = '====Меню===\n1.Переглянути наявні купюри\n2.Змінити кількість купюр\n3.Вихід з аккаунту'

            if usr_type == 'collector':
                print(collector)
                choice = input("Введіть дію: ")
                while True:

                    if choice == '1':
                        collector_function(False)
                        break
                    if choice == '2':
                        collector_function(True)
                        break
                    if choice == '3':
                        start()
                    else:
                        print(f"Ви ввели не коректну дію")
                        break
            elif usr_type == 'user':
                print(menu_user)
                choice = input("Введіть дію: ")
                while True:
                    if choice == '1':
                        print("Ваш баланс: ", balance()[0].get('balance'))
                        break
                    if choice == '2':
                        rep_money = input("Введіть суму поповнення: ")
                        if not rep_money.isdigit():
                            print("Ви ввели не коректну дію, спробуйте ще раз")
                            break

                        replenishment(int(rep_money))
                        break
                    if choice == '3':
                        w_money = input("Введіть суму для зняття: ")
                        if not w_money.isdigit():
                            print("Ви ввели не коректну дію, спробуйте ще раз")
                            break

                        withdraw(int(w_money))
                        break
                    if choice == '4':
                        start()
                    else:
                        print(f"Ви ввели не коректну дію, спробуйте зе раз")
                        break
    def balance():
        with open(outpath / "balance" /f'{name}_balance.json', "r+") as file:
            data_file = json.load(file)
            return data_file

    def withdraw(w_money):
        initial_balance = balance()[0].get('balance')
        balance_now = balance()
        if w_money > balance_now[0]['balance'] or w_money < 0:
            return print("Недостатньо коштів на рахунку")
        banknotes.start_banknotes(w_money)

        balance_now[0]['balance'] = balance()[0].get('balance') - w_money
        print('Ваш баланс: ', balance_now[0]['balance'])

        with open(outpath / "balance" / f'{name}_balance.json', "w") as file:
            json.dump(balance_now, file)
        trans(withdraw.__name__, initial_balance, w_money)

    def replenishment(rep_money: int):

        initial_balance = balance()[0].get('balance')
        balance_now = balance()

        balance_now[0]['balance'] = balance()[0].get('balance') + rep_money
        print('Ваш баланс: ', balance_now[0]['balance'])
        with open(outpath / "balance" /f'{name}_balance.json', "w") as file:
            json.dump(balance_now,file)
        trans(replenishment.__name__, initial_balance, rep_money)


    def trans(name_trans,balance_before,sum_trans):
        now = datetime.datetime.now()
        current_time = now.strftime("%d/%m/%Y %H:%M:%S")

        data = {'Name': name,
                'type_user': usr_type,
                'transaction': name_trans,
                'balance before ': balance_before,
                'sum of trans': sum_trans,
                'balance after': balance()[0].get('balance'),
                'date': current_time
                }

        with open(outpath / "transactions" / f'{name}_transactions.json', "r+") as file:
            read_t = json.load(file)
            read_t.append(data)
        with open(outpath / "transactions" / f'{name}_transactions.json', "w") as file2:
            file2.write('[')
            for i in read_t:
                json.dump(i, file2)
                if i != read_t[-1]:
                    file2.write(', \n')
            file2.write(']')



    def collector_function(action):
        '''
        action True = change banknotes
               False = check banknotes
        :param action:
        :return:
        '''

        with open(outpath / "bank_money.json", "r+") as file:
            data_collector = json.load(file)
            if not action:
                for i in data_collector:
                    print(i)
            elif action:
                banknote = input("Введіть номінал валюти: ")
                check = False
                q_banknote = input("Введіть кількість купюр: ")
                if not q_banknote.isdigit():
                    return print('Введено не дійсне число')
                print(data_collector)
                for i in data_collector:
                    if banknote in i:
                        i[banknote] = int(q_banknote)
                        check = True
                print(data_collector)
                if check == False:
                    print('Даного номіналу не існує спробуйте ще')

                file.seek(0,0)
                json.dump(data_collector,file,indent=4, sort_keys=True)


        return


    outpath = Path.cwd()
    with open(outpath / "users_data", "r") as file_r:
        data = json.load(file_r)
    print(20*'=')
    name = input("Name: ")
    password = input("Password: ")
    usr_type = ''.join([i["type"] for i in data if i['name'] == name])



    user_confirm()

"""
[{"name": "Alex", "password":"123", "type": "collector"},
{"name": "Vasya", "password":"OK",  "type": "user"},
{"name": "Tamara", "password":"vedro123", "type": "user"},
{"name": "Petro", "password":"fayer", "type": "user"}]
"""

start()