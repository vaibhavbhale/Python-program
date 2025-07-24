n=int(input("Enter the number:"))
fact=1

if n<0:
    print("factorial doesn't exist for negative number")

elif(fact==0):
  print("factorial of 0 is 1")

else:
    for i in range(1,n+1):
        fact=fact*i;
print("Factorial is:",fact)