"""
5. Запишіть в один рядок генератор списку (числа в діапазоні від 0 до 100), сума цифр кожного елемент якого буде дорівнювати 10.
   Перевірка: [19, 28, 37, 46, 55, 64, 73, 82, 91]
"""

gen_list = [i for i in range(0, 100)if (i % 10) + (i // 10) == 10]
print(gen_list)