arr1 =list(map(int, input("Enter 1st array element:").split()))
arr2 =list(map(int, input("Enter 2nd array element:").split()))

merged =arr1 + arr2
merged.sort()

print("After merging the array elements in sorted order",merged)