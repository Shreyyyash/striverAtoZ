# def left_rotate(arr,pos):
#     n=len(arr)
#     pos=pos%n
#     arr2=[]
#     for i in range(n):
#         arr2.append(arr[(i+pos)%n])
#     return arr2

# def right_rotate(arr,pos):
#     n=len(arr)
#     pos=pos%n
#     arr2=[0]*n
#     for i in range(n):
#         arr2.append(arr[(i-pos)%n])
#     return arr2
#       another approach
        # rotated = [0] * n
        # for i in range(n):
        #     rotated[(i + k) % n] = nums[i]


# without using extra space : Leetcode 189
def right_rotate(nums,k):
    n = len(nums)
    k = k % n
    
    def reverse_section(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    reverse_section(0, n - 1)
    reverse_section(0, k - 1)
    reverse_section(k, n - 1)
    return nums

def left_rotate(nums,k):
    n = len(nums)
    k = k % n
    
    def reverse_section(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    reverse_section(0,n-1)
    reverse_section(0,n-k-1)
    reverse_section(n-k,n-1)
    return nums


array=[1,2,3,4,5,6,7,8,9,0]
# array=[-1,-100,3,99]
pos=3
a=left_rotate(array,pos)
# b=right_rotate(array,pos)
print(a)