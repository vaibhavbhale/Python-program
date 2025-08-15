arr = list(map(int, input("Enter the elements: ").split()))
min= arr[0]
max = arr[0]

for i in range(len(arr)):
    if arr[i] < min:
        min = arr[i]
    if arr[i] > max:
        max = arr[i]

print("Smallest element is:", min)
print("Largest element is:", max)
