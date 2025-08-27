arr =list(map(int, input("Enter the element in the array :").split()))

repeat_ele=[]
non_repeat_ele=[]

for i in arr:
    if arr.count(i) > 1 and i not in repeat_ele:
        repeat_ele.append(i)
    elif arr.count(i) == 1 and i not in non_repeat_ele:
        non_repeat_ele.append(i)

print("Repeating elements in the array are:", repeat_ele)
print("Non Repeating elements in the array are:", non_repeat_ele)
