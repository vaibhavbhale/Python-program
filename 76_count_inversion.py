#inversions are pairs in an array which are not placed in sorted order

arr =list(map(int, input("Enter the inversion elements:").split()))
inversion = 0

for i in range(len(arr)):
  for j in range(len(arr)):
    if arr[i] > arr[j] and i < j:   
     inversion+= 1
     print((arr[i], arr[j]), end="\n")

print("Total inversions:",inversion)
