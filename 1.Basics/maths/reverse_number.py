def reverseNumber(num):
    ans=0
    while num!=0:
        remainder=num%10
        ans=ans*10+remainder
        num=num//10
    return ans

print(reverseNumber(num=1234))
