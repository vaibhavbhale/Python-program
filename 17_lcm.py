'''The LCM of two numbers is the smallest number which can divide the both numbers equally.'''

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

maxnum=max(num1,num2)

while(True):
    if(maxnum % num1==0 and maxnum % num2==0):
        break
    maxnum=maxnum+1

print(f"The lcm {num1} and {num2} is {maxnum}")
        