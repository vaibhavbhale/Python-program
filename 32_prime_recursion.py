def prime_recursive(num, i=2):
    if num < 2:
        return False
    if i == num:
        return True
    if num % i == 0:
        return False
    return prime_recursive(num, i + 1)


num = int(input("Enter the number: "))
if prime_recursive(num):
    print("Prime number")
else:
    print("Not a prime number")
