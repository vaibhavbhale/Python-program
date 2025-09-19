'''Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal 
to the sum of elements at higher indexes.'''

def equilibrium_indexes(arr):
    total_sum = sum(arr)   
    left_sum = 0
    indexes = []
    
    for i, val in enumerate(arr):
        right_sum=total_sum - left_sum - val  
        
        if left_sum==right_sum:
            indexes.append(i)
        
        left_sum += val 
    return indexes

arr =list(map(int, input("Enter array elements:").split()))
print("Array:",arr)
print("Equilibrium Indexes:", equilibrium_indexes(arr))
