def NoOfRotation(nums):
    n = len(nums)
    left=0
    right=n-1
    ans=524523345634
    index=n

    while left<=right:
        mid=(left+right)//2
        if nums[left] <= nums[right]:
            if ans>nums[left]:
                ans=nums[left]
                index=left
                break
        
        if nums[left]<=nums[mid]:
            if ans>nums[left]:
                ans=nums[left]
                index=left
            left=mid+1
            

        elif nums[mid]<nums[right]:
            if ans>nums[mid]:
                ans=nums[mid]
                index=mid
            right=mid-1
           
    
    return index

    
nums = [5, 6, 1, 2, 3, 4]
print(NoOfRotation(nums))

# for i in range(n):
#         if nums[i] > nums[(i + 1) % n]:
#             return (i + 1) % n