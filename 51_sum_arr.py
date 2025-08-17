arr=list(map(int, input("Enter the elements in array :").split()))
sum=0

for i in range(len(arr)):
    sum += arr[i]
print(f"Sum of the array:{sum}")