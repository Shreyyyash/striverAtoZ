class Solution:
    def myAtoi(self, s: str) -> int:
        n=len(s)
        i=0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        is_positive = True
        result = 0
        while i < n and s[i] == ' ':
            i += 1
        if i < n and (s[i]== "-" or s[i]=="+"):
            if s[i]=="-":
                is_positive = False
            i+=1
        
        while i<n and s[i].isnumeric():
            digit = ord(s[i]) - ord("0")                   
            result = result * 10 + digit
            i+=1
            if is_positive and result > INT_MAX:
                return INT_MAX
            if not is_positive and -result < INT_MIN:
                return INT_MIN  

        return result if is_positive else -result


x=Solution()
s = "-91283472332"
print(x.myAtoi(s))

# s = s.strip()

#         sign = 1
#         num = 0
#         for i in range(len(s)):
#             if i ==0:
#                 if s[i] == "-":
#                     sign = -1
#                 elif s[i] == "+":
#                     sign = 1
#                 elif s[i].isdigit():
#                     num = num*10 + int(s[i])
#                 else:
#                     break
#             else:
#                 if s[i].isdigit():
#                     num = num*10 + int(s[i])
#                 else:
#                     break
                    
#         # Apply the sign to the number
#         num *= sign
        
#         # Clamp the number within the 32-bit signed integer range
#         INT_MAX = 2**31 - 1
#         INT_MIN = -2**31
        
#         if num > INT_MAX:
#             return INT_MAX
#         elif num < INT_MIN:
#             return INT_MIN
        
#         return num