class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #find the length of the row
        n = len(matrix[0])
        #length of the column
        m = len(matrix)

    

        #this solution is O(mlogn) and space complexity is constant

        #this iterator is for the row.
        for i in range(m):
            left = 0
            right = n-1
            

            #while loop for searching for each row
            while left<=right:
                #create the middle pointer
                mid = left+(right-left)//2
                if target<matrix[i][mid]:
                    #then we move the right pointer
                    right = mid-1
                elif target>matrix[i][mid]:
                    left = mid+1
                else: 
                    return True
        return False