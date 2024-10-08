def FindMin(nums):
    n=len(nums)
    left=0
    right=n-1
    ans=34324233423
  

    while left<=right:
        mid=(left+right)//2
        if nums[left] <= nums[right]:
            ans = min(ans, nums[left])
            break

        if nums[left]<=nums[mid]:
            ans=min(ans,nums[left])
            left=mid+1
        
        elif nums[mid]<nums[right]:
            ans=min(ans,nums[mid])
            right=mid-1

    return ans

        
        

nums = [3,4,5,1,2]
print(FindMin(nums))