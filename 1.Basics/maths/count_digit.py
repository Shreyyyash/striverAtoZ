
def CountDigit(num):
    count=0
    while num!=0:
        count+=1
        num=num//10
    return count

print(CountDigit(1234))

