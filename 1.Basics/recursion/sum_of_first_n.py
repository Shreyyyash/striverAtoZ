## 1

# def Sum(num,i,summ):
#     # print(summ)
#     if i>num:
#         return summ    
#     summ=summ+i
#     i=i+1   
#     return Sum(num,i,summ)   
# a=Sum(6,1,0)
# print(a)

##2

# def sunN(num):
#     if num==0:
#         return 0   
#     ans=sunN(num-1)+num
#     print(ans)
#     return ans
# a=sunN(5)
# print(a)

##3

def SumN(n,i):
    if i>n:
        return 0
    ans=SumN(n,i+1)+i  
    print(ans)
    return ans   # final ans is 0+5+4+3+2+1

a=SumN(5,1)
print(a)

# 5
# 9
# 12
# 14
# 15
# 15 (final value of a)