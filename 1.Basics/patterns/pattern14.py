n=5
for i in range(n):
    for j in range(i+1):
        print(chr(j+65),end=' ')
    print()

# A  value of chr(65)=A and so on...
# A B
# A B C
# A B C D
# A B C D E