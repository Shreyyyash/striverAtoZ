def LongestSubarray(arr,k):
    n=len(arr)
    count=0
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum=sum+arr[j]
            if sum==k:
                count=max(count,j-i+1)
        
    return count

arr=[2,3,5,1,9,2,3,2,3]
k=10
a=LongestSubarray(arr,k)
print(a)