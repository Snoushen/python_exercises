"""
4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона, і вертатиме список простих чисел всередині цього діапазона.
"""
import sympy

def prime_list(start_range, end_range):
    is_prime_list_result = [value for value in range(start_range,end_range) if sympy.isprime(value)]
    return is_prime_list_result

input_start = int(input("Enter start of range: "))
input_end = int(input("Enter end of range: "))
print(prime_list(-input_start,input_end))