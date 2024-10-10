#540

def singleNonDuplicate(nums):
    n=len(nums)
    left,right=0,n-1
    if n==1:
        return nums[0]       
    if nums[n-1]!=nums[n-2]:
        return nums[n-1]

    while left<=right:
        mid=(left+right)//2
        # if single middle element is found
        if (nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]):
            return nums[mid]

        elif (mid % 2==1 and nums[mid]==nums[mid-1]) or (mid % 2==0 and nums[mid]==nums[mid+1]):
            left=mid+1
        
        else:
            right=mid-1
          
    return nums[mid]
nums = [3,3,7,7,10,11,11]
# nums = [1,1,2,3,3,4,4,8,8]
# nums = [1,1,2,2,3,3,4,4,5,5,6,7,7,8,8]
print(singleNonDuplicate(nums))