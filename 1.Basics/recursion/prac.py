def fibonacci(num):
    if num==1 or num==2:
        return 1
    ans= fibonacci(num-2) + fibonacci(num-1)
    return ans
a=fibonacci(6)
print(a)
