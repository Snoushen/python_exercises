####################################Task############
#5. Write a script to convert decimal to hexadecimal
#        Sample decimal number: 30, 4
#        Expected output: 1e, 04
####################################################
 
print("Enter a decimal number: ")
decimal1, decimal2 = int(input()),int(input())
print("Sample decimal number: ", end = "")
print(decimal1, decimal2, sep= ", ")

print("Hexadecimal: ", end = "")
print(hex(decimal1)[2:],hex(decimal2)[2:], sep =", ")
