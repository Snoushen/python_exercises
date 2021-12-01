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
        list_user.index(value_check)
        silent = True
    except LoginException:
        pass
    return silent

print(user("Kostia","1234"))







