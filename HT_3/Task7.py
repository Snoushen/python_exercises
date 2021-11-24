"""
7. Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!
"""
def adronui_colaider(value1,value2,action):
    if action == '+':
       return value1 + value2
    if action == '-':
        return value1 - value2
    if action == '/':
        return value1 / value2
    if action == '*':
        return value1 * value2

number1 = int(input('Введіть перше число: '))
number2 = int(input('Введіть друге число: '))
option_set = input('Введіть дію("+","-","/","*"): ')

print(adronui_colaider(number1,number2,option_set))