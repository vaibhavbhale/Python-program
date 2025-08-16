arr = list(map(int, input("Enter the elements: ").split()))
arr.sort(reverse=True)

print("Second largest element is:", arr[1])
