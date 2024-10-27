class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        # as we move from left to right every possible rotation can be present in s+s i.e abcdeabcde
        return goal in (s + s)
    
        # n=len(s)
        # rotation=0
        # check =""
        # while rotation<n:
        #     for i in range(n):
        #         check += s[(i + rotation) % n]
        #     if check == goal:
        #         return True
        #     else:
        #         check=""
        #         rotation +=1
        # return False

x=Solution()
s = "abcde"
goal = "cdeab"
print(x.rotateString(s,goal))