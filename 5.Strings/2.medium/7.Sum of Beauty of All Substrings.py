class Solution:
    def beautySum(self, s: str) -> int:
        total_beauty = 0
        left=0
        right=0
        
        for left in range(len(s)):
            hashmap = {}
            for right in range(left,len(s)):
                hashmap[s[right]] = hashmap.get(s[right],0)+1

                maxi= max(hashmap.values())
                mini = min(value for value in hashmap.values() if value>0) 
                total_beauty+=(maxi-mini)
                
                    
        return total_beauty


x=Solution()
s="aabcbaas"
print(x.beautySum(s))