"""
2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
   - щось своє :)
   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
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
        print("Error: max length 50 symbol,min length 3")
    except ErrorPassword:
        print("Error: password must contain min - 8 character and one number")
    else:
        val_state = True
    return val_state

print(validation_function("Alaaaaaa","Tasdas4D"))

