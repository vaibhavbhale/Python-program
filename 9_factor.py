divisor = int(input("Enter the number: "))
num = int(input("Enter the range of numbers: "))

for i in range(1, num + 1):
    if divisor % i == 0:
        print(f"{i} is a divisor of {divisor}")
    else:
        print(f"{i} is not a divisor of {divisor}")


