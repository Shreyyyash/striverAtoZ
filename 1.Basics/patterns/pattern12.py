n=4
for i in range(n):
    for j in range(i+1):
        print(j+1,end='')
    
    for j in range((n-i)*2-2):
        print( ' ',end='')

    for j in range(i+1):
        print(i-j+1,end='')


    print()

# 1||||||1
# 12||||21
# 123||321
# 12344321