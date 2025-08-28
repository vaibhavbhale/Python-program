arr1=list(map(int, input("Enter the 1st array element: ").split()))
arr2=list(map(int, input("Enter the 2nd array element: ").split()))

scalar_product=0
for i in range(len(arr1)):
   scalar_product+=arr1[i] * arr2[i]
   
print(f"Scalar Product of the array is :{scalar_product} ")