def Prime(num):
    k=2
    while k*k<=num:
        if num%k==0:
            return False         
        k=k+1
    return True

k=20
primes=[1]*(k+1)
primes[0]=primes[1]=0
'''
for i in range(2,k+1):   # it will check all i/p from 2 to 20
    if Prime(i):
        primes[i]=1
    else:
        primes[i]=0
print(primes)
'''

for i in range(2,k+1):
    if primes[i]==1:
        j=i*i            # prime no behind 49 will already filled by 7-i
        while j<=k:
            primes[j]=0
            j=j+i
print(primes)

