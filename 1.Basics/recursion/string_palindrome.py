# iterative method
# def reverse(str):
#     ans=''
#     for i in str:
#         ans=i+ans
#     return ans
# a=reverse('yash')
# print(a)

# recursive method

def reverse(str):
    print(str[1:])
    if len(str)==0:
        return str
    ans=reverse(str[1:])+str[0]
    # print(ans)
    return ans
    # print 0th index and then 1st index will become 0th index

def str_palindrome(str):
    if str==reverse(str):
        print("IsPalindrome")
    else:
        print('NotPalindrome')
a=str_palindrome('yash')
print(a)

#2
# def is_pali(str,s,e):
#     if str[s] != str[e]:
#         return False
#     if s>e:
#         return True
#     return is_pali(str,s+1,e-1)
# str='nayan'
# b= is_pali(str,0,len(str)-1)
# print(b)

#3
# def is_palindrome(s):
#     if len(s) <= 1:
#         return True
#     elif s[0] != s[-1]:
#         return False
#     else:
#         return is_palindrome(s[1:-1])

# string = "nayan"
# result = is_palindrome(string)
# if result:
#     print(f"{string} is a palindrome")
# else:
#     print(f"{string} is not a palindrome")