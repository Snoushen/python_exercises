"""
6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
"""

def generator_func(start: int,stop=0,step=1):
    if stop == 0:
        stop = start
        start = 0

    while start < stop:
        start += step
        yield start

for i in generator_func(5):
  print(i)






