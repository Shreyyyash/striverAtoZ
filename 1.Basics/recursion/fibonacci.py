# iterative
# def fibonacci(num):
#     a=0
#     b=1  
#     for i in range(1,num):
#         c=a+b
#         a=b
#         b=c
#     return b
# a=fibonacci(6)
# print(a)

# recursive

def fibonacci(num):
    if num==1 or num==2:
        return 1
    ans= fibonacci(num-2) + fibonacci(num-1)
    return ans
a=fibonacci(6)
print(a)

# using both
# def fibonacci(n):
#     def fibonacci_helper(a, b, count):
#         if count == 0:
#             return a
#         else:
#             return fibonacci_helper(b, a + b, count - 1)

#     if n <= 0:
#         return 0
#     else:
#         return fibonacci_helper(0, 1, n)

# print(fibonacci(7))  # Output the 7th Fibonacci number