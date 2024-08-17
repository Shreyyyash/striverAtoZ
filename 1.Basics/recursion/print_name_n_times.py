def printName(name,n,i):
    print(name)
    if i<n:
        return printName(name,n,i+1)
    return

printName('shreyash',5,1)

# def PN(n):
#     if n==0:
#         return
#     print('shreyash')
#     PN(n-1)

# PN(5)