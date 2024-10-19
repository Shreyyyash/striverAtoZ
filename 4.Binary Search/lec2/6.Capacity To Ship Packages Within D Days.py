from typing import List
import math
class Solution:
    def isPossible(self,weights,capacity,days):
        day_count = 1
        current_weight = 0
        
        for weight in weights:
            if current_weight + weight > capacity:
                day_count += 1
                current_weight = weight
                if day_count > days:
                    return False
            else:
                current_weight += weight
        return day_count <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_weight = max(weights)
        max_weight = sum(weights)
        
        while min_weight<=max_weight:
            mid_weight=(min_weight+max_weight)//2
            
            if self.isPossible(weights,mid_weight,days):
                max_weight=mid_weight-1
            else:
                min_weight=mid_weight+1
        return min_weight

        
        # total_weight = sum(weights)
        
        # for capacity in range(max_weight, total_weight + 1):
        #     if self.isPossible(weights,capacity,days):
        #         return capacity
            

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
a=Solution()
print(a.shipWithinDays(weights,days))