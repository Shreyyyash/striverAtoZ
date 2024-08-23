def findMaxConsecutiveOnes(nums):
    count=0
    max_count=0
    n=len(nums)
    for i in range(n):
        if nums[i]==1:
            count+=1
            # max_count=max(count,max_count)
            if count>max_count:
                max_count=count 
        else:
            count=0      
               

    return max_count


arr=[1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1]
a=findMaxConsecutiveOnes(arr)
print(a)