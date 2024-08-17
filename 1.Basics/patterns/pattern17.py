n=4
for i in range(n):
    for j in range(n-i):
        print(' ',end='')
    for j in range((2*i+2)//2):
        print(j+1,end='')
    for j in range(i):
        print(i-j,end='')
    print()
print()

#     1
#    121
#   12321
#  1234321

# same for chr

n=4
for i in range(n):
    for j in range(n-i):
        print(' ',end='')
    for j in range((2*i+2)//2):
        print(chr(j+1+64),end='')
    for j in range(i):
        print(chr(i-j+1+63),end='')
    print()

#     A
#    ABA
#   ABCBA
#  ABCDCBA