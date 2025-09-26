def subarray_sum_zero(arr):
    n=len(arr)

    for i in range (n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            if sum==0:
              return arr[i:j+1]#return the subarray
    return None
    
arr =list(map(int, input("Enter the elements in subarray:").split()))
result=subarray_sum_zero(arr)

if result:
  print("The subarray with sum equal to 0 is",result)
else:
  print("No subarray with sum equal to 0 found")  