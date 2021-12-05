"""
6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
"""

def custom_range(stop,start=None,step=1):
    if step == 0:
        raise ValueError
    if start != None:
        stop, start = start, stop
    else:
        start = 0
    try:
        if step > 0:
            while start < stop:
                start += step
                yield start
        if step < 0:
            while start > stop:
                start += step
                yield start

    except ValueError:
        pass

for i in custom_range(10):
    print(i)
