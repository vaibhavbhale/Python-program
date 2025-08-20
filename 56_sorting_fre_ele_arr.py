arr = list(map(int, input("Enter elements : ").split()))
freq_list = []

for num in set(arr):  
    freq_list.append((num, arr.count(num)))

freq_list.sort(key=lambda x: (-x[1], x[0]))

print("Element : Frequency")
for num, count in freq_list:
    print(f"{num} : {count}")
