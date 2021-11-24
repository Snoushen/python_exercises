"""
6. Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
-  якщо довжина бульше 50 - > ваша фантазiя
"""

def string_processing(some_string):
    if 30 < len(some_string) < 50:
        print(len(some_string))
        print(len([x for x in some_string if x.isalpha()]))
        print(len([x for x in some_string if x.isnumeric()]))

    if len(some_string) < 30:
        print(sum([int(x) for x in some_string if x.isnumeric()]))
        print("".join([x for x in some_string if x.isalpha()]))

    if len(some_string) > 50:
        print(sorted(some_string))

first_case = "AAAAAAAAAAAAAAAAaaaaaaaaAaaa55555"
second_case = "BBBBBBBBB1111111111"
third_case = "AAAACCCCCCCCCCCCCCCCCCCCDDDDD555DDDDDDDDDDDDDddaa12312aaaaaaaaaaaaaaaaatttttttttttt"

string_processing(second_case)