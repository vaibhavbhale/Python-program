def subset_sums(arr, index, current_sum, result):
    if index == len(arr):
        result.append(current_sum)
        return
    
    # Include current element
    subset_sums(arr, index + 1, current_sum + arr[index], result)
    
    # Exclude current element
    subset_sums(arr, index + 1, current_sum, result)


# Take input and convert to list of integers
arr = list(map(int, input("Enter the array elements: ").split()))
result = []

subset_sums(arr, 0, 0, result)
print("Sums of all subsets:", result)