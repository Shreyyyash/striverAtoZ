#Leetcode

def cheack(nums):
    length=len(nums)
    count=0
    for i in range(length):
        if nums[i]>nums[(i+1)%length]:
            count+=1
        print(f"Checking: nums[{i}] > nums[{(i + 1) % length}] -> {nums[i]} > {nums[(i + 1) % length]} -> count = {count}")
    print(count)
    if count>1:
        return False
    else:
        return True



a=[2,1,3,4]
b=cheack(a)
print(b)

# def check(array):
#     for i in range(len(array)-1):
#         if array[i]<array[i+1]:
#             isSorted=True 
#         else:
#             isSorted=False
#             break    
#     if isSorted==True:
#         print("Sorted")
#     else:
#         print("not Sorted")

# Recursive

# def isSorted(array,n):
#     if n==0 or n==1:
#         return True
    
#     elif array[n-1]<array[n-2]:
#         return False
    
#     return isSorted(array,n-1)

        
# # array=[3,7,4,5,9,2,8]
# array=[1,2,3,4,5]
# n=len(array)
# a=isSorted(array,n)
# print(a)
