
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans=""
        count_of_opening =0
        count_of_closing =0

        for i in s:
            if i == "(" :
                if count_of_opening>0:
                    ans+=i
                count_of_opening+=1
            
            elif i==")":
                count_of_closing+=1
                if count_of_opening != count_of_closing:
                    ans+=i
            
            if count_of_closing==count_of_opening:
                count_of_opening=0
                count_of_closing=0
        return ans

        # another approach is similar only here we use one varibale to plus/minus check
        ans=""
        check=0
        for i in s:
            if i == "(":
                if check>0:
                    ans+=i
                check+=1
            if i == ")":
                check-=1
                if check>0:
                    ans+=i
        return ans


# s="(()())(())(()(()))"  # op "()()()()(())"
s="(()(()))"
# s="(()())(())" # op "()()()"

a=Solution()
print(a.removeOuterParentheses(s))