def CheckPrime(num):
    ''' if num==2:
        return True
    for i in range(2,num//2):
        if num%i==0:
            return False    
        return True
        '''
    # optimised solution
    if num<2:
        return False
    if num==2:
        return True
    k=2
    while k*k<=num:
        if num%k==0:
            return False
        k=k+1               # upto root of num
    return True
      
a=CheckPrime(1)
print(a)