def leaderArray(nums):
    n=len(nums)
    ans=[]
    max_elem = nums[n-1]
    ans.append(nums[n-1])
    for i in range(n-2,-1,-1):
        if nums[i]>max_elem:
            ans.append(nums[i])
            max_elem=nums[i]
    
    return ans



arr = [10, 22, 12, 3, 0, 6]
print(leaderArray(arr))