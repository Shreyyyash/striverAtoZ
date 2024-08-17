n=5

for i in range(2*n):
    for j in range(n-i):
        print('*',end='')
    
    for j in range(i-n+1):
        print('*',end='')
    if i<n:
        for j in range(i*2):
            print(' ',end='')
    if i>n-1:
        for j in range((2*n-i-1)*2):
            print(' ',end='')
    
    for j in range(n-i):
        print("*",end='')

    for j in range(i-n+1):
        print("*",end='')
    print()

# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********