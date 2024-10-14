def findNRoot(n,m):
    low=1
    high=m
    ans=0

    while low<=high:
        mid=(low+high)//2
        val=mid**n
        if val>m:
            high=mid-1
        else:
            ans=mid
            low=mid+1
    return ans

m=81
n=3
print(findNRoot(n,m))