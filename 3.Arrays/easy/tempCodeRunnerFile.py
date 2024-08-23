def singleNumber(nums):
    dic={}
    count=1
    n=len(nums)
    for i in range(n):
        if nums[i] in dic:
            dic[nums[i]]=count+1
        else:
            dic[nums[i]]=count
    for key, value in dic.items():
        if value == 1:
            return key