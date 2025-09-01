arr =list(map(int, input("Enter array elements: ").split()))
max_product = arr[0]

for i in range(len(arr)):
    product = 1
    for j in range(i, len(arr)):
        product *= arr[j]
        max_product = max(max_product, product)

print("Maximum product subarray is:", max_product)
