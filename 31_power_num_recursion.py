def power(a,b):
    if b!=0:
        return a * power(a,b-1)
    else:
        return 1

a=int(input("Enter the base:"))
b=int(input("Enter the expression:"))

print(f"the power of {a} is {b} = ",power(a,b))