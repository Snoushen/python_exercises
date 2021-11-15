
stop_cycle = True
concatenate_string = ''

while stop_cycle:
    concatenate_second_string = input()

    if concatenate_second_string == 'q':
        break
    concatenate_string += concatenate_second_string

print(concatenate_string)