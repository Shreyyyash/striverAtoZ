from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        left=0
        right=n-1
        answer=0
        result=0
        
        if n==2:
            return (right-left) * min(height[right],height[left])
        
        while left<right:
            answer=(right-left) * min(height[right],height[left])
            result=max(answer,result)

            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
            
            
        return result

a=Solution()
height =[6,4,3,1,4,6,99,62,1,2,6]
print(a.maxArea(height))