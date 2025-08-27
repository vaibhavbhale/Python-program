arr =list(map(int, input("Enter duplicate element in the array :").split()))

dup_ele=[]
for i in arr:
    if arr.count(i) > 1 and i not in dup_ele:
        dup_ele.append(i)
        
print(f"duplicate element in array: {dup_ele}")
