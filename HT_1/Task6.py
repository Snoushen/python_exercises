####################################Task################################################
#6. Write a script to check whether a specified value is contained in a group of values.
#        Test Data :
#        3 -> [1, 5, 8, 3] : True
#        -1 -> (1, 5, 8, 3) : False
########################################################################################
  
stop_cycle = True
array_list = []

print("Please enter a namber(q or Q for quit)")
while stop_cycle:

    message = input()

    try:
        print("Your number ")
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
