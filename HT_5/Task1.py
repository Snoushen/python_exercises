"""
1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
   Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>)
   і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
   Логіка наступна:
       якщо введено коректну пару ім'я/пароль - вертається <True>;
       якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>,
            інакше (<silent> == <False>) - породжується виключення LoginException
"""
class LoginException(Exception):
    pass

def user(username,password,silent=False):
    value_check = [username,password]
    list_user = [["Kostia","123"],["Alex","321"],["Dima","a"],["Yarik","yarik"],["Sasha","sahsa123"]]

    try:
        flag = 0
        for value in list_user:
            if value_check == value:
                flag = 1
        if flag == 0:
            if silent == True:
                return False
            else:
                raise LoginException
        else:
            return True
    except LoginException:
        return "Error: wrong name or password"





print(user("Kostia","123"))
print(user("Kostiaaaa","123",silent=True))
print(user("Kostiaaaa","123"))
