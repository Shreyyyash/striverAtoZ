def twoSum(nums, target):
    n=len(nums)
    hash_map={}
    for i in range(n):
        if target-nums[i] in hash_map:
            return [hash_map[target-nums[i]],i]
        else:
            hash_map[nums[i]]=i
        
nums = [3,2,3]
target = 6
a=twoSum(nums,target)
print(a)


# brute force
# for i in range(n):
#         for j in range(i+1,n):
#             if nums[i]+nums[j]==target:
#                 return [i,j]
