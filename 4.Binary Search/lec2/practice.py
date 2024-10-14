import math
class Solution:
    def minSpeed(self,piles,h):
        right=max(piles)
        left=1

        while left<=right:
            mid=(left+right)//2
            print(mid)
            hours=0
            for pile in piles:
                hours+= math.ceil(pile/mid)
            if hours<=h:
                right=mid-1
            else:
                left=mid+1
        return left



piles = [3,6,7,11]
h = 8
a=Solution()
print(a.minSpeed(piles,h))