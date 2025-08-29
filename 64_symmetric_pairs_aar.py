def findSymmetricPairs(arr):
    pairs = {}               
    symmetric_pairs = []    

    for pair in arr:
      x, y = pair
      if (y, x) in pairs:         
         symmetric_pairs.append((x, y))
      else:
         pairs[(x, y)] = True      

    return symmetric_pairs

pairs = [(3, 4), (1, 2), (5, 2), (7, 10), (4, 3), (2, 5)]
symmetric_pairs = findSymmetricPairs(pairs)

for pair in symmetric_pairs:
    print(pair)
