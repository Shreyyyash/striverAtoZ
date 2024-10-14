class Solution:
    def canMakeBouquets(self,bloomDay, m, k, day):
        bouquets=0
        flowers=0
        # iterate through whole array for that day
        for i in range(len(bloomDay)):
            if bloomDay[i]<=day:
                # if index i is less or equal to than "day" means flower is bloomed we increment flower
                flowers+=1
                if flowers==k:
                    # if flower size eual to k i.e size of bouquet increment bouquet
                    bouquets+=1
                    flowers=0
                
            else:
                # we only have to take adjacent flowers so if bloomDay[i]>day: 12 >day 7 we make flower zero
                flowers=0
            
            # if bouquets size if more or equal to m we return true for that day
            if bouquets>=m:
                return True
        
        return bouquets >= m
    
    def minDays(self,bloomDay,m,k):
        no_of_flowers = len(bloomDay)
        if no_of_flowers<m*k:
            return -1
        
        min_day = min(bloomDay)
        max_day = max(bloomDay)

        while min_day<=max_day:
            mid_day = (min_day+max_day)//2
            if self.canMakeBouquets(bloomDay, m, k, mid_day):
                max_day = mid_day - 1
            else:
                min_day = mid_day+1
        
        return min_day
    
        # for day in range(min_day, max_day + 1):
        #     # for each day check if we can make all bouquets
        #     if self.canMakeBouquets(bloomDay, m, k, day):
        #         return day

bloomDay = [7,7,7,7,12,7,7]
m = 2
k = 3
a=Solution()
print(a.minDays(bloomDay,m,k))