#disjoint array means there is no common elements between the both arrays

arr1=set(map(int, input("Enter the numbers in the 1st array : ").split()))
arr2=set(map(int, input("Enter the numbers in the 2nd array : ").split()))

def disjoint(arr1,arr2):
 intersection=arr1.intersection (arr2)
 
 if intersection:
     print("Array are not disjoint,the common element between them are:",intersection)
 else:
     print("Arrays are disjoints")
     
disjoint(arr1,arr2)