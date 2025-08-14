a = (input("Enter the elements:"))
max_ele = a[0]

for i in range(len(a)):
  if a[i] > max_ele:
     max_ele = a[i]

print (max_ele)