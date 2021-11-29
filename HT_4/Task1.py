"""
1. Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата, і вертатиме 3 значення (кортеж):
 периметр квадрата, площа квадрата та його діагональ.
"""
import math

def square(side_square=1):

    P = side_square * 4
    A = side_square**2
    D = math.sqrt(side_square)

    return A, P, D

print(square(int(input("Enter the side of square: "))))

