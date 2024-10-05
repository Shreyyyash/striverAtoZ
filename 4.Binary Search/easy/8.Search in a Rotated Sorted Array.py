# First, we identify the sorted half of the array. 
# Once found, we determine if the target is located within this sorted half. 
# If not, we eliminate that half from further consideration. 
# Conversely, if the target does exist in the sorted half, we eliminate the other half.

def search(nums,target):
    nums.sort()
    n=len(nums)
    low,high=0,n-1
    pivot=0
    
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            pivot=mid
        elif target < nums[mid]:
            low = mid+1
        else:
            high = mid-1
    return pivot


nums = [4,5,6,7,8,0,1,2]
target = 0
print(search(nums,target))