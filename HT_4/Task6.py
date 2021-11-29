"""
6. Вводиться число. Якщо це число додатне, знайти його квадрат, якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.
"""

def change_number(number):
    result = 0
    if number < 0:
        result = number + 100
    elif number > 0:
        result = number ** 2
    else:
        pass
    return result

input_number = int(input("Enter your number: "))

print(change_number(input_number))