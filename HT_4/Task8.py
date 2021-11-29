"""
8. Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку. Тобто, функція приймає два аргументи:
 список і величину зсуву (якщо ця величина додатня - пересуваємо з кінця на початок, якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
   Наприклад:
       fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
       fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]
"""
import collections

def logical_cycle_move(array,shift_move):
    array = collections.deque(array)
    array.rotate(shift_move)
    shifted_list = list(array)
    return  shifted_list

array = [1, 2, 3, 4, 5]
print("Array: ", array)

shift_value = int(input("Enter shift value: "))

print("Shifted array : ", logical_cycle_move(array,shift_value))