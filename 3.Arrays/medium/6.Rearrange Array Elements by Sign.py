def rearrangeArray(nums):
    n=len(nums)
    ans = [0]*n
    positive,negative=0,1
    for i in range(n):
        if nums[i]>0:
            ans[positive]=nums[i]
            positive+=2
        else:
            ans[negative]=nums[i]
            negative+=2
    
    return ans
    

nums=[3,1,-2,-5,2,-4]
a=rearrangeArray(nums)
print(a)

# arr1=[]
#     arr2=[]
#     arr3=n*[]
#     count=0
#     for i in range(n):
#         if nums[i]>0:
#             arr1.append(nums[i])
#         else:
#             arr2.append(nums[i])
#     while count <n//2:
#         arr3.append(arr1[count])
#         arr3.append(arr2[count])
#         count+=1

#     return arr3
