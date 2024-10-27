from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = {}
        for char in s:
            hashmap[char] = hashmap.get(char,0)+ 1
        
        # Step 2: Create buckets (index represents frequency)
        max_freq = max(hashmap.values())
        buckets = [[] for i in range(max_freq+1)]
        
        for char, freq in hashmap.items():
            buckets[freq].append(char)
        print(buckets)
        
        # Step 4: Construct the result string by iterating buckets from high to low frequency
        result = ""
        for freq in range(max_freq, 0, -1):
            for char in buckets[freq]:
                result += (char * freq) 
        return result 
        
        # # Step 5: Join the result list to form the final string
        # return ''.join(result)

        
        


x=Solution()
s = "tree"
print(x.frequencySort(s))
# hashmap={}
#         for i in s:
#             hashmap[i] = hashmap.get(i,0)+1
#         sorted_list = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
#         print(sorted_list)
#         ans=""
#         for key in sorted_list:
#             ans+=key[0] * key[1]
#         return(ans)
