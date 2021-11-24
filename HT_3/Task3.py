"""
3. Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12), яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)
"""
def season(month_number):

    result = "1"

    month_library = {'зима': [12, 1, 2],
                     'весна': [3, 4, 5],
                     'літо': [6, 7, 8],
                     'осінь': [9, 10, 11]}

    for x,y in month_library.items():
        for z in y:
            if month_number == z:
                    result = x
    return result

print("Пора року: ", season(int(input("Введіть цифру місяця: "))))

