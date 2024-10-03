def minSubarray(nums, p):
    array_sum=sum(nums)
    remainder=array_sum%p
    hash_map={}
    min_count=len(nums)
    current_sum=0
    current_remainder=0

    for i, num in enumerate(nums):
        current_sum += nums[i]
        current_remainder = current_sum % p

        needed_rem = (current_remainder - remainder) % p
        print(needed_rem)

        if needed_rem in hash_map:
            min_count = min(min_count, i - hash_map[needed_rem])
        else:
            hash_map[current_remainder % p] = i
    
    return hash_map



nums = [6,3,5,2]
p = 9
print(minSubarray(nums,p))