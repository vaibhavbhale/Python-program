num = int(input("Enter the number: "))
flag = 0

if num < 2:
    flag = 1 
    
else:
    for i in range(2, num):
        if num % i == 0:
            flag = 1
            break

if flag == 1:
    print("Not a prime number")
else:
    print("Prime number")
