n=5
for i in range(n):
    for j in range(i+1):
        print(chr(n-i+j+64),end='')
    print()

# E
# DE
# CDE
# BCDE
# ABCDE