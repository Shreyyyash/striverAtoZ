def searchInsert(nums,target):
    low=0
    high=len(nums)-1
    ans=len(nums)

    while low<=high:
        mid=(low+high)//2
        if target==nums[mid]:
            return mid
        
        elif target<nums[mid]:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    
    return ans




nums = [1,3,5,6]
target = 2
print(searchInsert(nums,target))