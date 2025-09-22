arr =list(map(int, input("Enter array element:").split()))
max_sum = 0
current_sum = 0

for num in arr:
   current_sum += num
   if current_sum < 0:
      current_sum = 0
   if current_sum > max_sum:
      max_sum = current_sum

print("Maximum sum of subarray:", max_sum)
