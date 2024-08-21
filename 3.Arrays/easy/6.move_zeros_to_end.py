# 283. Move Zeroes

def move_zeros(nums):
    n=len(nums)
    left_index=0
    for right_index in range(n):
        if nums[right_index]!=0:
            nums[left_index],nums[right_index]=nums[right_index],nums[left_index]
            left_index+=1
    return nums

arr=[0,1,0,3,12]
a=move_zeros(arr)
print(a)