'''A Number that is equal to the sum of the factorial of it's individual digits is known as Strong Number.'''

n = int(input("Enter the number: "))
org = n
sum = 0 

while n > 0:
    digit = n % 10  
    fact = 1
   
    for i in range(1, digit + 1):
        fact = fact * i
    sum=sum+ fact  
    n= n//10  

if sum == org:
    print(f"{org} is a strong number.")
else:
    print(f"{org} is not a strong number.")
