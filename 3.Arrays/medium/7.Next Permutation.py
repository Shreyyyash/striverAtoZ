def nextPermutation(nums):
    n=len(nums)
    i=n-2
    # Find first element from the right that is not in decreasing order; here nums[1]
    while i>=0 and nums[i]>=nums[i+1]:
        i-=1
    
    # find the smallest element from the right that is greater than that number i.e (i); here nums[4]
    if i>=0:
        j=n-1
        while nums[j]<=nums[i]:
            j-=1
        # swap two elements
        nums[i], nums[j] = nums[j], nums[i]
    
    # reverse the elements from i+1 to end which makes them in increasing order from i+1 to find next permutation
    nums[i + 1:] = reversed(nums[i + 1:])
    return nums
    

    
# nums=[1,2,3]
nums=[2,1,5,4,3,0,0]
# nums=[2,2,4,5,0,2,4]
a=nextPermutation(nums)
print(a)