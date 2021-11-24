"""
5. Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;
-  Створiть просту умовну конструкцiю(звiсно вона повинна бути в тiлi ф-цiї),
пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" і при нерiвностi змiнних "х" та "у" вiдповiдь повертали рiзницю чисел.
-  Повиннi опрацювати такi умови:
-  x > y;       вiдповiдь - х бiльше нiж у на z
-  x < y;       вiдповiдь - у бiльше нiж х на z
-  x == y.      вiдповiдь - х дорiвнює z
"""

def difference(x,y):
    difference = abs(x - y)
    if (x - y) == 0:
        print(f'відповідь - {x} дорівнює {y} ')
    if x > y:
        print(f'відповідь - {x} більше за  {y} на {difference}')
    if x < y:
        print(f'відповідь - {x} меньше за {y} на {difference}')

first_number = int(input("Введіть число х: "))
second_number = int(input("Введіть число у: "))

difference(first_number,second_number)
