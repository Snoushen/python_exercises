####################################Task###########################################################################################
#1 .Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
#        Sample data : 1, 5, 7, 23
#        Output :
#        List : [‘1', ' 5', ' 7', ' 23']
#        Tuple : (‘1', ' 5', ' 7', ' 23')
####################################################################################################################################
 
stop_cycle = True
array_list = []
array_typle = {}
print("We must create a tuple and list. Let's go")
while stop_cycle:
    message = input("Enter a number(q to complete): ")

    try:
        message = int(message)
        array_list.append(message)
    except ValueError:
        print("It's not a number i can't add to the list, please try again")

    if message == "q":
        stop_cycle = False







print("List: ",array_list, "\nTuple: ", tuple(array_list))
