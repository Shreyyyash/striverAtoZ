# Given two sorted arrays of size n and m respectively, find their union. The Union of two arrays can be defined as the common and distinct elements in the two arrays. Return the elements in sorted order.

def findUnion(arr1,arr2):
    m=len(arr1)
    n=len(arr2)
    i,j=0,0
    result=[]
    
    while i<m and j<n:
        
        # to skip duplicates in arr1
        if i > 0 and i < m and arr1[i] == arr1[i - 1]:
            i += 1
        # to skip duplicates in arr2
        if j > 0 and j < n and arr2[j] == arr2[j - 1]:
            j += 1
        
        if i < m and j < n:
            if arr1[i]>arr2[j]:
                result.append(arr2[j])
                j+=1
            elif arr1[i]<arr2[j]:
                result.append(arr1[i])
                i+=1
            
            elif arr1[i]==arr2[j]:
                result.append(arr1[i])
                i+=1
                j+=1
            
    while i<m:
        result.append(arr1[i])
        i+=1
    
    while j<n:
        result.append(arr2[j])
        j+=1

    return result


arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 3, 5, 6]
a=findUnion(arr1,arr2)
print(a)