

from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # O(n+m)
        n=len(nums1)
        m=len(nums2)
        total_length = n + m
        median_index2 = total_length // 2
        median_index1 = median_index2 - 1
        count = 0
        element_at_index1, element_at_index2 = -1, -1

        i, j = 0, 0
        while i < n and j < m:
            if nums1[i]< nums2[j]:
                if count == median_index2:
                    element_at_index2 = nums1[i]
                if count == median_index1:
                    element_at_index1 =  nums1[i]
                count += 1
                i += 1
            else:
                if count == median_index2:
                    element_at_index2 = nums2[j]
                if count == median_index1:
                    element_at_index1 =  nums2[j]
                count += 1
                j += 1

        if total_length % 2 == 1:
            return float(element_at_index2)
        else:
            return float(element_at_index1+element_at_index2)/2

nums1 = [1, 4, 7, 10, 12]
nums2 = [2, 3, 6, 15]
a=Solution()
print(a.findMedianSortedArrays(nums1,nums2))

# O((m+n)log(m+n))
        # nums3=nums1+nums2
        # nums3.sort()
        # n=len(nums3)
        # if n%2==1:
        #     median = nums3[n//2]
        # else:
        #     median = (nums3[n//2]+nums3[n//2 -1 ]) / 2
        # return median 