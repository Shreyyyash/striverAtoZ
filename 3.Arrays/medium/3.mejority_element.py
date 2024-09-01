# Leetcode 169
# Optimal Approach: Moore’s Voting Algorithm:

def majorityElement(nums):
    candidate=None
    count=0
    for num in nums:
        if count==0:
            candidate=num
        if num==candidate:
            count+=1
        else:
            count-=1
    return candidate


nums=[2,2,1,1,1,2,2]
print(majorityElement(nums))

# time and space = O(n)
# n=len(nums)
#     hash_map={}
#     for i in range(n):
#         hash_map[nums[i]]=hash_map.get(nums[i],0)+1
#         if hash_map[nums[i]]>n//2:
#             return nums[i]

# also  there is another way --> sort array and find middle item