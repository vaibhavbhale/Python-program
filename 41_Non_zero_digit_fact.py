def last_non_zero_digit(n):
    result = 1
    count2 = 0
    count5 = 0
    
    for i in range(1,n+1):
        num = i
        # Remove factors of 2
        while num % 2 == 0:
            num //= 2
            count2 += 1
        # Remove factors of 5
        while num % 5 == 0:
            num //= 5
            count5 += 1
        # Multiply remaining number
        result = (result * num) % 10

    for  _ in range(count2 - count5):
        result = (result * 2) % 10
    
    return result

n =int(input("Enter the digit :"))
print(f"Last non-zero digit of {n}! is {last_non_zero_digit(n)}")
