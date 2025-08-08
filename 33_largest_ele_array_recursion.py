def largest(arr):
    n = len(arr)
    max_val = arr[0]  
    for i in range(n):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val

arr =(input("Enter the array elements:"))
print(f"largest element in the array is:{largest(arr)}")