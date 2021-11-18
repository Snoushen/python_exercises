####################################Task####
#4. Write a script to concatenate N strings.
############################################

N = int(input("Enter a number of concatenation string: "))

conc_string = ""

for i in range(N):
    conc_string += input("Enter a string to concanate: ")

conc_string = conc_string.replace(" ","")
print("Result: ",conc_string)




"""
stop_cycle = True

concatenate_string = ''

while stop_cycle:
    concatenate_second_string = input("Enter a string that you want a concanate(q to exit from concatenation)\n")

    if concatenate_second_string == 'q':
        break

    concatenate_string += concatenate_second_string

print("Result = ",concatenate_string)
"""
