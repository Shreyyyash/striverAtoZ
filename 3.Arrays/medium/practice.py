def twosu(nums,target):
    n=len(nums)
    hash_map={}
    for i in range(n):
        if target-nums[i] in hash_map:
            return [hash_map[target-nums[i]],i]
        else:
            hash_map[nums[i]]=i
        

arr=[2,3,7,3]
target=9
print(twosu(arr,target))