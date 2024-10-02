def binary_search(nums,target):
    low=0
    high=len(nums)-1
    
    while low<high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid        
        elif target>nums[mid]:
            low=mid+1
        else:
            high=mid-1
    

# nums=[-1,0,3,5,9,12]
# target=9
# print(binary_search(nums,target))

# Recursive Approcch

def binary_search_recursion(nums,target,low,high):
    mid=(low+high)//2
    if nums[mid]==target:
        return mid
    
    elif target>nums[low]:
        return binary_search_recursion(nums,target,low=mid+1,high=high)
    
    else:
        return binary_search_recursion(nums,target,low=low,high=mid-1)

nums=[-1,0,3,5,9,12]
target=9
low=0
high=len(nums)
print(binary_search_recursion(nums,target,low,high))