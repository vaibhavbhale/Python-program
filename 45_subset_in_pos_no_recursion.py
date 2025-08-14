def subsets(nums, index=0, current=[]):
    if index == len(nums):
        print(current)
        return
    
    subsets(nums, index + 1, current + [nums[index]])
    subsets(nums, index + 1, current)

nums = list(map(int, input("Enter elements separated by space: ").split()))
subsets(nums)
