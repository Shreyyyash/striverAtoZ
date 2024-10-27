from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  
            return ""
        prefix = strs[0]
        n=len(prefix)
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

x=Solution()
strs = ["flower","flow","flight"]
print(x.longestCommonPrefix(strs))