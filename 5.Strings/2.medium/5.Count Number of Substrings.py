# There is optimised solution for this one
def countSubstrings(s,k):
    n=len(s)
    left = 0
    right = 0
    result = set()
    for left in range(n):
        chars = set()
        for right in range(left,n):
            chars.add(s[right])
            if len(chars) > k:
                break
            if len(chars) == k:
                result.add(s[left:right+1])
    return result


s="aba"
k=2
print(countSubstrings(s,k))