'''The HCF or GCD of two integers is the largest integer that can exactly divide both numbers (without a remainder).'''

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

if num1>num2:
    min=num1
else:
    min=num2
    
for i in range(1,min+1):
    if num1%i==0 and num2%i==0:
        hcf=i
        
print(f"The hcf/gcd of two number is:{hcf}")  
