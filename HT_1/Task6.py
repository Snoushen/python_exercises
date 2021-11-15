stop_cycle = True
array_list = []

print("Please enter a namber(q or Q for quit)")
while stop_cycle:
    message = input()

    try:
        message = int(message)
        array_list.append(message)
    except ValueError:
        if message == 'q':
            print("Goodbye!")
        else :
            print("It's not a number i can't add to the list, please try again. Q,q = quit")

    if message == "q" or message == "Q":
        stop_cycle = False

print(array_list)

print("Enter the number to check on the list: ")
check_number = int(input()) in array_list

print(check_number)

