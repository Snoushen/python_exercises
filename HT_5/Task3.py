"""
3. На основі попередньої функції створити наступний кусок кода:
   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)
"""



class NameError(Exception):
    pass
class ErrorPassword(Exception):
    pass
def validation_function(name,password,val_state=False):
    try:
        if 50 <= len(name) or len(name) <= 3:
            val_state = False
            raise NameError
        if len(password) < 8:
            val_state = False
            raise ErrorPassword

        flag_character = False
        flag_upper = False
        for character in password:
            if character.isdigit():
                flag_character = True
            if character.isupper():
                flag_upper = True

        if flag_character == False or flag_upper == False:
            raise ErrorPassword

    except NameError:
        return "NameError - max length 50 symbol,min length 3"
    except ErrorPassword:
        return "PasswordError - password must contain,8 character,one symbol Upper and one number"
    else:
        return "OK"


account_list = [["Kostia","12344444s"],["Al","321asSdads1"],["Dima","sad4asdas3sD"],["Yarik","yarik"],["Sasha","sahsa123232"]]

for account in account_list:
        print("Name: ", account[0])
        print("Password: ", account[1])

        print("Status: ",validation_function(account[0],account[1]))
        print(10 * "=")


