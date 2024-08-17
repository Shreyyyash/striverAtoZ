n=5
for i in range(n):
    for j in range(i+1):
        print((i+j+1)%2,end='')

        # if (i+j)%2==0:
        #     print(1,end='')
        # else:
        #     print(0,end='')
    print()

# calculate sum of i+j and find if it is even or odd
# 1
# 01
# 101
# 0101
# 10101 