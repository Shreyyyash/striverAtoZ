def prime(num):
    k=2
    while k*k<=num:
        if num%k==0:
            return False
        k=k+1
    return True

k=20
primes=[1]*(k+1)
primes[0]=primes[1]=0
# print(primes)

for i in range(2,k+1):        
    if prime(i):          
        j=i*i         # for range 100 it will check for i till 10 i.e 2,3,5,7
        while j<=k:
            primes[j]=0
            j=j+i
        print(i,end=' ')
print()
print(primes)


# a=prime(131)
# print(a)