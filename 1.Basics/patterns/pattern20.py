n=5
for i in range(2*n-1):
    if i<n:
        for j in range(i+1):
            print('*',end='')
    if i>n-1:
        for j in range(2*n-i-1):
            print('*',end='')
    for j in range(2*(n-i-1)):
        print(' ',end='')
    
    for j in range(2*(i-n+1)):
        print(' ',end='')
    if i<n:
        for j in range(i+1):
            print('*',end='')
    if i>n-1:
        for j in range(2*n-i-1):
            print('*',end='')
    print()

# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *