arr1=list(map(int, input("Enter the 1st array element: ").split()))
arr2=list(map(int, input("Enter the 2nd array element: ").split()))

product=[]
for i in range(len(arr1)):
   product.append(arr1[i] * arr2[i])

scalar_product=sum(product)
min_val=min(product)
   
print(f"Scalar Product of the vector is :{scalar_product}")
print(f"Minimum Scalar Product of the vector is :{min_val}")
