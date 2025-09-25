def merge(intervals):  
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    for interval in intervals:
     if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
     else:
            merged[-1][1] = max(merged[-1][1], interval[1])
            
    return merged

arr = list(map(int, input("Enter intervals :").split()))  
intervals = []
for i in range(0, len(arr), 2):  
    intervals.append([arr[i], arr[i+1]])  

print("Merged:", merge(intervals))  
