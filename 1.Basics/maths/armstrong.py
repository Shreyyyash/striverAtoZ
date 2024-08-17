def CountDigit(num):
    # return len(str(num))
    count=0
    while num!=0:
        count=count+1
        num=num//10
    return count

def Armstrong(num):
    k=CountDigit(num)
    ans=0
    temp=num               # preserved num for comparison with ans
    while num!=0:
        remainder=num%10
        ans=ans+(remainder**k)
        num=num//10

    if ans==temp:
        print('Number is Armstrong')
    else:
        print('Number is Not Armstrong')

Armstrong(153)


    