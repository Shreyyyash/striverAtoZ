def findSquareRoot(n):
    low=1
    high=n
    ans=0

    while low<=high:
        mid=(low+high)//2

        if mid*mid>n:
            high=mid-1
        else:
            ans=mid
            low=mid+1
            

    return ans

    
n=30
print(findSquareRoot(n))