"""
7. Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.
"""
def if_equal(numbers_list):

    print(numbers_list)
    numbers_list = list(map(str, numbers_list))
    numbers_list.sort()

    numbers_list2 = list(set(numbers_list))
    count = 0

    for check_value2 in numbers_list2:
        count_same_value_more_than2 = 0
        for check_value in numbers_list:
            if check_value2 == check_value:
                count_same_value_more_than2 += 1

        if count_same_value_more_than2 >= 2:
            count += count_same_value_more_than2
        print(f'Object "{check_value2}" = repeated {count}  times')
        count = 0

    return None
range_massive = int(input("Enter a range of massive: "))
array_object = []

for x in range(0,range_massive):
    array_object.append(input(f'Element №{1 + x.__index__()} = '))

if_equal(array_object)

