class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #imma do it my way
        #create the vars for length of matrix and length of row
        n = len(matrix[0]) #length of a row
        m = len(matrix) #length of a column

        left = 0
        right = n-1

        #just binary search each row then move to the next column
        #need an iterating var to move to the next row
        for i in range(m):
            left = 0
            right = n-1
            while left <= right:
                mid = left+(right-left)//2
                if target < matrix[i][mid]:
                    #then target on the left
                    right = mid-1
                elif target> matrix[i][mid]:
                    left = mid+1
                else:
                    return True
        return False

            