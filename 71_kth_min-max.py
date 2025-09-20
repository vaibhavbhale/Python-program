def kth_min_max(arr,a):
    arr.sort()
    
    min = arr[a-1]
    max = arr[-a]
    return min,max

arr =list(map(int, input("Enter array elements:").split()))
a =int(input("Enter the kth element:"))

min, max = kth_min_max(arr, a)
print(f"{a}th Minimum element is :{min}")
print(f"{a}th Maximum element is :{max}")
