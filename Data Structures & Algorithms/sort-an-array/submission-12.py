class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #mergeosrt
        #create the function
        def mergesort(arr):
            #base case
            if len(arr) <= 1:
                return arr
            #create the mid pointer
            mid = len(arr)//2

            #create the left and right arr
            left_arr = arr[:mid]
            right_arr = arr[mid:]

            #sort the left then right
            mergesort(left_arr)
            mergesort(right_arr)

            #then we need to create the pointers
            i = 0
            j = 0
            k = 0
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    arr[k] = left_arr[i]
                    k+=1
                    i+=1
                else:
                    arr[k] = right_arr[j]
                    k+=1
                    j+=1
            
            #then if one of them arrays is smaller than the other
            while j < len(right_arr):
                arr[k]=right_arr[j]
                k+=1
                j+=1
            while i < len(left_arr):
                arr[k]=left_arr[i]
                k+=1
                i+=1
            
            return arr

        return mergesort(nums)