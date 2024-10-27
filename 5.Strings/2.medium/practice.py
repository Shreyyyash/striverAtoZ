class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_length =0
        n = len(s)
        left=0
        hashmap = {}
        
        for right in range(n):
            if s[right] in hashmap:
                left = max(left, hashmap[s[right]] + 1)
            hashmap[s[right]] = right
            max_length = max(max_length,right-left+1)
        print(hashmap)
        return max_length

x=Solution()
s="abcabcb"
print(x.lengthOfLongestSubstring(s))


# for left in range(n):
#             hashmap={}
#             substring = "" 
#             for right in range(left,n):
#                 if s[right] not in hashmap:
#                     substring += s[right]
#                     hashmap[s[right]] = True
#                     if len(substring)  > max_length:
#                         max_length = len(substring)
#                 else:
#                     break
#         return max_length