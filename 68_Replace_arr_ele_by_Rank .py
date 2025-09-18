def replace_by_ranks(arr):
    sorted_arr= sorted(set(arr))

    rank_dic = {}
    rank = 1
    for val in sorted_arr:
      rank_dic[val] = rank
      rank += 1
    
    ranked_arr = []
    for val in arr:
      ranked_arr.append(rank_dic[val])
    return ranked_arr

arr = list(map(int, input("Enter array elements: ").split()))
print("Original array:", arr)
print("Ranked array: ", replace_by_ranks(arr))
