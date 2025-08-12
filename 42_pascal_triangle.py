def pascal_tri(n, k):
   
    if k == 0 or k == n:
        return 1
    return pascal_tri(n-1, k-1) + pascal_tri(n-1, k)

rows = int(input("Enter number of rows: "))

for i in range(rows):
    print(" " * (rows - i), end="")
    for j in range(i + 1):
        print(pascal_tri(i, j), end=" ")
    print()