def searchRange(nums, target):
    n=len(nums)

    # Lower Bound
    def StartIndex(nums,target):
        low=0
        high=n-1
        start=-1
        while low<=high:
            mid=(low+high)//2
            if target==nums[mid]:
                start=mid
                high=mid-1  # check for the left appearance 
            elif target>nums[mid]:
                low=mid+1
            else:
                high=mid-1
        return start
    
    # Upper Bound
    def EndIndex(nums,target):
        low=0
        high=n-1
        end=-1
        while low<=high:
            mid=(low+high)//2
            if target==nums[mid]:
                end=mid
                low=mid+1           # check for the last right appearance 
            elif target > nums[mid]:
                low=mid+1
            else:
                high=mid-1
        return end
    
    return [StartIndex(nums,target),EndIndex(nums,target)]

nums=[5,7,7,8,8,8,8,8,8,8,8,8,8,10,13,13,13]
target=8
print(searchRange(nums,target))

# n=len(nums)
#         start=-1
#         end=-1

#         for i in range(n):
#             if nums[i]==target:
#                 if start==-1:
#                     start=i
#                 end=i
#         return [start,end]


# n=len(nums)
#     left=right=-1
#     if target not in nums:
#         return [left,right]
#     for i in range(n):
#         if nums[i]==target:
#             right=i
    
#     for i in range(n):
#         if nums[i]==target:
#             left=i
#             break
    
#     return [left,right]