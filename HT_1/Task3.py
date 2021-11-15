stop_cycle = True
array_list = []

print("Please enter a number(q or Q for quit)")
while stop_cycle:
    message = input()

    try:
        message = int(message)
        if message > 0:
            array_list.append(message)
    except ValueError:
        if message == 'q':
            print("Goodbye!")
        else :
            print("It's not a number i can't add to the list, please try again. Q,q = quit")

    if message == "q" or message == "Q":
        stop_cycle = False


print("All positive integer: ", end = "" )
print(*array_list, sep = ", ")

print("Sum of first 2 value is: ", array_list[0] + array_list[1] )