# this can be optimised
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n=len(s)
        max_palindrome = s[0]
        # odd string
        for middle in range(n):
            left =middle-1
            right = middle+1
            while left >=0 and right <n and s[left] == s[right]:
                if right-left+1> len(max_palindrome):
                    max_palindrome = s[left:right+1]
                left-=1
                right +=1
        # even string
        for middle2 in range(n):
            left = middle2
            right =middle2 +1
            while left >=0 and right <n and s[left] == s[right]:
                if right-left+1> len(max_palindrome):
                    max_palindrome = s[left:right+1]
                left-=1
                right +=1

        return max_palindrome


    
x=Solution()
s = "cbba"
print(x.longestPalindrome(s))

# n=len(s)
#         chr_string = ""
#         max_len = 0
#         max_string =""
#         for left in range(n):
#             chr_string = ""
#             for right in range(left,n):
#                 chr_string += s[right]
#                 if self.is_palindrome(chr_string):
#                     curr_len = len(chr_string)
#                     if curr_len > max_len:
#                         max_len = curr_len
#                         max_string = s[left:right+1]
        
#         return max_string
    
#     def is_palindrome(self,chr_string):
#         return chr_string == chr_string[::-1]
