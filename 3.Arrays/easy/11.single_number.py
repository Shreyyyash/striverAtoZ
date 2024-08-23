#136
def singleNumber(nums):
    # hashmap={}
    # for num in nums:
    #     hashmap[num]=hashmap.get(num,0)+1
    # for key, value in hashmap.items():
    #     if value == 1:
    #         return key
    
    # we can do it using xor
    result=0
    for num in nums:
        result=result^num
    return result

arr=[4,1,2,1,2]
a=singleNumber(arr)
print(a)

    # count=1
    # n=len(nums)
    # for i in range(n):
    #     if nums[i] in hashmap:
    #         hashmap[nums[i]]=count+1
    #     else:
    #         hashmap[nums[i]]=count
    # for key, value in hashmap.items():
    #     if value == 1:
    #         return key