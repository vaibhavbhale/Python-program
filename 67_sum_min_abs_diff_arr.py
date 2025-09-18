arr = list(map(int, input("Enter numbers: ").split()))

arr.sort()
n = len(arr)
sum = 0

for i in range(n):
 if i == 0:
    sum += arr[1] - arr[0]     
 elif i == n-1:
    sum += arr[n-1] - arr[n-2]    
 else:
    sum += min(arr[i] - arr[i-1], arr[i+1] - arr[i])

print("Sum of minimum absolute difference:", sum)
