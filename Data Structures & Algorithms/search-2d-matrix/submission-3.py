class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        m = len(matrix)

        for i in range(m):
            left = 0
            right = n-1
            while left<=right:
                mid = left+(right-left)//2
                if target>matrix[i][mid]:
                    left = mid+1
                elif target<matrix[i][mid]:
                    right = mid-1
                else: 
                    return True
        return False