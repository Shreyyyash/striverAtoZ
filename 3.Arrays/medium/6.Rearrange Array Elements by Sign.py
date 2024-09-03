def rearrangeArray(nums):
    n=len(nums)
    arr1=[]
    arr2=[]
    arr3=n*[]
    count=0
    for i in range(n):
        if nums[i]>0:
            arr1.append(nums[i])
        else:
            arr2.append(nums[i])
    while count <n//2:
        arr3.append(arr1[count])
        arr3.append(arr2[count])
        count+=1

    return arr3


nums=[3,1,-2,-5,2,-4]
a=rearrangeArray(nums)
print(a)