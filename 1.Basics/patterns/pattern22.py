n=7
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print('4',end='')
        elif i==1 or j==1 or i==n-2 or j==n-2:
            print('3',end='')
        elif i==2 or j==2 or i==n-3 or j==n-3:
            print('2',end='')
        else:
            print('1',end='')
    print()

# 4444444
# 4333334
# 4322234
# 4321234
# 4322234
# 4333334
# 4444444