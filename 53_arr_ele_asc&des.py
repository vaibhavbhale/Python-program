arr=list(map(int, input("Enter the element in array:").split()))

arr.sort()
print(f"Element in asscending order{arr}")

arr.sort(reverse=True)
print(f"Elements in descending order{arr}")