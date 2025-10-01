def trap(height):
    l, r = 0, len(height) - 1
    res = 0
    lmax, rmax = height[l], height[r]

    while l < r:
        if lmax < rmax:
            l += 1
            lmax = max(lmax, height[l])
            res += (lmax - height[l])
        else:
            r -= 1
            rmax = max(rmax, height[r])
            res += (rmax - height[r])

    return res   

height = list(map(int, input("Enter the height : ").split()))

result = trap(height)
print("Trapped water is :", result)
