def longestConsecutive(nums):
    if not nums:
        return 0
    nums_set=set(nums)
    max_streak=0
    for num in nums_set:
        if num-1 not in nums_set:
            current_num = num
            current_streak = 1
            # print(current_num)
            while current_num + 1 in nums_set:
                current_num = current_num+1
                current_streak += 1
        max_streak = max(max_streak, current_streak)
    
    return max_streak


nums=[100, 200, 1, 2, 3, 4]
print(longestConsecutive(nums))

# nums = sorted(set(nums))  # Sort and remove duplicates
#     longest_streak=1
#     current_streak=1

#     for i in range(1,len(nums)):
#         if nums[i] == nums[i-1] + 1:
#             current_streak += 1
#         else:
#             longest_streak = max(longest_streak, current_streak)
#             current_streak = 1

#     return max(longest_streak, current_streak)
