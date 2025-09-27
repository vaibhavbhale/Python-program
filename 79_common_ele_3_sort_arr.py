arr1 = list(map(int, input("Enter elements of 1st array : ").split()))
arr2 = list(map(int, input("Enter elements of 2nd array : ").split()))
arr3 = list(map(int, input("Enter elements of 3rd array : ").split()))

arr1.sort()
arr2.sort()
arr3.sort()

def common_elements(arr1, arr2, arr3):
    i = j = k = 0
    result = []
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            result.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1
    return result

print("Common elements are:", common_elements(arr1, arr2, arr3))
