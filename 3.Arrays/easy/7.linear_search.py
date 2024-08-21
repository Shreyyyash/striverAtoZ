def liner_serach(arr,k):
    for i in arr:
        if i==k:
            return True
    else:
        return False

def binary_serach(arr,k):
    n=len(arr)
    left=0
    right=n-1
    while left<=right:
        mid=left+(right - left)//2
        if arr[mid]==k:
            return True
        elif arr[mid]>k:
            right=mid-1
        else:
            left=mid+1
    return False

arr=[1,3,5,6,8,9,10]
a=binary_serach(arr,3)
print(a)