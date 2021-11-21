"""
2. Написати скрипт, який пройдеться по списку, який складається із кортежів, і замінить для кожного кортежа останнє значення.
   Список із кортежів можна захардкодити. Значення, на яке замінюється останній елемент кортежа вводиться користувачем.
   Значення, введене користувачем, можна ніяк не конвертувати (залишити рядком). Кількість елементів в кортежу повинна бути різна.
             Приклад списка котежів: [(10, 20, 40), (40, 50, 60, 70), (80, 90), (1000,)]
             Очікуваний результат, якщо введено "100":
        Expected Output: [(10, 20, "100"), (40, 50, 60, "100"), (80, "100"), ("100",)]
"""
#Имопрт рандом библиотеки
import random

def verify_input(verify_string):
    if verify_string == 'help':
        print("e - выход из программы")
        print("с - потвердить создание кортежей")
    if verify_string == 'e':
        print("Goodbye!!!")
        exit(0)

    return verify_string

list_number = []

print("==================================================================================================")
print("==================Добрый день, программа создана для создания списка из кортежей==================")
print("=============================Для подсказки введите help===========================================")

calc_cycle = 0
while True:
    number_elements_of_tuple = verify_input(input("Количество элементов в кортеже N{}: ".format(calc_cycle+1)))
    if str(number_elements_of_tuple) == "c":
        break

    try:
        number_of_tuple = tuple(random.randint(0,100) for i in range(int(number_elements_of_tuple) ))
        print(number_of_tuple)
        calc_cycle += 1
        list_number.append(number_of_tuple)
    except:
        if number_elements_of_tuple == "help":
            pass
        else:
            print("Вы ввели не число попробуйте еще")


print("==================================Ваш список====================================================== \n",list_number,sep = "")

#Переобразовываем каждый елемент кортежа в список
lst = [list(i) for i in list_number]
print("Введите число для замены каждого последнего элемента кортежа: ")
change_last_number = None

while change_last_number == None:
    temporary_variable = verify_input(input())
    try:
        change_last_number = int(temporary_variable)
        #Каждый последний елемент меняем на число которое вводим
        for x in lst:
            x[-1] = change_last_number
    except:
        print("Введите число")
#Переобразовываем в кортеж
list_number = [tuple(x) for x in lst]

print("====================================Результат=====================================================\n",list_number,sep = "")
