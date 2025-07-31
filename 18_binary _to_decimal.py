num=int(input("Enter the binary number:"))
dec=0
i=0

while(num!=0):
    rem=num%10
    dec=dec+rem*pow(2,i)
    num=num//10
    i=i+1
    
print("The decimal number is",dec)