# as both rows and cols are sorted there are two ways to travel
# 1. travel from (0,c)
# 2. travel from 9=(r,0)
# increase decrease values according to target
from typing import List
class Solution:
    # 1st method
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     rows=len(matrix)
    #     cols=len(matrix[0])
    #     r=0
    #     c=cols-1

    #     while r<rows and c>=0:
    #         if matrix[r][c]==target:
    #             return True
    #         elif matrix[r][c]<target:
    #             r+=1
    #         else:
    #             c-=1
    #     return False

    # 2nd method
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        r=rows-1
        c=0
        while r>=0 and c<cols:
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]<target:
                c+=1
            else:
                r-=1
                
        return False

    

matrix = [[1,4,7,11,15],
          [2,5,8,12,19],
          [3,6,9,16,22],
          [10,13,14,17,24],
          [18,21,23,26,30]]
target = 14
a=Solution()
print(a.searchMatrix(matrix,target))