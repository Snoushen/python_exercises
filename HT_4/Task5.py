"""
5. Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.
"""
import sympy

def fibonacci(number):
    list_fibonacci = [sympy.fibonacci(x) for x in range(0,number)if number > sympy.fibonacci(x)]
    return list_fibonacci
input_user = int(input("Enter your number: "))
print(fibonacci(input_user))
