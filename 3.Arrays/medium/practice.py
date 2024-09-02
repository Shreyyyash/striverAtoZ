def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count=1
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:
            count+=1
    
    return count


nums = [1, 1, 2, 3, 3, 4, 5, 5, 6]

length = removeDuplicates(nums)
print("New length:", length)
# print("Array after removing duplicates:", nums[:length])

