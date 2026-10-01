class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #isn't this just binary search but row by row?, idk how the left and right ptrs would work out.
        n = len(matrix[0])
        m=len(matrix) #this is the length of the matrix, which is height m
        #n is the length of a 1D array in the matrix.
        #matrix[0][] allows us to access the first row
        for i in range(len(matrix)): #bruh its not for i in range(n), the iterates over the cols, it must be rows so m
            #create the left and right pointers
            left = 0
            #ith row, and col is always 0 so left most column
            right = n-1 #right most column, and ith row.

            while left <= right:
                    #calculate the middle number for a row
                mid = left+(right-left)//2
                    #just do binary search
                if target > matrix[i][mid]:
                    #if our target is greater than a value on this row then we move left ptr
                    left = mid+1
                elif target< matrix[i][mid]:
                    right = mid-1
                else:
                    return True

            #our ptrs meet and we didn't find the value in one of the rows, so we increment i to 
            #move to the next row, which shifts all the other ptrs down
        return False #not in the matrix