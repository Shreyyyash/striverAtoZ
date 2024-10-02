def upperBound(nums,target):
    low=0
    high=len(nums)-1
    ans=len(nums)
    while low<=high:
        mid=(low+high)//2
        if target<nums[mid]:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

nums=[1,2,8,10,11,12,19]
target=5
print(upperBound(nums,target))