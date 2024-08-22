def missingNumber(nums):
    # O(n^2)
    # n=len(nums)
    # for i in range(n+1):
    #     if i not in nums:
    #         break
    # return i

    #O(n)
    # n=len(nums)
    # expected_sum=n*(n+1)//2
    # actual_sum=sum(nums)
    # result=expected_sum-actual_sum
    # return result

    n = len(nums)
    xor = 0
    
    # XOR all numbers in nums and all numbers from 0 to n
    for i in range(n):
        xor = xor^nums[i] ^ i
    
    # XOR with the last number (which is n)
    xor = xor^n
    
    return xor
nums=[9,6,4,2,3,5,7,0,1]
# nums=[0,1]
a=missingNumber(nums)
print(a)