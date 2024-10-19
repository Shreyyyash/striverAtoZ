from typing import List
class Solution:
    def searchMatrix(self,matrix,target):
        rows = len(matrix)
        cols = len(matrix[0])
        total = rows * cols
        low=0
        high= total -1
        while low<=high :
                mid=(low+high)//2
                r=mid//cols
                c=mid%cols
                if matrix[r][c] ==  target:
                        return True
                elif matrix[r][c]<target:
                        low=mid+1
                else:
                        high=mid-1
        return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
a=Solution()
print(a.searchMatrix(matrix=matrix,target=target)) 

#  O(n+log(m))
# def binary_search(self,nums,target):
#         low=0
#         high=len(nums)-1
#         if nums[low] <= target <= nums[high]:
#             while low<=high:
#                 mid =(low+high)//2
#                 if nums[mid]==target:
#                     return True
#                 elif nums[mid]< target:
#                     low=mid+1
#                 else:
#                     high=mid-1
#         else:
#             return False

#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         n=len(matrix)
#         for i in range(n):
#             if self.binary_search(matrix[i],target):
#                 return True
#         return False
# col=len(matrix[0])
        # row=len(matrix)
        # for i in range(row):
        #     for j in range(col):
        #         if matrix[i][j]==target:
        #             return True
        # return False