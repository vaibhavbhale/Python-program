# the program to count the frequency of elements in an array in python programming language. 
# We are given with an array and need to print each element along its frequency.

arr = list(map(int, input("Enter the elements to count frequency : ").split()))

frequency =[]

for num in arr:
    if num not in frequency:  
        count = arr.count(num)  
        print(f"{num} occurs {count} time(s)")
        frequency.append(num)
