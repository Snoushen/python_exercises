"""
1. Написати скрипт, який конкатенує всі елементи в списку і виведе їх на екран. Список можна "захардкодити".
   Елементами списку повинні бути як рядки, так і числа.
"""

array_list = []

cycle_state = True
print("Введите элемент списка(для окончания конкатенации или выхода введите q): ")
count = 0

while cycle_state:
    element_add = input("Элемент №{}: ".format(count+1))
    if element_add.isnumeric():
        element_add = int(element_add)
    if element_add == "q":
        cycle_state = False

    else:
        array_list.append(element_add)
    count += 1

print("Ваш список эелемнтов: ", array_list)

concatanated_list = [str(i) for i in array_list]
print("Результат конкатенации: ", end = "")

print("".join(concatanated_list))
