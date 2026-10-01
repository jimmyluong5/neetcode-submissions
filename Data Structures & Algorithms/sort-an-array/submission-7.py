class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(arr):
            #base case
            #is if the array is empty
       
            if len(arr) <=1:
                return arr

            #get the middle pointer
            mid = len(arr)//2

            #make the left arr nd right arr
            left_arr = arr[0:mid]
            right_arr = arr[mid:]

            #sort the arrays
            mergesort(left_arr)
            mergesort(right_arr)

            #we have to add the elements from each arr if they are smaller
            #like add the smallest element from each arr to the main arr
            i=0
            j=0
            k=0
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    arr[k] = left_arr[i]
                    i+=1
                    k+=1
                else:
                    arr[k]=right_arr[j]
                    k+=1
                    j+=1
            
            while i < len(left_arr):
                arr[k] = left_arr[i]
                k+=1
                i+=1

            while j < len(right_arr):
                arr[k] = right_arr[j]
                k+=1
                j+=1
            return arr
        #we do mergesort
        return mergesort(nums)