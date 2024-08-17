'''
n=5

for i in range(5):
    for j in range(5-i-1):
        print(' ',end='')

    for j in range(2*i+1):
        print('*',end='')

    print()
for i in range(n):
    for j in range(i):
        print(' ',end='')
    for j in range(2*(n-i)-1):
        print('*',end='')   
    print()
'''
#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *
# Alternate Solution
    
n=7

for i in range(2*n):
    if i<n:
        for j in range(n-i-1):
            print(' ',end='')

        for j in range(2*i+1):
            print('*',end='')
    else:            
        for j in range(i-n):
            print(' ',end='')
        for j in range((2*n-1)-(i-n)*2):
            print('*',end='')  
  
    print()
