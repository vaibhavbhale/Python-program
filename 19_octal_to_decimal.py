octal = int(input("Enter the octal number: "))
dec = 0
i = 0

while octal != 0:
    rem = octal % 10
    dec =dec + rem *pow(8,i)
    octal = octal // 10
    i += 1

print("The decimal number is", dec)
