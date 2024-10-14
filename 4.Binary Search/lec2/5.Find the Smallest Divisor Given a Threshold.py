import math
class Solution:
    def smallestDivisor(self, nums, threshold: int):
        minimum= 1
        maximum= max(nums)

        while minimum<=maximum:
            mid=(minimum+maximum)//2
            current=0
            
            for num in nums:
                current+=math.ceil(num/mid)

            if current<=threshold:
                maximum=mid-1
            else:
                minimum=mid+1
        
        return minimum
        
        for i in range(minimum,maximum+1):
            current=0
            for num in nums:
                current+=math.ceil(num/i)
            if current<=threshold:
                return i
        return -1

threshold = 6
# nums = [44,22,33,11,1]
nums = [1,2,5,9]
a=Solution()
print(a.smallestDivisor(nums,threshold))