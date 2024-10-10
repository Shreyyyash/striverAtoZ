def floor_and_ceiling(nums,target):
    floor=None
    ceiling=None
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        
        if target==nums[mid]:
            return target, target

        elif target<nums[mid]:
            ceiling=nums[mid]
            high=mid-1
        else:
            floor=nums[mid]
            low=mid+1

    return floor,ceiling

nums=[3, 4, 4, 7, 8, 10]
target=5
print(floor_and_ceiling(nums,target))