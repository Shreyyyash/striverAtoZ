# Leetcode 75
# Dutch National Flag algorithm by Dijkstra

def SortArry(nums):
    n=len(nums)
    low = 0
    mid = 0
    high = len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            
    return nums
    
arr=[2,0,2,1,1,0]
# arr=[0,1,0,2,0,2]
print(SortArry(arr))

# count1=0
# count2=0
# count3=0
# for i in nums:
#     if i==0:
#         count1+=1
#     elif i==1:
#         count2+=1
#     else:
#         count3+=1
        
# for i in range(count1):
#     nums[i]=0
# for i in range(count1,count1+count2):
#     nums[i]=1
# for i in range(count1+count2,len(nums)):
#     nums[i]=2