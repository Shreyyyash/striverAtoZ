def leftCount(nums,target):
    n=len(nums)
    start=0
    low,high=0,n-1
    while low<=high:
        mid=(low+high)//2
        if target==nums[mid]:
            start=mid
            high=mid-1
        elif target>nums[mid]:
            low=mid+1
        else:
            high=mid-1
    
    return start

def RightCount(nums,target):
    n=len(nums)
    end=0
    low,high=0,n-1
    while low<=high:
        mid=(low+high)//2
        if target==nums[mid]:
            end=mid
            low=mid+1
        elif target>nums[mid]:
            low=mid+1
        else:
            high=mid-1
    
    return end

def CountOccurance(nums,target):
    start_index= leftCount(nums,target)
    end_index=RightCount(nums,target)
    total_count =  end_index - start_index + 1
    return total_count

    


arr = [2, 4, 6, 8, 8, 8, 11, 13]
target=8
print(CountOccurance(nums=arr,target=target))