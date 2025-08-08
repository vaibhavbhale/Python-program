def smallest(arr):
    n = len(arr)
    min_val = arr[0]  
    for i in range(n):
        if arr[i] < min_val:
            min_val = arr[i]
    return min_val

input_str = input("Enter the array elements: ")
input_list = input_str.split()

arr = []
for item in input_list:
    arr.append(int(item))

print("Smallest element is:", smallest(arr))
