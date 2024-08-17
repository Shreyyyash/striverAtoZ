# 1
# def factorial(num):
#     if num==1 or num==0:
#         return 1
#     else:
#         return num * factorial(num-1)
# a=factorial(5)
# print(a)

# 2
def factorial(num,i):
    if i>num-1:
        return 1
    i=i+1
    return factorial(num,i)*i
a=factorial(5,1)
print(a)