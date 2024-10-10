#162
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # If the array has only one element, it's a peak
        if n == 1:
            return 0
        
        # Check if the first element or last element is the peak
        if nums[0] > nums[1]:
            return 0
        if nums[n - 1] > nums[n - 2]:
            return n - 1

        # Binary search from the second element to the second-last element
        left, right = 1, n - 2
        while left <= right:
            mid = (left + right) // 2

            # Check if nums[mid] is greater than both its neighbors
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            
            # If nums[mid] is greater than the left neighbor, move right
            if nums[mid] > nums[mid - 1]:
                left = mid + 1
            else:
                right = mid - 1
        
        # If no peak is found in the loop, return left (it will point to a peak)
        return left



nums = [1,2,1,2,1]
# nums = [1,2,1,3,5,6,4]
a=Solution()
print(a.findPeakElement(nums))

# n=len(nums)
#         ans=n
#         if n==1:
#             return 0
#         for i in range(n-1):
#             if nums[i]<nums[i+1]:
#                 ans=i+1
#             elif nums[i]>nums[i+1]:
#                 return i
#         return ans