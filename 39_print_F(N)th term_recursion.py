def term(calculated, current, n):
    result = 0
    while current != n + 1:
        cur = 1
        for i in range(calculated, calculated + current):
            cur *= i
        calculated = i + 1
        result += cur
        current += 1
    return result

n = int(input("Enter the value of n: "))
print("The term is:",term(1,1,n))
