
def lowerBound(nums, n, target):
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        if target<nums[mid]:
            high=mid-1
        
        else:
            ans=mid
            low=mid+1
    return ans

nums=[1,2,8,10,11,12,19]
target=13
print(lowerBound(nums,len(nums),target))