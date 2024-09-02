# Kadane's Algorithm, maximum subarray sum

def maxSubArray(nums):
    n=len(nums)
    sum=0
    total_sum = nums[0]
    for i in range(n):
        sum=sum+nums[i]
        total_sum=max(total_sum,sum)
        if sum < 0:
            sum = 0
       
    return total_sum
    

nums=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums=nums))

# for O(n) if sum is less than 0 make it sum=0
# n=len(nums)
#     sum=0
#     total_sum=0
#     for i in range(n):
#         sum=sum+nums[i]
#         total_sum=max(total_sum,sum)
#         if sum < 0:
#             sum = 0
       
#     return total_sum

# n=len(nums)
#     total_sum=-43550
#     for i in range(n):
#         sum=0
#         for j in range(i,n):
#             sum=sum+nums[j]
#             total_sum=max(total_sum,sum)
    
#     return total_sum