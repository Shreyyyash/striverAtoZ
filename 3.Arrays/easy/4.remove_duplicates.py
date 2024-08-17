# def removeDuplicates(arr):
#     dic={}
#     result=[]
#     for item in arr:
#         if item in dic:
#             dic[item]+=1
#         else:
#             dic[item]=1
#             # result.append(item)
#             result=result+[item]  
#     print(dic,"\n")
#     return result
# arr=[1,1,2,3,3,4,5,1,6,3,8]
# a=removeDuplicates(arr)
# print(a)

"Without USing extra Space"
# leecode problem for sorted array
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        write_index=1
        for read_index in range(1,len(nums)):
            if nums[read_index]!=nums[read_index-1]:
                nums[write_index]=nums[read_index]
                write_index+=1
            # print(nums)
        print(nums)
        return write_index   

s=Solution()
# nums=[0,0,1,1,1,2,2,3,3,4]
nums=[1,2,3,3,4,4,5]
b=s.removeDuplicates(nums)
print(b)

"Using Set"
# def removeDuplicates(arr):
#     seen = set()
#     result = []
#     for item in arr:
#         if item not in seen:
#             seen.add(item)
#             result.append(item)
#     return result

# arr = [1, 1, 2, 3, 3, 4, 5, 1, 6, 3]
# result = removeDuplicates(arr)
# print(result)
