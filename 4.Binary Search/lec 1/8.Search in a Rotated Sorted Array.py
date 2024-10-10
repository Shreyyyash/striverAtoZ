# First, we identify the sorted half of the array. 
# Once found, we determine if the target is located within this sorted half. 
# If not, we eliminate that half from further consideration. 
# Conversely, if the target does exist in the sorted half, we eliminate the other half.

def search(nums,target):
    n=len(nums)
    left,right=0,n-1

    while left<=right:
        mid=(left+right)//2
        if target==nums[mid]:
            return mid
        
        # Check if the left half is sorted
        if nums[left]<=nums[mid]:
            # If target is in the left sorted half
            if nums[left]<=target<nums[mid]:
                right=mid-1
            else:
                left=mid+1
        
        # Else, the right half must be sorted
        elif nums[mid]<nums[right]:
            # If target is in the right sorted half
            if nums[mid]<target<=nums[right]:
                left=mid+1
            else:
                right=mid-1
    
    return -1
    


nums = [4,5,6,7,8,0,1,2]
target = 0
print(search(nums,target))