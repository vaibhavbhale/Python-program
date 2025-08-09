def hcf(a,b):
  if b==0:
    return a
  else:
    return  hcf(b,a % b)

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

print(f"The hcf of {num1} and {num2} is",hcf(num1,num2))