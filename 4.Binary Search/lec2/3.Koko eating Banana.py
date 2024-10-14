import math

class Solution:
    def minEatingSpeed(self,piles, h):      
        left=1
        right=max(piles)

        while left<=right:
            mid=(left+right)//2
            hours=0
            for pile in piles:
                hours+=math.ceil(pile/mid)
            # print("{}->{}".format(mid,hours))
            
            if hours<=h:
                # here we have to find min value k that is minimum eating speed
                right=mid-1

            elif hours>h:
                left=mid+1
        
        return left
        
piles = [30,11,23,4,20]
h=6
# piles = [3,6,7,11]
# h = 8
a=Solution()
print(a.minEatingSpeed(piles,h))


# n = max(piles) 
        # k = 1  
        # while k <= n+1:
        #     hours = 0  

        #     for pile in piles:
        #         hours += math.ceil(pile / k)  

        #     if hours <= h:
        #         return k
        #     else:
        #         k += 1 

        # return k  