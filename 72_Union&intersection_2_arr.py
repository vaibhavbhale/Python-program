def accept():
    arr = []   
    n = int(input("Enter the number of elements:"))
    for i in range(n):
        a =(input("Enter element:"))
        arr.append(a)
    return arr

print("Enter the elements of 1st array:")
arr1 = accept()
print("Enter the elements of 2nd array:")
arr2 = accept()

def Union(a,b):
    res =list(set(a) | set(b))   
    print("Union of arrays:", res)

def Intersection(a,b):
    res = list(set(a) & set(b))  
    print("Intersection of arrays:", res)
    
Union(arr1, arr2)
Intersection(arr1, arr2)
