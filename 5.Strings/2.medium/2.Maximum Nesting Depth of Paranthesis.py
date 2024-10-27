class Solution:
    def maxDepth(self, s: str) -> int:
        count_open = 0
        count_close = 0
        depth = 0
        max_depth=0
        for i in s:
            if i == "(":
                count_open +=1
            elif i == ")":
                count_close +=1
            depth = count_open - count_close
            max_depth = max(depth,max_depth)
        return max_depth