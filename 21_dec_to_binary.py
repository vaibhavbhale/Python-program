dec = int(input("Enter the decimal number: "))
bin = ""

if dec == 0:
    bin = "0"
    
    
else:
    while dec > 0:
        rem = dec % 2
        bin = str(rem) + bin
        dec = dec // 2

print("The binary number is", bin)