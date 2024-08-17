'''
n=5
for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print()
for i in range(n):
    for j in range(n-i-1):
        print('*',end='')
    print()
    '''
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

#Alternate using one loop
n=7
for i in range(2*n-1):
    if i<n:
        for j in range(i+1):
            print('*',end='')
    else:
        for j in range(2*n-i-1):
            print('*',end='')
    print()