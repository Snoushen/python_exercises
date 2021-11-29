"""
3. Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000, и яка вертатиме True, якщо це число просте, и False - якщо ні.
"""
import sympy

def is_prime(number):
    return sympy.isprime(number)

print(is_prime(int(input("Verify prime number, enter your number: "))))
