"""
8. Написати скрипт, який отримує від користувача позитивне ціле число і створює словник, з ключами від 0 до введеного числа,
   а значення для цих ключів - це квадрат ключа.
        Приклад виводу при введеному значенні 5 :
        {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""
number_of_element = input("Введите длину кортежа: ")

result = {}

for element in range(1+int(number_of_element)):
    result[element] = element*element
print(result)
